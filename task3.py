import scipy.linalg as sl
import numpy as np

N=20
A=np.zeros((N,N)) 
i,j=np.indices(A.shape) 

A[i==j]=1
A[i==j+1]=1
A[i==j+2]=1

B=np.arange(N)
C=np.linalg.solve(A,B)

print (C);
