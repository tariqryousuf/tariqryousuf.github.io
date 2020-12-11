

## Tariq Yousuf and Mark Geha

[Project Repository](https://github.com/tariqryousuf/tariqryousuf.github.io) 

## Prior Work

Gesture Recognition is an emerging field with a breadth of use ranging from improved human-computer interactions, medical care, and numerous more scientific and simply enjoyable applications.
In this project, we are analyzing two open-source, efficient, and low-complexity gesture recognition algorithms in hopes of understanding the best approach for ultra-low power microcontrollers and accelerometers. We will test each of these approaches using the common gestures tested between each research paper in order to accurately represent its effectiveness. The most ideal method of testing would come down to the accuracy of the detection and inclusion of noise and approximations.  Furthermore, we will evaluate relevant considerations in gesture control such as user and time dependency, robustness in recognizing gestures with slight difference from training samples, and associated complexity with each approach. All these evaluations will occur on an Arduino Nano BLE Sense 33 and will all utilize real-time accelerometer and gyroscopic data and classification results. This will allow us to accurately create patterns and compare the detection algorithms.


The first approach is based on research paper (1) which utilizes Dynamic Time Warping in order to classify hand gestures. These hand gestures are designed to be mutually exclusive from each other and only rely on full hand/arm motion (rather than finger motion). Thus, the Nano BLE Sense will be mounted on the arm of the user during testing. To ensure that the margin of error is minimized during initial testing, there will be a secure strap to hold the Arduino such that its detected motions are almost identical to that of the hand.

The second approach is based on research paper (4) instead relies on a Gaussian Kernel Support Vector Machine classification in order to recognize hand gestures. Furthermore, this approach uses a Haar Wavelet transform in order to reduce noise, user dependence, and classification sensitivity. Note that this approach is designed for the same form of gestures as research paper (1), thus we will use the same testing apparatus. This will ensure that our comparisons are not only accurate, but also emphasize the differences in the algorithms by maintaining a controlled variable, the motions. More details about both of these approaches can be found in the References section.

Both of these approaches represent common techniques for simple gesture recognition; a more demanding recognition task may require more complicated approaches such as Convolutional
Neural Networks and Hidden Markov Models. However, through this analysis, we instead hope to be able to make an accurate, educated recommendation for simple gesture recognition tasks
without the need for significantly computational classification techniques.   

