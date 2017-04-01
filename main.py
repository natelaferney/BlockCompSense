from scipy.ndimage import imread
from scipy.misc import imsave
import numpy as np
import CompressImage as cs
import Reconstruction as recon

def main():
    #Read in image
    img = imread('a.png')
    num_rows = img.shape[0]
    num_cols = img.shape[1]
    dim = img.shape[2]
    bs = 16
    subrate = .1
    lambduh = 12
    y1, Phi1 = cs.CompressImage(img[:,:,0], bs, subrate)
    y2, Phi2 = cs.CompressImage(img[:,:,1], bs, subrate)
    y3, Phi3 = cs.CompressImage(img[:,:,2], bs, subrate)
    reconstructedImg = np.zeros(img.shape)
    print "Reconstructing channel 1..."
    reconstructedImg[:,:,0] = recon.Reconstruction(y1, Phi1, bs, num_rows, num_cols, lambduh)
    reconstructedImg[:,:,1] = recon.Reconstruction(y2, Phi2, bs, num_rows, num_cols, lambduh)
    reconstructedImg[:,:,2] = recon.Reconstruction(y3, Phi3, bs, num_rows, num_cols, lambduh)
    imsave("reconstructed.png", reconstructedImg)


main()
    
