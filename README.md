## Tariq Yousuf and Mark Geha

## Abstract

Gesture Recognition is an emerging field with a breadth of use ranging from improved human-computer interactions, medical care, and numerous more applications.
In this project, we are attempting to build a robust, efficient gesture recognition application to allow recognition of shapes drawn on a 2-D surface. 
By leveraging the accelerometer and TinyML support built into the Arduino Nano BLE Sense 33, we hope to be able to recognize many common shapes irrespective of the user. 
We foresee difficulty collecting enough training data to ensure a robust model; therefore, we will be especially diligent on selecting a classifier that won’t overfit to our own handwriting.

Digits present another significant challenge and our ability to accurately and robustly identify digits may be diminished compared to that of shapes. 
While these numbers may simply be a combination of intricate shapes, the challenge would be determining the differences between them. 
While shape detection has been utilized and developed before, we must ensure that this model can operate successfully and be altered for other applications. 
Thus, we hope to first develop strong recognition of shapes and then evaluate our model before proceeding towards digit recognition.

## References 

(1) [uWave: Accelerometer-based personalized gesture recognition and it applications](https://www.sciencedirect.com/science/article/abs/pii/S1574119209000674) \
This research article presents uWave, a higly-efficient, low-complexity method of gesture recognition using Dynamic Time Warping. This research paper boasts 
an approach that requires small amounts of training data and very little computational capabilites, however this approach relies on a simple and naive classifier.
Dynamic Time Warping, and its tranformation into a classifier in this research paper, would struggle to identify gestures that differ from the training data. Nevertheless,
this approach may prove adequate in certain situations for the gestures tested, thus this method will serve as a baseline classifier in this analysis.

(2) [Gesture Recognition using Accelerometer and ESP](https://create.arduino.cc/projecthub/mellis/gesture-recognition-using-accelerometer-and-esp-71faa1) \
This application uses the Example-based Sensor Predictions source code (referenced below) in order to classify real-time accelerometer data from an Arduino.
This application facilitates an efficient method of producing useful training data and testing various gestures through a GUI. This application will run on our
local computer, but the source code is designed for Arduino and can be easily deployed to various microcontroller. Thus, we believe it is appropraiate to use
this application due to these benifits. 

(3) [Example-based Sensor Predictions](https://github.com/damellis/ESP) \
This github repository provides the source code for the above application. This repository includes an implementaiton of Dynamic Time Warping that can be easily ported to Arduino.
We hope to ensure that this classifier can run on the Arduino Nano BLE Sense 33 for completenes. Note that this classifier is slightly different than that offered in (1), but 
it still relies completely on Dynamic Time Warping. Thus we beleive that it is a strong representation of the uWaves classifier.


(4) [Gesthaar: An accelerometer-based gesture recognition method and its application in NUI driven pervasive healthcare](https://ieeexplore.ieee.org/abstract/document/6152471) \
This research paper presents Gesthaar as a robust gesture recognition classifier utilizing Haar Transforms and Gaussian Kernel Support Vector Machine Classifier. This paper presents this
approach as an alternatuve to the Dynamic Time Warping Classificantion method presented in (1). Based on the research paper, this classifier should be significantly more user and time independent
compared to Dynamic Time Warping classification techniques. This method is more computationally complex than the approach in (1), however the Nano BLE Sense should be able to easily handle
this algorithm. We will compare this classifier to (1) through various relevant requirements of gesture control. 

(5) [Even Smaller Machine Learning Models for your MCU](https://eloquentarduino.github.io/2020/02/even-smaller-machine-learning-models-for-your-mcu/) \
This github webpage walks through the process of training a Gaussian Kernel SVM classifier in Python and porting that model to C. Thus, this model could be run on any microcontroller
with enough capabilites. We will use this method to train and import the Gaussian Kernel SVM to the Nano Sense BLE, and then test the effectiveness of the strategy suggested in (4). 

(6) [Haar Transform Library for C](https://people.sc.fsu.edu/~jburkardt/c_src/haar/haar.html) \
This code repository provided by Florida State University offers the Haar and Inverse Haar Transform implemented in C. Thus, this code can be easily ported to the Nano BLE sense in order to replicate the approach used in (3)




