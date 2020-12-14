# Tariq Yousuf and Mark Geha

[Project Repository](https://github.com/tariqryousuf/tariqryousuf.github.io) 

## Table of Contents
* [Introduction](#introduction) <br />
* [Prior Works and Experimental Setup](#prior-works-and-experimental-setup) <br />
* [Pre-Improved Implementation](#pre-improved-implementation) <br />
* [Haar Wavelet Transform](#haar-wavelet-transform) <br />
* [Dynamic Time Warping](#dynamic-time-warping) <br />
* [RBF Kernel SVM](#rbf-kernel-svm) <br />
* [Experimental Results](#experimental-results) <br />
* [Improvements to RBF Kernel SVM](#improvements-to-rbf-kernel-svm) <br />
* [Gaussian Noise](#gaussian-noise) <br />
* [SMOTE](#smote) <br />
* [Improved Experimental Results](#improved-experimental-results) <br />
* [Timeline](#timeline) <br />
* [References](#references) <br />



# Introduction

Gesture Recognition is an emerging field with a breadth of use ranging from improved human-computer interactions, medical care, and numerous more scientific and simply enjoyable applications.
In this project, we are analyzing Dynamic Time Warping and RBF Kernel SVM in hopes of understanding the best approach for ultra-low power microcontrollers and accelerometers. 
Both of these algorithms are open-source, efficient, low-complexity, and prevelant in gesture recognition applications. 
We will test each of these approaches using the common gestures tested between each research paper in order to accurately represent its effectiveness. 
The most ideal method of testing would come down to the accuracy of the detection and inclusion of noise and approximations.  
Furthermore, we will evaluate relevant considerations in gesture control such as user and time dependency, robustness in recognizing gestures with slight difference from training samples, and associated complexity with each approach. All these evaluations will occur on an Arduino Nano BLE Sense 33 and will all utilize real-time accelerometer and gyroscopic data and classification results. This will allow us to accurately create patterns and compare the detection algorithms.
Once that analysis is complete, we will experiment with methods of improving our classification under these constraints by adding Gaussian Noise and utelizing SMOTE to better balance our training data. Finally, we will compare the accuracy of our methods to that of a high-complexity Neural Network classifier in order to vest understand the trade-offs made between the different classifiers.

## Prior Works and Experimental Setup  

The first approach we will study is based on research paper (1) which utilizes Dynamic Time Warping (DTW) in order to classify hand gestures. These hand gestures are designed to be mutually exclusive from each other and only rely on full hand/arm motion (rather than finger motion). The reserach paper suggests a very simplified version of DTW with relatively high complexity, thus we will improve upon their approach to run efficiently on the Arduiono.
For our purposes, the Nano BLE Sense will be mounted on the arm of the user during testing. To ensure that the margin of error is minimized during initial testing, there will be a secure strap to hold the Arduino such that its detected motions are almost identical to that of the hand.

The second approach is based on research paper (4) instead relies on a Gaussian Kernel Support Vector Machine classification in order to recognize hand gestures.
Furthermore, this approach uses a Haar Wavelet transform in order to reduce fetaures, noise, user dependence, and classification sensitivity. Note that this approach is designed for the same form of gestures as research paper (1), thus we will use the same testing apparatus. 
This will ensure that our comparisons are not only accurate, but also emphasize the differences in the algorithms by maintaining a controlled variable, the motions. More details about both of these approaches can be found in the Implementation section.

Both of these approaches represent common techniques for simple gesture recognition; a more demanding recognition task may require more complicated approaches such as Convolutional Neural Networks and Hidden Markov Models. 
However, through this analysis, we instead hope to be able to make an accurate, educated recommendation for simple gesture recognition tasks without the need for significantly computational classification techniques.   

Finally, we will make continuous improvements on all of the aformentioned methods in order to improve classification for a wide variety of users in different enviornments. Through this report, we hope to develop the most effective gesture recogniton classifier, and then finally compare it to a Neural Netowrk classifier.   


# Pre-Improved Implementation

We will now introduce Haar Wavelet Transform, Dynamic Time Warping, and RBF Kernel SVM and discuss how these algorithms were implemeted on Arduiono. Initial improvements made to the algorithms based on the aformentioned research papers are discussed here; further improvements to these methods using training data augmentations will be introduced once these methods have been thuroughly analyzed. 

## Haar Wavelet Transform

The Haar Wavelet transform was proposed in research paper (4) as a method of reducing features, noise, and other small-signal pertubations that could lead to misclassification. 
For our uses, we utilized the Haar Wavelet tranform as an averaging function, which could decopose a N-feature signal to  N/2 -1 feature signal using the below formula:

<img src="https://render.githubusercontent.com/render/math?math=s_k = (x_{2k} - x_{2k-1})/2"> 

where x is the original signal, s is the reduced-feature signal, and k is from 0 to N/2 - 1. 
By recursively using this transform, a signal can be further decomposed to a smaller feature space. 

For our project, we reduced our 128-feature accelerometer data (for each axis) from the Arduiono, and reduced it to a 31-feature signal. 
As shown below, this tranform significantly reduces the noise of the signal while maintaining the large-signal waveform. 
Furthermore, any computations on the signals will be significantly faster because the each signal is now 75% smaller. 

![128_feature](/Images/Raw_128_feature.png)
![31_feature](/Images/Filtered_31_feature.png)

## Dynamic Time Warping

Dynamic Time Warping operates by comparing a sample to various templates and determining which template is closest to the sample. 
The euclidian distance used between the sample and each template in order to genearate a cost matrix which is then used to determine the best-fit template.
The below figures taken from research paper (1) best summarize this algorithm and provide a graphical interpretation. 

![dtw_graph](/Images/DTW_graph.jpg)
![31_feature](/Images/DTW_tree.jpg)

By looping through the entire time range of the sample and the templates, this algorithm makes an effort to reduce time-dependencies. 
However, we will later see that this naive template matching results in highly inaccurate results in very inaccurate results when non-ideal samples are used.
Furthermore, note that this algorithm is of the order <img src="https://render.githubusercontent.com/render/math?math=O(mn^2)"> since sample must warp through each m template, givem that they both have n features.
In order to significantly reduce the complexity of Dynamic Time Warping, we employed the Haar Wavelet tranform to reduce the features for each dimension from 128 to 31. Research paper (1) offered no such feature reduction techniques, and instead did all the classification using a PC rather than a microcontroller.
This optimizaiton allowed us to efficiently run DTW on the Arduino with accuracy expected of this classifier. 

## RBF Kernel SVM

RBF Kernel SVM instead operates by using a non-linear boundary and Support Vectors to accuracy and efficiently classify the samples in linear time. 
Based on resarch paper (4), the SVM classifier opearates on 31-feature Haar transformed data. 
As explaineb below, this classifier offered a easily-deployable, efficient, and accurate alternative to Dynamic Time Warping

We trained our SVM classifier in Pycharm using the sklearn package. Using a grid search, we found best test accuracy with a gamma of 0.01 and a C of 1.
Once the model had been trained, we used the [micromlgen](https://eloquentarduino.github.io/2020/02/even-smaller-machine-learning-models-for-your-mcu/) library to convert our classifier to C.
This package offered a straightforward method of converting our classifier from Python to C, which then could easily be implemented onto the Arduino.


# Experimental Results 

Setting up the system with a normalized environment and as accurate motions as possible, we get the following results that show a successful classification by both the SVM and the DTW techniques.

![SVM Normal](/Images/SVM_Normal.png)
![DTW Normal](/Images/DTW_Normal.png)

Next, we looked to see how speed of motion would affect the classification as people that utilize gesture recognition in games should not be forced to simply rely on one speed.

![SVM Slow](/Images/SVM_Slow.png)
![DTW Slow](/Images/DTW_Slow.png)

We can see that the SVM is a better classification technique when it comes to a slower speed. A lot of the faults with the DTW seemed to come from the sampling size and there would be an early or late classification. For example, a lot of Left Arrow motions would be detected as Right Arrow motions when the Arduino was returned back to the center. This was only detected when the speed was slowed down, showing that there is a bit more speed dependency with the DTW.

Finally, we looked at implementing our own environmental noise by tilting the Arduino forward at a 45 degree angle. This was encouraged by the concept of video game players leaning forward and not simply holding the controller at a level point. Angular dependence should be limited when it comes to gaming as any sort of tilt causing a problem would seem unfair and not enjoyable. 45 degrees was chosen as it felt like a limit when it comes to comfort level of the player.

![SVM 45](/Images/SVM_45.png)
![DTW 45](/Images/DTW_45.png)

As we can see, the SVM has a much better ability when it comes to angular dependence while the DTW is unable to differentiate its values from the Down Arrow. This leads us to believe that the downward tilt provides values that are much more sensitive to differentiation and not ideal for gaming.

# Improvements to RBF Kernel SVM

Based on the above results, we can see that, between the two models, the SVM is clearly a better solution when it comes to noisy environments and non-ideal gestures. Since our aim is to provide the best possible solution, we want to look at improving these responses as best as we can.
In order to improve our classification, we added Gaussian noise to all of our data, and then expanded our training data using SMOTE.
These processes used to improve our training dataset were presented to us by Professor Srivastava and J.Vikranth Jeyakumar.

## Gaussian Noise 

The process used for including Gaussian noise in the training data simply consisted of adding a sample of a Gaussian distribution to each training example.
The Gaussian distribution had zero mean and a standard deviation that is half of the specific example. 
This standard deviation had to be emperically selected to best improve the training data; too large of a standard deviation could cause misclassification and two small would be filtered away by the Haar transform.


## SMOTE 

SMOTE (Synthetic Minority Oversampling Technique) is a data augmentation technique used to boost the number of miniority examples in a training dataset.
Part of the Sklearn package, this technique is readily available for many applications, and we used it to boost the outliers in our dataset.
We used Adaptive Synthetic Sampling (ADASYN), an extension of the SMOTE package, which generates minority examples at locations inversely proportional to the density of that class at that location.
ADASYN can be easily visualized in the below figures taken from referece (Note that our training data is much more linearly-separable than the below example):

Before ADASYN:

![Before_ADASYN](/Images/Scatter-Plot-of-Imbalanced-Binary-Classification-Problem.png)

After ADASYN:

![After_ADASYN](/Images/Scatter-Plot-of-Imbalanced-Dataset-with-Adaptive-Synthetic-Sampling-ADASYN.png)


We theorized that we could use this method to increase samples in regions that our training data didn't emphasize, and thus increase accuracy of non-ideal gestures.
Note that our training data already contained non-ideal gestures that have vastly different accelerometer data than ideal gestures, so we hypothesized that this method would create more of these non-ideal examples and thus force the SVM to place more weight on these examples.
With enough fine-tuning, we could find a balance where this process improved non-ideal gesture recognition without diminishing ideal gesture recognition accuracy. 


# Improved Experimental Results

With the addition of SMOTE to the system, we can see that the accuracy of the system improves to a noticeable point. While SMOTE was only applied to the Up Arrow data and the Left Arrow data, we can see that the accuracy for other motions also improves. Improving the sampling data of a single motion also decreases the amount of misclassifications that occur with different motions, ultimately limiting the choices and ensuring there are less mistakes. The changes are noticeable in the reduced amount of misclassified Up and Left Arrow motions and overall accuracy on those two themselves.

![SVM SMOTE Normal](/Images/SVM_SMOTE_Normal.png)
![SVM SMOTE Slow](/Images/SVM_SMOTE_Slow.png)
![SVM SMOTE 45](/Images/SVM_SMOTE_45.png)

## Conclusion

Our initial goal with this investigation was to determine the best possible classification technique in which gesture recognition can be applied. Through research, we found two main techniques, the SVM and the DTW Techniques, that were both widely used and successful in their own way. What we found was that the SVM, while more complicated, was much more accurate and could be used to overcome noise while the DTW was quick and simple, but highly inaccurate when it came to non-ideal motions.

In our research, we aimed to find the best technique for gaming situations where gesture recognition would be utilized by players to achieve goals. With this goal in mind, it became clear that the SVM is the better option to classify different gestures in these specific types of environments.

To fully hit every aspect, we were introduced to the idea of SMOTE which could help improve our classification techniques and decided to apply that to our already successful SVM model. In the end, it was able to provide the accuracy that we needed to get our overall successful classifications in the 90% or higher.

## Timeline

Week 5 - Find relevant references, source code examples, and software packages in order to ensure an accurate and effective analysis.

Week 6/7 - Set up platforms for both recognition approaches, and ensure Arduino implementations adhere to methodology outlined in research papers. Difficulty comes down to utilizing the software and incorporating data collection techniques into the code so that we can determine accuracy of detection.

Week 8 - Collect training data, and evaluate ideal case test data in order to validate claims on research paper. Prepare YouTube Presentation.

Week 9 - Evaluate all relevant gesture control parameters, and rigorously test non-ideal gestures. 

Week 10 - Finalize all Evaluations, Prepare final report and YouTube presentation.  

## References 

(1) [uWave: Accelerometer-based personalized gesture recognition and it applications](https://www.sciencedirect.com/science/article/abs/pii/S1574119209000674) \
This research article presents uWave, a highly-efficient, low-complexity method of gesture recognition using Dynamic Time Warping. This research paper boasts an approach that requires small amounts of training data and very little computational capabilities, however, this approach relies on a simple and naive classifier. Dynamic Time Warping, and its transformation into a classifier in this research paper, would struggle to identify gestures that differ from the training data. Nevertheless, this approach may prove adequate in certain situations for the gestures tested, thus this method will serve as a baseline classifier in this analysis; this comes from our desire to test the actual model itself, so we can determine accuracy of both intended and extraneous solutions.

(2) [Wikipedia: Dynamic Time Warping](https://en.wikipedia.org/wiki/Dynamic_time_warping) \
This Wikipedia page provides a simple implementation of Dynamic Time Warping in MATLAB, which we were easily able to convert to C and then implement on the Arduino.

(3) [Arduino TensorFlow Lite Tutorial](https://github.com/arduino/ArduinoTensorFlowLiteTutorials) \
This GitHub repository provided us with source code we used to collect training data, and skeleton code that we used classify gestures in real-time. Although we didn't use TinyML or TensorFlow Lite, this repository provided many resources for getting started with gesture recognition on an Arduino. 

(4) [Gesthaar: An accelerometer-based gesture recognition method and its application in NUI driven pervasive healthcare](https://ieeexplore.ieee.org/abstract/document/6152471) \
This research paper presents Gesthaar as a robust gesture recognition classifier utilizing Haar Transforms and Gaussian Kernel Support Vector Machine Classifier. This paper presents this
approach as an alternative to the Dynamic Time Warping Classification method presented in (1). Based on the research paper, this classifier should be significantly more user and time independent
compared to Dynamic Time Warping classification techniques. This will help us not only filter out noise, which is ideal, but also ensure there is minimal margin of error amongst users. As there are two of us, this testing can be performed. This method is more computationally complex than the approach in (1), however the Nano BLE Sense should be able to easily handle this algorithm. We will compare this classifier to (1) through various relevant requirements of gesture control. 

(5) [Even Smaller Machine Learning Models for your MCU](https://eloquentarduino.github.io/2020/02/even-smaller-machine-learning-models-for-your-mcu/) \
This GitHub webpage walks through the process of training a Gaussian Kernel SVM classifier in Python and porting that model to C. Thus, this model could be run on any microcontroller with enough capabilities. We used the package presented in this website (micromlgen) to import the Gaussian Kernel SVM to the Nano Sense BLE, and then test the effectiveness of the strategy suggested in (4).

(6) [Haar Transform Library for C](https://people.sc.fsu.edu/~jburkardt/c_src/haar/haar.html) \
This code repository provided by Florida State University offers the Haar and Inverse Haar Transform implemented in C. Thus, this code can be easily ported to the Nano BLE sense in order to replicate the approach used in (4).

(7) [Discrete Haar Wavelet Transform](https://www.codeproject.com/Articles/683663/Discrete-Haar-Wavelet-Transformation) \
This article offered further explanation of the Haar Wavelet transform, and examples that assisted us in implementing it on the Arduino.

(8) [SMOTE Package](https://github.com/scikit-learn-contrib/imbalanced-learn) \
This is the repository that contains the SMOTE imbalanced learn package that we used to improve our training data.

(9) [SMOTE for Imbalanced Classification in Python](https://machinelearningmastery.com/smote-oversampling-for-imbalanced-classification/) \
This website offered various extenstions of the SMOTE library, which introduced ADASYN as a method of balancing training data using the inverse of the density of the minority class. 
 