# Measuirng Planar objets with OpenCV-python

## Motivation

Implementation of the algorithm to find real world coordinates from a USB Microsoft Camera and a Raspberry pi. 
The process is analogous to the used in MATLAB to measure planar objects. 
The core idea is to develop a program with the functionality of the MATLAB camera calibration application into an embedding system with purposes of developing autonomous robots equipped with computer vision algorithms.
The work developed is based on the tutorials from OpenCV with python and MATLAB to calibrate a pinhole camera.

## Pinhole Camera

Pinhole cameras are widely used for computer vision tasks because price accessibility and the features that can be extracted form an image are rich enough about the environment information. 
The relationship between world points and the camera points is given by the following matrix equation.

