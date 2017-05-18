# BlockCompSense

This is a project to implement a basic compressive sensing algorithm in Python (2.7 or 3.6).
It also requires Numpy 1.11 and Scipy 0.17.

An image is compressed by dividing it into distinct blocks which are then reshaped into 
column vectors. These column vectors are then multiplied by a random gaussian matrix.

If the image is RGB, then each color channel has its own compression matrix.

The image is reconstructed the BCS-SPL algorithm using a Discrete Cosine Transform 
as the sparse basis.

When the reconstructed image is finished, it is saved to the disk.

