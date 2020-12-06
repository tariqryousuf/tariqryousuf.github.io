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
const int reducedSamples = 31;
int samplesRead = numSamples;

// Used for DTW
double x_input_data[numSamples];
double y_input_data[numSamples];
double z_input_data[numSamples];
int cost_matrix[reducedSamples][reducedSamples];


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

      

     

      // record the samples
      x_input_data[samplesRead] = (double) aX;
      y_input_data[samplesRead] = (double) aY;
      z_input_data[samplesRead] = (double) aZ;

      // print the data in CSV format
      /*
      Serial.print(ax);
      Serial.print(',');
      Serial.print(ay);
      Serial.print(',');
      Serial.print(az);
      
   
      Serial.println();
      */

      samplesRead++;

      if (samplesRead == numSamples) {
        // add an empty line if it's the last sample
		double x_haar_1[(numSamples/2) -1], y_haar_1[(numSamples/2) -1], z_haar_1[(numSamples/2) -1];
        haar_transform(x_input_data, x_haar_1, numSamples);
        haar_transform(y_input_data, y_haar_1, numSamples);
        haar_transform(z_input_data, z_haar_1, numSamples);
        double x[31], y[31], z[31];
        haar_transform(x_haar_1, x, 64);
        haar_transform(y_haar_1, y, 64);
        haar_transform(z_haar_1, z, 64);
        int features[reducedSamples][3];
        for (int i = 0; i < 31; i++)
        {
          features[i][0] = non_linear_quantization(x[i]);
          features[i][1]= non_linear_quantization(y[i]);
          features[i][2] = non_linear_quantization(z[i]);
        }
        int dtw_result_1 = dtw(features, circle_1);
        int dtw_result_2 = dtw(features, reverse_circle_1);
        int dtw_result_3 = dtw(features, downward_arrow_1);
        int dtw_result_4 = dtw(features, upward_arrow_1);
        int dtw_result_5 = dtw(features, left_arrow_1);
        int dtw_result_6 = dtw(features, right_arrow_1);
        int cost_array[6] = {dtw_result_1, dtw_result_2, dtw_result_3, dtw_result_4, dtw_result_5, dtw_result_6};
        int min_idx = min_cost(cost_array, 6);
        if (min_idx == 0)
          Serial.print("Clockwise Circle");
        else if (min_idx == 1)
          Serial.print("Counterclockwise Circle");
        else if (min_idx == 2)
           Serial.print("Downward Arrow");
        else if (min_idx == 3)
           Serial.print("Upward Arrow");
        else if (min_idx == 4)
           Serial.print("Left Arrow");
        else
          Serial.print("Right Arrow");
        Serial.println();
        /*
        Serial.print(dtw_result_1);
        Serial.println();
        Serial.print(dtw_result_2);
        Serial.println();
        */
      }
    }
  }
}

int dtw(int sample[][3], int reference[][3])
{
  for (int i = 0; i < reducedSamples; i++)
  {
    for (int j = 0; j < reducedSamples; j++)
    {
      cost_matrix[i][j] = INT_MAX;
    }
  }
  cost_matrix[0][0] = 0;
  

  for (int i = 1; i < reducedSamples; i++)
  {
    for (int j = 1; j < reducedSamples; j++)
    {
      int cost = (int) d3_dist(sample[i], reference[j]);
      cost_matrix[i][j] = cost + min3(cost_matrix[i-1][j], cost_matrix[i][j-1], cost_matrix[i-1][j-1]);
    }
  }
  return cost_matrix[reducedSamples-1][reducedSamples-1]; 
}
