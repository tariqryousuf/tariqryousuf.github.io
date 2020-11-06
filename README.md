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

(1) [uWave: Accelerometer-based personalized gesture recognition and it applications](https://www.sciencedirect.com/science/article/abs/pii/S1574119209000674)
This research article presents uWave, a higly-efficient, low-complexity method of gesture recognition using Dynamic Time Warping. This research paper boasts 
an approach that requires small amounts of training data and very little computational capabilites, however this approach relies on a simple and naive classifier.
Dynamic Time Warping, and its tranformation into a classifier in this research paper, would struggle to identify gestures that differ from the training data. Nevertheless,
this approach may prove adequate in certain situations for the gestures tested, thus this method will serve as a baseline classifier in this analysis.

(2) [Gesthaar: An accelerometer-based gesture recognition method and its application in NUI driven pervasive healthcare](https://ieeexplore.ieee.org/abstract/document/6152471)

(3) [An accelerometer based handwriting recognition of English alphabets using basic strokes](https://ieeexplore.ieee.org/abstract/document/8227846)



