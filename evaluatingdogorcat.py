import numpy as np
import matplotlib.pyplot as plt

def s(z):
    if z <= 0:
        return 0
    return 1

# load w and b
w = np.load("w.npy")
b= np.load("b.npy")
b= b[0]

#load the test and prepare with same setting
X_test = np.load("mycatdog1.npy")
n_rows, n_cols = 3,3
fig, axs = plt.subplots(n_rows, n_cols)
axs = axs.ravel()
for i in range(n_rows*n_cols):
    #display image
    im = X_test[i].reshape((64,64,3))
    axs[i].imshow(im)
    # predict X_test[i]
    y_hat = s(np.dot(X_test[i], w)+b)
    if y_hat == 0:
        axs[i].set_title("predicted output: cat")
    else:
        axs[i].set_title("predicted output: dog")
plt.show()