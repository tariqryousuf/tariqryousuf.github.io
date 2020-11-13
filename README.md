## Tariq Yousuf and Mark Geha

[Project Repository](https://github.com/tariqryousuf/tariqryousuf.github.io) \ 

## Abstract

Gesture Recognition is an emerging field with a breadth of use ranging from improved human-computer interactions, medical care, and numerous more scientific and simply enjoyable applications.
In this project, we are analyzing two open-source, efficient, and low-complexity gesture recognition algorithms in hopes of understanding the best approach for ultra-low power microcontrollers and accelerometers. We will test each of these approaches using the common gestures tested between each research paper in order to accurately represent its effectiveness. The most ideal method of testing would come down to the accuracy of the detection and inclusion of noise and approximations.  Furthermore, we will evaluate relevant considerations in gesture control such as user and time dependency, robustness in recognizing gestures with slight difference from training samples, and associated complexity with each approach. All these evaluations will occur on an Arduino Nano BLE Sense 33 and will all utilize real-time accelerometer and gyroscopic data and classification results. This will allow us to accurately create patterns and compare the detection algorithms.


The first approach is based on research paper (1) which utilizes Dynamic Time Warping in order to classify hand gestures. These hand gestures are designed to be mutually exclusive from each other and only rely on full hand/arm motion (rather than finger motion). Thus, the Nano BLE Sense will be mounted on the arm of the user during testing. To ensure that the margin of error is minimized during initial testing, there will be a secure strap to hold the Arduino such that its detected motions are almost identical to that of the hand.

The second approach is based on research paper (4) instead relies on a Gaussian Kernel Support Vector Machine classification in order to recognize hand gestures. Furthermore, this approach uses a Haar Wavelet transform in order to reduce noise, user dependence, and classification sensitivity. Note that this approach is designed for the same form of gestures as research paper (1), thus we will use the same testing apparatus. This will ensure that our comparisons are not only accurate, but also emphasize the differences in the algorithms by maintaining a controlled variable, the motions. More details about both of these approaches can be found in the References section.

Both of these approaches represent common techniques for simple gesture recognition; a more demanding recognition task may require more complicated approaches such as Convolutional
Neural Networks and Hidden Markov Models. However, through this analysis, we instead hope to be able to make an accurate, educated recommendation for simple gesture recognition tasks
without the need for significantly computational classification techniques.   

## Timeline

Week 5 - Find relevant references, source code examples, and software packages in order to ensure an accurate and effective analysis.

Week 6/7 - Set up platforms for both recognition approaches, and ensure Arduino implementations adhere to methodology outlined in research papers. Difficulty comes down to utilizing the software and incorporating data collection techniques into the code so that we can determine accuracy of detection.

Week 8 - Collect training data, and evaluate ideal case test data in order to validate claims on research paper. Prepare YouTube Presentation.

Week 9 - Evaluate all relevant gesture control parameters, and rigorously test non-ideal gestures. 

Week 10 - Finalize all Evaluations, Prepare final report and YouTube presentation.  

## References 

(1) [uWave: Accelerometer-based personalized gesture recognition and it applications](https://www.sciencedirect.com/science/article/abs/pii/S1574119209000674) \
This research article presents uWave, a highly-efficient, low-complexity method of gesture recognition using Dynamic Time Warping. This research paper boasts an approach that requires small amounts of training data and very little computational capabilities, however, this approach relies on a simple and naive classifier. This ideally helps us collect necessary data and test whether small amounts of training data can optimally provide a solid amount of successful testing results. Dynamic Time Warping, and its transformation into a classifier in this research paper, would struggle to identify gestures that differ from the training data. Nevertheless, this approach may prove adequate in certain situations for the gestures tested, thus this method will serve as a baseline classifier in this analysis; this comes from our desire to test the actual model itself, so we can determine accuracy of both intended and extraneous solutions.

(2) [Gesture Recognition using Accelerometer and ESP](https://create.arduino.cc/projecthub/mellis/gesture-recognition-using-accelerometer-and-esp-71faa1) \
This application uses the Example-based Sensor Predictions source code (referenced below) in order to classify real-time accelerometer data from an Arduino. This application facilitates an efficient method of producing useful training data and testing various gestures through a GUI. This application will run on our local computer, but the source code is designed for Arduino and can be easily deployed to various microcontroller. Thus, we believe it is appropriate to use
this application due to these benefits. The application of this model will be ideal for testing purposes and will allow us to properly collect data to determine accuracy.

(3) [Example-based Sensor Predictions](https://github.com/damellis/ESP) \
This GitHub repository provides the source code for the above application. This repository includes an implementation of Dynamic Time Warping that can be easily ported to Arduino. We hope to ensure that this classifier can run on the Arduino Nano BLE Sense 33 for completeness. Note that this classifier is slightly different than that offered in (1), but it still relies completely on Dynamic Time Warping. Thus, we believe that it is a strong representation of the uWaves classifier.


(4) [Gesthaar: An accelerometer-based gesture recognition method and its application in NUI driven pervasive healthcare](https://ieeexplore.ieee.org/abstract/document/6152471) \
This research paper presents Gesthaar as a robust gesture recognition classifier utilizing Haar Transforms and Gaussian Kernel Support Vector Machine Classifier. This paper presents this
approach as an alternative to the Dynamic Time Warping Classification method presented in (1). Based on the research paper, this classifier should be significantly more user and time independent
compared to Dynamic Time Warping classification techniques. This will help us not only filter out noise, which is ideal, but also ensure there is minimal margin of error amongst users. As there are two of us, this testing can be performed. This method is more computationally complex than the approach in (1), however the Nano BLE Sense should be able to easily handle this algorithm. We will compare this classifier to (1) through various relevant requirements of gesture control. 

(5) [Even Smaller Machine Learning Models for your MCU](https://eloquentarduino.github.io/2020/02/even-smaller-machine-learning-models-for-your-mcu/) \
This GitHub webpage walks through the process of training a Gaussian Kernel SVM classifier in Python and porting that model to C. Thus, this model could be run on any microcontroller with enough capabilities. We will use this method to train and import the Gaussian Kernel SVM to the Nano Sense BLE, and then test the effectiveness of the strategy suggested in (4). Luckily, our device allows us to perform such tasks, so testing is within our bandwidth.

(6) [Haar Transform Library for C](https://people.sc.fsu.edu/~jburkardt/c_src/haar/haar.html) \
This code repository provided by Florida State University offers the Haar and Inverse Haar Transform implemented in C. Thus, this code can be easily ported to the Nano BLE sense in order to replicate the approach used in (4).
