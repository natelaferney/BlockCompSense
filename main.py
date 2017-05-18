from scipy.ndimage import imread
from scipy.misc import imsave
import numpy as np
import compressimage as cs
import reconstruction as recon

def main():
    #Read in image
    img = imread('a.png')
    num_rows = img.shape[0]
    num_cols = img.shape[1]
    dim = img.shape[2]
    bs = 16
    subrate = .1
    lambduh = 12
    y1, phi1 = cs.compress_image(img[:,:,0], bs, subrate)
    y2, phi2 = cs.compress_image(img[:,:,1], bs, subrate)
    y3, phi3 = cs.compress_image(img[:,:,2], bs, subrate)
    reconstructed_img = np.zeros(img.shape)
    print("Reconstructing channel 1...")
    reconstructed_img[:,:,0] = recon.reconstruction(y1, phi1, bs, num_rows, num_cols, lambduh)
    print("Reconstructing channel 2...")
    reconstructed_img[:,:,1] = recon.reconstruction(y2, phi2, bs, num_rows, num_cols, lambduh)
    print("Reconstructing channel 3...")
    reconstructed_img[:,:,2] = recon.reconstruction(y3, phi3, bs, num_rows, num_cols, lambduh)
    imsave("reconstructed.png", reconstructed_img)


main()
    
