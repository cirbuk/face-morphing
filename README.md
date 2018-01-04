Face Morphing
===================


This is a tool which creates a morphing effect. It takes two facial images as input and returns a video morphing from the first image to the second.

----------

Usage
-------------
Clone this repository and run setup.py and requirements.txt. Also install below mentioned dependencies. Then pass the following command-line arguments to \_\_init\_\_.py in **morphing** folder.
```
python3 __init__.py face/body path_to_first_image path_to_second_image duration_of_video frame_rate path_where_video_is_to_be_saved
```
- Note that presently only **face** is allowed as first argument.
- Also instead of the path to image file, Python **File Object** of that image can also be passed in as an argument.

Examples
-------------
![A photo of Ben Affleck](https://raw.githubusercontent.com/KubricIO/face-morphing/master/demos/ben.jpg)
![A phtot of Morgan Freeman](https://raw.githubusercontent.com/KubricIO/face-morphing/master/demos/morgan.jpg)
Using the below command you can generate a video depicting morphing.
```
python3 __init__.py face ben.jpg morgan.jpg 5 25 morphing-example.mp4
```
![Morphed Video](https://raw.githubusercontent.com/KubricIO/face-morphing/master/demos/morphing-example.gif)

How It Works
-------------
1. Find point-to-point correspondences between the two images using Dlib's **Facial Landmark Detection**.
2. Find the **Delaunay Triangulation** for the average of these points.
3. Using these corresponding triangles in both initial and final images, perform **Warping** and **Alpha Blending** and obtain intermediate images to be used in creating videos.
4. Use **ffmpeg** to return a video from above created frames.

Requirements
-------------
These are the requirements apart from what is mentioned in *requirements.txt* :

>- FFMPEG
>- X11 (Xquartz on macOS)
>- Boost and Boost-Python
>- Dlib

For macOS : https://www.learnopencv.com/install-dlib-on-macos/     
For Linux : https://www.learnopencv.com/install-dlib-on-ubuntu/       
For Windows : https://www.learnopencv.com/install-opencv-3-and-dlib-on-windows-python-only/

Citations
-------------
Most of the help for this project came from this post http://www.learnopencv.com/face-morph-using-opencv-cpp-python/
