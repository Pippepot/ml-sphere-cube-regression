# Cube to Sphere Interpolation Predictor

This repository contains a machine learning model that predicts the degree of interpolation between a cube and a sphere mesh.
The convolutional neural network (CNN) model achieves an average error of ~0.066 when prediction sphere-cube interpolation in the range of [0, 1]

Images ranging from cube(0) to sphere(1)

![](https://github.com/Pippepot/ml-sphere-cube-regression/blob/master/data/output_179.png)
![](https://github.com/Pippepot/ml-sphere-cube-regression/blob/master/data/output_181.png)
![](https://github.com/Pippepot/ml-sphere-cube-regression/blob/master/data/output_52.png)

&emsp; &emsp; &emsp; &emsp; &emsp;0.0067&emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;0.5024&emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;0.9994

## Content
- spherecube-prediction.ipynb - CNN prediction model
- spherecube.blend - Blender model
- spherecube.blend.py - Blendtorch image generation
- sphercube.py - Creates dataset by launching multiple instances of spherecube.blend.py 
