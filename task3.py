import scipy.linalg
import numpy as np

A=np.zeros((15,15))
i,j=np.indices(A.shape)

A[i==j]=1
A[i==j+1]=1
A[i==j+2]=1

print (A);
B=np.arange(15)
C=np.linalg.solve(A,B)
print (B)
print (C)
