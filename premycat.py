import numpy as np
from PIL import Image

#number of Image
N = 5
#prepare an empty array
#1 row for 1 Image
D = np.empty((2*N,12288))
for i,t in enumerate(['cat','dog']):
    for j in range(N):
        fname = "./cat or dog/mycat/%s.%d.jpg" % (t,j)
        print(fname)
        #load image
        im = Image.open(fname)
        #resize
        im = im.resize((64,64))
        #convert img to numpy array
        im=np.array(im)
        im = im.flatten()
        #append image into data set
        D[N*i+j, :] = im
# make it 0.0-1.0
D = D/225

np.save("mycatdog1.npy",D )