# YUGA: a non commercial embedded pupil estimation as simulated virtual input for video games 

## An eye tracker (using k-NN classification and PCA/LDA feature extraction) born out of survival, speed, and necessity.

### About the name

YUGA is an acronym born out of the combination of the following words: e*Y*e p*U*pil *G*aze tr*A*cker
~~Also it's a reference to the Yu-Gi-Oh! protagonist of the newest franchise entry, Yuga of Yu-Gi-Oh! Sevens. Even though I don't really like the new entry at all and think Yuga's a stupid name (I tried to think of something that would rhyme with VRAINS, which I enjoyed much better, but only obtained TRAINS which sounded dumb to me) I can't think of anything else and am having my quarter life Yu-Gi-Oh! crisis.~~
This is my first attempt at an eye tracker using commodity software (because I bought the wrong camera) using k-NN framework to track the pupil. Using OpenCV as simulated input for camera axis movement.
 
 - **Author:** Melody Asghari
 - **Deadline:** November 23rd, 2020
 - **Last modified:** 2020-11-24

## Features

  * Artificial Neural Network in Python or C++
  * Back-propagation (RPROP)
  * trains the artificial Neural Network
  * sequence labeling
  * Uses structural SVM tools for pupil detection in images
  * Whatever the python equivalent of iostream and streambuf objects that enables TCIP sockets to interoperate with the C++ iostreams library.

### Algorithm mockup

![img1](img/algorithm-detail.png)

### Estimation with _k_-Nearest-Neighbors algorithm
  - Convert searches to a _k_-NN model to estimate gaze direction.
  - Find the images with the most similarity to the nearest neighbors.
  - Compute the distance from the inputs to the label examples.
  - Take its corresponding label as output.
  - Take the median of their corresponding labels = output.
  - Output goes to mouse implementation for controlling camera axes

![img2](img/idk_more_diagrams.png)

## Implementation
### 
This demo showcases the work of gaze estimation model. The corresponding pre-trained model `gaze-estimation-adas-0002` is delivered with the product.
The demo also relies on the following auxiliary networks:
-   `face-detection-retail-0004` or face-detection-adas-0001 detection networks for finding faces
-   `head-pose-estimation-adas-0001`, which estimates head pose in Tait-Bryan angles, serving as an input for gaze estimation model
-   `facial-landmarks-35-adas-0002`, which estimates coordinates of facial landmarks for detected faces.
    - The keypoints at the corners of eyes are used to locate eyes regions required for the gaze estimation model
-   `open-closed-eye-0001`, which estimates eyes state of detected faces. 

Parameters for the algorithm from `OpenCV`:
  - PCA
- dimensionality reduction (using PCA)
  - Hough / Fisher / HAAR Cascades
  - SVM
  - kNN
    - kNN (weighted)
    
Image Transformations with `numpy`:
  - RGB->Greyscale
  - crop
  - bilinear
  - HOG
  - Histogram transformations

## Requirements

  This project requires a lot of software dependencies, therefore I suggest [this guide](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/) and creating a container-ized solution to the dependency problem through `pip` and `virtualenv`. I used pycharm to generate a `virtualenv` on the remote laptop and installed everything locally through the debian package manager on the Pi (most of the dependencies come shipped with Raspbian already).
  * `numpy`
  * `Image` (a lot of other projects use PIL/pillow but that's lame _and_ depreciated!)
  * `OpenVINO`
  * `Adaboost` (To train HAAR Cascade classifiers)
  * `matplotlib`
  * `Inference Engine`
  * `PyGame`
  * `OpenCV`
  * `dlib`

### (Open Source) Datasets referenced
  * [Labelled Pupils in the Wild (LPW)](https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/labelled-pupils-in-the-wild-lpw/) 
  * [Gaze Estimation in the Wild (MPIIGaze)](https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/appearance-based-gaze-estimation-in-the-wild/)
  * [FANN](http://leenissen.dk/fann/wp/)
  * [GazeCapture](https://gazecapture.csail.mit.edu/)
  * [OpenCV library](http://opencv.willowgarage.com/wiki/)
  * [LC Technologies](http://www.eyegaze.com)
  * [ITU Gaze Tracker](http://www.gazegroup.org)
  * [The BioID database](http://support.bioid.com/downloads/facedb/index.php)
  * [ANN](http://www.cs.umd.edu/%7Emount/ANN/)
  * [FaceScrub](http://vintage.winklerbros.net/facescrub.html)
  * [VGG](http://www.robots.ox.ac.uk/~vgg/data/vgg_face/)
  * So, I actually had more references here, but both my libreoffice file / pycharm did not save any version of it I guess, so those are all gone. They were just links to wikipedia/wolframalpha/openCV/openVINO articles on the specific models and how to train them, so forth. I guess not useful for the graders, but it would have been good reference for me or anyone who looks at this if it's public. Perhaps I will re-find them but I am way too lazy right now and I definitely can't remember what I linked specifically off the top of my head.
