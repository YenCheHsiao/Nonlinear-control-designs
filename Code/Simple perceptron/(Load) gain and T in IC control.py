# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:05:46 2023

@author: ych22001
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from pyswarms.single.global_best import GlobalBestPSO
#import seaborn as sns
#sns.set_context('talk')

t_step = 1e-1
t = np.arange(0, 100, t_step)

lamb_np = np.arange(0, 2, t_step)
T_np = np.arange(0, 5, t_step)

#%% Simple perceptron
Converge = np.load('Converge.npy')

xa1 = np.empty(np.size(Converge))
xa2 = np.empty(np.size(Converge))
za = np.empty(np.size(Converge))
i = 0

for l_idx in range(0,len(lamb_np)):
    for T_idx in range(0,len(T_np)):
        if Converge[l_idx][T_idx] != -1:
            xa1[i] = T_np[T_idx]
            xa2[i] = lamb_np[l_idx]
            if Converge[l_idx][T_idx] == 1:
                za[i]=1
            elif Converge[l_idx][T_idx] == 0:
                za[i]=-1
            i = i + 1
            
ones = np.ones((1,len(xa1)))
X_temp = np.stack((xa1, xa2), axis=0)
X = np.concatenate((ones, X_temp), axis=0)
X_Z_temp = np.stack((xa1, xa2, za), axis=0)
X_Z = np.concatenate((ones, X_Z_temp), axis=0)
X_del = np.delete(X_Z, -1, 0)

w = np.array([[1.33744429],
       [0.85195401],
       [1.31081734]])
WX = np.transpose(w)@X

labels_a = []
for i in range(len(za)):
    if za[i] == 1:
        labels_a.append("*")
    if za[i] == -1:
        labels_a.append("o")
"""Problem 7a"""
C1 = plt.scatter(xa1[(za==1)],
            xa2[(za==1)],
           marker='*',
           color='red',
           label='Class 1')
C2 = plt.scatter(xa1[(za==-1)],
            xa2[(za==-1)],
           marker='o',
           color='blue',
           label='Class 2')
plt.xlabel('$T$ [a.u.]')
plt.ylabel('$K_P$')
plt.grid()
# create a legend with both scatter and line 
# https://stackoverflow.com/questions/45070477/trying-to-create-a-legend-with-both-scatter-and-line-in-matplotlib
plt.legend([C1,C2],['Error converge to 0','Error not converge to 0'])
plt.show()

#%%
"""Problem 7b method 2"""
from sklearn.utils import shuffle
import timeit

T_base = np.linspace(0,5,100)

w_0 = np.array([[-1.07540972],
       [ 0.43306762],
       [-0.79703894]])

x2_0 = (-w_0[0]-w_0[1]*T_base)/w_0[2]

start = timeit.default_timer()
w_new_2 = w_0
w_prev_2 = w_0
# WX_old = np.transpose(w)@X

for iteration in range(10000):
    #X_shuf = shuffle(X)
    WX_new_2 = np.transpose(w_new_2)@X
    #WX_old = np.transpose(w)@X
    zb = 0
    wrong_idx = -1
    count = 0
    error_2 = 0
    X_sum = np.zeros((3,1))
    for i in range(len(za)):
        if WX_new_2[0][i] >= 0:
            if za[i] < 0:
                wrong_idx = i
                zb = -1
                X_sum = X_sum+za[i]*X[:,[i]]
                count = count + 1
        if WX_new_2[0][i] < 0:
            if za[i] >= 0:
                wrong_idx = i
                zb = 1
                X_sum = X_sum+za[i]*X[:,[i]]
                count = count + 1
    if wrong_idx != -1:
        test1 = np.ones(WX_new_2[0].shape)
        test2 = -1*np.ones(WX_new_2[0].shape)
        zb_2 = test1*(WX_new_2[0] >= 0) + test2*(WX_new_2[0] < 0)
        error_2 = np.sum(np.abs((za-zb_2)*WX_new_2[0]))
        if error_2 < 0.1:
            break
        w_new_2 = w_new_2 + (X_sum/count)
    else:
        break
    n_iter_2 = iteration
    print(n_iter_2)
    
WX_new_2 = np.transpose(w_new_2)@X
zb_2 = np.empty(len(WX_new_2[0]))
for i in range(len(WX_new_2[0])):
    if WX_new_2[0][i] >= 0:
        zb_2[i]=1
    if WX_new_2[0][i] < 0:
        zb_2[i]=-1

x2_new_2 = (-w_new_2[0]-w_new_2[1]*T_base)/w_new_2[2]

#%% Plot the parameter plane

TF0 = plt.plot(T_base[x2_0>=0], x2_0[x2_0>=0], 'm--') # initial target function
# TF = plt.plot(T_base, x2, 'k-') # target function  
TF_new_2 = plt.plot(T_base, x2_new_2, 'g-') # estimated target function  
C1 = plt.scatter(xa1[(zb_2==1)],
            xa2[(zb_2==1)],
           marker='o',
           color='blue',
           label='Error converge to 0')
C2 = plt.scatter(xa1[(zb_2==-1)],
            xa2[(zb_2==-1)],
           marker='*',
           color='red',
           label='Error not converge to 0')
plt.xlabel('$T$ [a.u.]', fontsize=20)
plt.ylabel('$K_P$', fontsize=20)
plt.xticks(np.arange(0, 5+0.1, 1), fontsize=20)
plt.yticks(np.arange(0, 2+0.1, 0.5), fontsize=20)
# create a legend with both scatter and line 
# https://stackoverflow.com/questions/45070477/trying-to-create-a-legend-with-both-scatter-and-line-in-matplotlib
plt.legend([TF0[0],TF_new_2[0],C1,C2],['Initial target','Estimated target','Error converge to 0','Error not converge to 0'],loc=(1.04, 0.5), fontsize=15) 
stop = timeit.default_timer()
plt.grid()
# plt.title('Pick all the misclassified sample and average\n N=%d, %d iterations, running time: %fs, error: %.2f'% (len(za),n_iter_2,(stop - start),error_2))
plt.title('The convergence result in the parameter plane (' + r'$T, K_P$' + ')')
plt.show()
print('Weights:' + str(w_new_2))

# Weights:[[ -5.14616891]
# [-43.81703299]
# [161.81609981]]

#%% Plot the parameter plane

# TF0 = plt.plot(T_base[x2_0>=0], x2_0[x2_0>=0], 'm--') # initial target function
# TF = plt.plot(T_base, x2, 'k-') # target function  
TF_new_2 = plt.plot(T_base, x2_new_2, 'g-') # estimated target function  
C1 = plt.scatter(xa1[(zb_2==1)],
            xa2[(zb_2==1)],
           marker='o',
           color='blue',
           label='Error converge to 0')
C2 = plt.scatter(xa1[(zb_2==-1)],
            xa2[(zb_2==-1)],
           marker='*',
           color='red',
           label='Error not converge to 0')
plt.xlabel('$T$  [a.u.]', fontsize=20)
plt.ylabel('$K_P$', fontsize=20)
plt.xticks(np.arange(0, 5+0.1, 1), fontsize=20)
plt.yticks(np.arange(0, 2+0.1, 0.5), fontsize=20)
# create a legend with both scatter and line 
# https://stackoverflow.com/questions/45070477/trying-to-create-a-legend-with-both-scatter-and-line-in-matplotlib
plt.legend([TF_new_2[0],C1,C2],[r'$g_d(T,K_P)$','Error converge to 0','Error not converge to 0'],loc=(1.04, 0.5), fontsize=15) 
stop = timeit.default_timer()
plt.grid()
# plt.title('Pick all the misclassified sample and average\n N=%d, %d iterations, running time: %fs, error: %.2f'% (len(za),n_iter_2,(stop - start),error_2))
plt.title('The convergence result in the parameter plane (' + r'$T, K_P$' + ')')
plt.show()

print('Weights:' + str(w_new_2))

# Weights:[[ -5.14616891]
# [-43.81703299]
# [161.81609981]]