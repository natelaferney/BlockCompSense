# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 23:00:58 2016

@author: nathan
"""
import numpy as np
from scipy.signal import wiener
import pywt
from scipy.stats import threshold
from scipy.fftpack import dct, idct
from CompressImage import Col2Im, Im2Col

    
def Reconstruction(y, Phi, bs, num_rows, num_cols, lambduh):
    
    tol = .001
    d_Prev = 0
    num_factor = 0
    max_iterations = 300
    x = np.dot(np.transpose(Phi), y)
    x0 = x
    num_iter = 0

    for i in range(0, max_iterations):
        x_image = Col2Im(x0, bs, num_cols, num_rows)
        x0 = Im2Col(wiener(x_image), bs)
        x = x0 + np.dot(np.transpose(Phi), (y-np.dot(Phi, x0)))   
        x_check = dct(x, norm='ortho')

        thresh = lambduh*np.sqrt(2*np.log(num_rows*num_cols))*(np.median(np.absolute(x_check)))*(1/.6745)
        np.array(threshold(x_check,thresh,None,0))
        x = idct(x_check, norm='ortho')

        x0 = x + np.dot(np.transpose(Phi), (y-np.dot(Phi, x))) 

        d = np.linalg.norm(x-x0)

        if (d_Prev !=0 ) and (d < tol):
            lambduh = lambduh*.6
            num_factor += 1
        d_Prev = d
        
        print(i)
        

    return Col2Im(x0, bs, num_cols, num_rows)