import numpy as np

#This will be the file that has to do with the compression



#This function takes our array and a given blocksize 
#and takes a block of a given image
#and reshapes it into a single dimension array.
#It does this for all blocks


#We divide the image up into blocks
#then do the reshaping.  
#The blocks that are reshaped are then 
#combined into a single array.

def im2col(image, bs):
   width = int(len(image[1,:])/bs)
   height = int(len(image[:,1])/bs)
   total_blocks = width*height
   k=0
   retim = np.zeros([bs*bs, total_blocks]) 
   for i in  range(0, height):
       for j in range(0, width):
            retim[:, k] = image[i*bs:(i+1)*bs, j*bs:(j+1)*bs].ravel()	
            k+=1
   return retim
   
def col2im(retim, bs, iw, ih):
    width = int(iw/bs)
    height = int(ih/bs)
    image = np.zeros([ih, iw])   
    k=0
    for i in  range(0, height):
        for j in range(0, width):
            image[i*bs:(i+1)*bs, j*bs:(j+1)*bs] = retim[:,k].reshape(bs, bs)	
            k+=1
    return image
   
def get_CS_matrix(n, subrate):
    A = np.random.randn(n, n)
    U,S,V = np.linalg.svd(A, full_matrices=1)     
    m = int(round(subrate*n))
    phi = U[0:m, :]
    return phi

def compress_image(image, bs, subrate):
    phi = get_CS_matrix(bs*bs, subrate)
    return np.dot(phi, im2col(image, bs)), phi


