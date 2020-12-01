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
#include "SVM.h"
#include "utility.h"

const float accelerationThreshold = 2.5; // threshold of significant in G's
const int numSamples = 128;

int samplesRead = numSamples;

double x_input_data[numSamples];
double y_input_data[numSamples];
double z_input_data[numSamples];

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


      // print the data in CSV format
      /*
      Serial.print(aX);
      Serial.print(',');
      Serial.print(aY);
      Serial.print(',');
      Serial.print(aZ);
      */

      x_input_data[samplesRead] = (double) aX;
      y_input_data[samplesRead] = (double) aY;
      z_input_data[samplesRead] = (double) aZ;
   
      //Serial.println();
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
        double features[93];
        for (int i = 0; i < 31; i++)
        {
          features[i] = x[i];
          features[i+31]= y[i];
          features[i+62] = z[i];
        }
        //Serial.print(predict(features));
        int prediction = (int) predict(features);
        //Serial.print(prediction);
        if (prediction == 0)
          Serial.print("Clockwise Circle");
        else if (prediction == 1)
          Serial.print("Counterclockwise Circle");
        else if (prediction == 2)
          Serial.print("Downward Arrow");
        else if (prediction == 3)
          Serial.print("Left Arrow");
        else if (prediction == 4)
          Serial.print("Right Arrow");
        else
          Serial.print("Upward Arrow");
        Serial.println();
      }
    }
  }
}


   
