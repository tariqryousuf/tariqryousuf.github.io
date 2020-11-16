/*
  IMU Capture
  This example uses the on-board IMU to start reading acceleration and gyroscope
  data from on-board IMU and prints it to the Serial Monitor for one second
  when the significant motion is detected.
  You can also use the Serial Plotter to graph the data.
  The circuit:
  - Arduino Nano 33 BLE or Arduino Nano 33 BLE Sense board.
  Created by Don Coleman, Sandeep Mistry
  Modified by Dominic Pajak, Sandeep Mistry
  This example code is in the public domain.
*/

#include <Arduino_LSM9DS1.h>
#include "training_data.h"
#include "utility.h"
#include "limits.h"

// Used for Sampling
const float accelerationThreshold = 2.5; // threshold of significant in G's
const int numSamples = 128;
int samplesRead = numSamples;

// Used for DTW
int input_data[numSamples][3];
int cost_matrix[numSamples][numSamples];


void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

  // print the header
  Serial.println("aX,aY,aZ");
}

void loop() {
  float aX, aY, aZ;

  // wait for significant motion
  while (samplesRead == numSamples) {
    if (IMU.accelerationAvailable()) {
      // read the acceleration data
      IMU.readAcceleration(aX, aY, aZ);

      // sum up the absolutes
      float aSum = fabs(aX) + fabs(aY) + fabs(aZ);

      // check if it's above the threshold
      if (aSum >= accelerationThreshold) {
        // reset the sample read count
        samplesRead = 0;
        break;
      }
    }
  }

  // check if the all the required samples have been read since
  // the last time the significant motion was detected
  while (samplesRead < numSamples) {
    // check if both new acceleration and gyroscope data is
    // available
    if (IMU.accelerationAvailable()) {
      // read the acceleration and gyroscope data
      IMU.readAcceleration(aX, aY, aZ);

      

      int ax = non_linear_quantization(aX);
      int ay = non_linear_quantization(aY);
      int az = non_linear_quantization(aZ);

      // record the samples
      input_data[samplesRead][0] = ax;
      input_data[samplesRead][1] = ay;
      input_data[samplesRead][2] = az;

      // print the data in CSV format
      Serial.print(ax);
      Serial.print(',');
      Serial.print(ay);
      Serial.print(',');
      Serial.print(az);
      
   
      Serial.println();

      samplesRead++;

      if (samplesRead == numSamples) {
        // add an empty line if it's the last sample
        int dtw_result_1 = dtw(input_data, circle_1);
        int dtw_result_2 = dtw(input_data, reverse_circle_1);
        if (dtw_result_1 < dtw_result_2)
          Serial.print("Circle 1 ");
        else
          Serial.print("Circle 2");
        Serial.println();
        Serial.print(dtw_result_1);
        Serial.println();
        Serial.print(dtw_result_2);
        Serial.println();
      }
    }
  }
}

int dtw(int sample[][3], int reference[][3])
{
  for (int i = 0; i < numSamples; i++)
  {
    for (int j = 0; j < numSamples; j++)
    {
      cost_matrix[i][j] = INT_MAX;
    }
  }
  cost_matrix[0][0] = 0;
  

  for (int i = 1; i < numSamples; i++)
  {
    for (int j = 1; j < numSamples; j++)
    {
      int cost = (int) d3_dist(sample[i], reference[j]);
      cost_matrix[i][j] = cost + min3(cost_matrix[i-1][j], cost_matrix[i][j-1], cost_matrix[i-1][j-1]);
    }
  }
  return cost_matrix[numSamples-1][numSamples-1]; 
}
