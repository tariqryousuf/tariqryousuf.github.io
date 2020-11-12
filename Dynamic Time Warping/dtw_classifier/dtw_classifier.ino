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

const float accelerationThreshold = 2.5; // threshold of significant in G's
const int numSamples = 119;
int input_data[numSamples][3];

int samplesRead = numSamples;

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
        int result = array_distance(input_data, circle_1, numSamples);
        Serial.print(result);
        Serial.println();
      }
    }
  }
}

int non_linear_quantization( float a )
{
  int return_value;
  if (abs(a) < 1)
    return_value = (int) (a * 10.0);
  else if (abs(a) < 2)
    return_value = 10 + (int) ((a - 1.0) * 2.0);
  else
    return_value = 16;

  return return_value;
  
}

int min3(int x, int y, int z)
{
  if ( (x < y) & (x < z) )
    return x;
  else if ( (y < x) & (y < z) )
    return y;
  else
    return z;
}

float d3_dist(int x[], int y[])
{
  return sqrt(pow((float)(x[0] - y[0]), 2) + pow((float) (x[1] - y[1]), 2) + pow((float) (x[2] - y[2]), 2));
}

int array_distance(int x[][3], int y[][3], int sample_size)
{
  int distance = 0;
  for (int i = 0; i < sample_size; i++)
  {
    distance = distance + (int) d3_dist(x[i], y[i]);  
  }
  return distance;
}
