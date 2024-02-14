# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 15:13:04 2023

@author: xiaoyenche
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
#import seaborn as sns
#sns.set_context('talk')

x1eA = 0.4165
x2eA = 0.4668
x3eA = 0.5700
x4eA = 0.7438
x5eA = 0.3215
x6eA = 0.9970
x7eA = 0.2756
x8eA = 0.4134
x9eA = 0.6647
x10eA = 0.3044
x11eA = 0.5262
x12eA = 0.4145
x13eA = 0.1484
x14eA = 0.2998
x15eA = 0.3765
x16eA = 0.2471
x17eA = 0.1336
x18eA = 0.1342
x19eA = 0.5788
x20eA = 0.1922
x21eA = 0.8766
x22eA = 0.7159
x23eA = 0.8486
x24eA = 0.1740
x25eA = 0.1433
x26eA = 0.4089
x27eA = 0
x28eA = 0
x29eA = 0.0806
x30eA = 0.6282
x31eA = 0.6915
x32eA = 0.4933


x1eB = 0.4277
x2eB = 0.4642
x3eB = 0.4511
x4eB = 0.2973
x5eB = 0.6263
x6eB = 0.7105
x7eB = 0.2645
x8eB = 0.2439
x9eB = 0.4760
x10eB = 0.8058
x11eB = 0.4606
x12eB = 0.6239
x13eB = 0.5908
x14eB = 0.6632
x15eB = 0.4680
x16eB = 0.4911
x17eB = 0.4613
x18eB = 0.4273
x19eB = 0.4853
x20eB = 0.2620
x21eB = 0.0688
x22eB = 0.2641
x23eB = 0.1024
x24eB = 0.7533
x25eB = 0.8853
x26eB = 0.5158
x27eB = 0
x28eB = 0
x29eB = 0.6772
x30eB = 0.4550
x31eB = 0.8148
x32eB = 0.4877


x1eC = 0.4712
x2eC = 0.4545
x3eC = 0.4378
x4eC = 0.2836
x5eC = 0.5298
x6eC = 0.1921
x7eC = 0.3087
x8eC = 0.1955
x9eC = 0.4758
x10eC = 0.8294
x11eC = 0.4636
x12eC = 0.6464
x13eC = 0.6214
x14eC = 0.6823
x15eC = 0.4702
x16eC = 0.7550
x17eC = 0.8022
x18eC = 0.8620
x19eC = 0.5550
x20eC = 0.3441
x21eC = 0.0621
x22eC = 0.2498
x23eC = 0.0923
x24eC = 0.7705
x25eC = 0.9007
x26eC = 0.5427
x27eC = 0
x28eC = 0
x29eC = 0.7016
x30eC = 0.5882
x31eC = 0.6413
x32eC = 0.4666


# Guess Cancer state
x1o = 0
x2o = 0
x3o = 0
x4o = 0
x5o = 1
x6o = 0
x7o = 0
x8o = 0
x9o = 0
x10o = 1
x11o = 0
x12o = 1
x13o = 1
x14o = 1
x15o = 0 
x16o = 1
x17o = 1
x18o = 1 
x19o = 1
x20o = 0
x21o = 0
x22o = 0
x23o = 0
x24o = 1
x25o = 0
x26o = 1
x27o = 0
x28o = 0
x29o = 1
x30o = 1
x31o = 1
x32o = 0

S = 0.5
n = 4
a = 0.5
b = 0.5
k = 1
s1 = 1.028
s2 = 1.281
s3 = 0.598
s4 = 0.827
s5 = 1.02
s6 = 2.244
s7 = 1.037
s8 = 1.507
s9 = 0.203
s10 = 1.299
s11 = 1.337
s12 = 0.921
s13 = 2.044
s14 = 0.678
s15 = 0.924
s16 = 0.467
s17 = 0.947
s18 = 0.242
s19 = 0.941
s20 = 0.48
s21 = 0.666
s22 = 0.232
s23 = 1.156
s24 = 0.951
s25 = 0.849
s26 = 0.698
s27 = 1.288
s28 = 0.966
s29 = 1.419
s30 = 0.401
s31 = 0.293
s32 = 1.479

xo = [x1o,x2o,x3o,x4o,x5o,x6o,x7o,x8o,x9o,x10o,x11o,x12o,x13o,x14o,x15o,x16o,x17o,x18o,x19o,x20o,x21o,x22o,x23o,x24o,x25o,x26o,x27o,x28o,x29o,x30o,x31o,x32o]
xeA = [x1eA,x2eA,x3eA,x4eA,x5eA,x6eA,x7eA,x8eA,x9eA,x10eA,x11eA,x12eA,x13eA,x14eA,x15eA,x16eA,x17eA,x18eA,x19eA,x20eA,x21eA,x22eA,x23eA,x24eA,x25eA,x26eA,x27eA,x28eA,x29eA,x30eA,x31eA,x32eA]
xeB = [x1eB,x2eB,x3eB,x4eB,x5eB,x6eB,x7eB,x8eB,x9eB,x10eB,x11eB,x12eB,x13eB,x14eB,x15eB,x16eB,x17eB,x18eB,x19eB,x20eB,x21eB,x22eB,x23eB,x24eB,x25eB,x26eB,x27eB,x28eB,x29eB,x30eB,x31eB,x32eB]
xeC = [x1eC,x2eC,x3eC,x4eC,x5eC,x6eC,x7eC,x8eC,x9eC,x10eC,x11eC,x12eC,x13eC,x14eC,x15eC,x16eC,x17eC,x18eC,x19eC,x20eC,x21eC,x22eC,x23eC,x24eC,x25eC,x26eC,x27eC,x28eC,x29eC,x30eC,x31eC,x32eC]

# Nonlinear system
def deriv(X,t):
    x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32 = X
    dx1 = (2*b*S**n)/(S**n+s32*x32**n)-k*x1
    dx2 = (a*(s1*x1**n+s9*x9**n+s14*x14**n)/3)/(S**n+(1/3)*s1*x1**n+(1/3)*s9*x9**n+(1/3)*s14*x14**n) + (2*b*S**n)/(2*S**n+s16*x16**n+s31*x31**n) - k*x2
    dx3 = (a*(s2*x2**n+s8*x8**n+s29*x29**n)/3)/(S**n+(1/3)*s2*x2**n+(1/3)*s8*x8**n+(1/3)*s29*x29**n) + (3*b*S**n)/(3*S**n+s9*x9**n+s10*x10**n+s16*x16**n) - k*x3
    dx4 = (a*s2*x2**n)/(S**n+s2*x2**n) + (b*S**n)/(S**n+s25*x25**n) - k*x4
    dx5 = (a*s13*x13**n)/(S**n+s13*x13**n) + (b*S**n)/(S**n+(1/3)*s14*x14**n+(1/3)*s17*x17**n+(1/3)*s19*x19**n) - k*x5
    dx6 = (2*b*S**n)/(S**n+(1/2)*s17*x17**n+(1/2)*s18*x18**n)-k*x6
    dx7 = (a*s20*x20**n)/(S**n+s20*x20**n) + (b*S**n)/(S**n+(1/2)*s15*x15**n+(1/2)*s32*x32**n) - k*x7
    dx8 = (2*b*S**n)/(S**n+(1/3)*s4*x4**n+(1/3)*s10*x10**n+(1/3)*s16*x16**n)-k*x8
    dx9 = (a*(s11*x11**n+s13*x13**n+s25*x25**n+s26*x26**n)/4)/(S**n+(1/4)*s11*x11**n+(1/4)*s13*x13**n+(1/4)*s25*x25**n+(1/4)*s26*x26**n) + (b*S**n)/(S**n+s29*x29**n) - k*x9
    dx10 = (a*(s11*x11**n+s12*x12**n+s13*x13**n)/3)/(S**n+(1/3)*s11*x11**n+(1/3)*s12*x12**n+(1/3)*s13*x13**n) + (b*S**n)/(S**n+s4*x4**n) - k*x10
    dx11 = (a*(s10*x10**n+s13*x13**n+s14*x14**n+s27*x27**n+s28*x28**n))/(5*S**n+s10*x10**n+s13*x13**n+s14*x14**n+s27*x27**n+s28*x28**n) + (b*S**n)/(S**n+s29*x29**n) - k*x11
    dx12 = (a*(s9*x9**n+s10*x10**n+s11*x11**n+s13*x13**n+s14*x14**n+s15*x15**n))/(6*S**n+s9*x9**n+s10*x10**n+s11*x11**n+s13*x13**n+s14*x14**n+s15*x15**n) + (b*S**n)/(S**n+s2*x2**n) - k*x12
    dx13 = (2*a*(s12*x12**n+s14*x14**n+s28*x28**n)/3)/(S**n+(1/3)*s12*x12**n+(1/3)*s14*x14**n+(1/3)*s28*x28**n) - k*x13
    dx14 = (a*(s10*x10**n+s13*x13**n+s25*x25**n+s26*x26**n+s28*x28**n))/(5*S**n+s10*x10**n+s13*x13**n+s25*x25**n+s26*x26**n+s28*x28**n) + (b*S**n)/(S**n+s2*x2**n) - k*x14
    dx15 = (a*s14*x14**n)/(S**n+s14*x14**n) + (b*S**n)/(S**n+(1/2)*s2*x2**n+(1/2)*s29*x29**n) - k*x15
    dx16 = (a*(s2*x2**n+s10*x10**n+s26*x26**n+s32*x32**n))/(4*S**n+s2*x2**n+s10*x10**n+s26*x26**n+s32*x32**n) + (3*b*S**n)/(3*S**n+s1*x1**n+s6*x6**n+s7*x7**n) - k*x16
    dx17 = (a*(s9*x9**n+s10*x10**n+s20*x20**n))/(3*S**n+s9*x9**n+s10*x10**n+s20*x20**n) + (2*b*S**n)/(2*S**n+s3*x3**n+s6*x6**n) - k*x17
    dx18 = (a*(s9*x9**n+s25*x25**n+s26*x26**n)/3)/(S**n+(1/3)*s9*x9**n+(1/3)*s25*x25**n+(1/3)*s26*x26**n) + (b*S**n)/(S**n+s6*x6**n) - k*x18
    dx19 = (2*b*S**n)/(S**n+(1/3)*s3*x3**n+(1/3)*s5*x5**n+(1/3)*s30*x30**n)-k*x19
    dx20 = (a*s1*x1**n)/(S**n+s1*x1**n) + (b*S**n)/(S**n+(1/2)*s6*x6**n+(1/2)*s17*x17**n) - k*x20
    dx21 = (a*(s22*x22**n+s23*x23**n)/2)/(S**n+(1/2)*s22*x22**n+(1/2)*s23*x23**n) + (b*S**n)/(S**n+(1/2)*s10*x10**n+(1/2)*s24*x24**n) - k*x21
    dx22 = (a*(s2*x2**n+s9*x9**n)/2)/(S**n+(1/2)*s2*x2**n+(1/2)*s9*x9**n) + (b*S**n)/(S**n+s24*x24**n) - k*x22
    dx23 = (2*b*S**n)/(S**n+s10*x10**n)-k*x23
    dx24 = (a*(s12*x12**n+s13*x13**n+s25*x25**n)/3)/(S**n+(1/3)*s12*x12**n+(1/3)*s13*x13**n+(1/3)*s25*x25**n) + (b*S**n)/(S**n+(1/2)*s2*x2**n+(1/2)*s21*x21**n) - k*x24
    dx25 = (a*(s10*x10**n+s13*x13**n)/2)/(S**n+(1/2)*s10*x10**n+(1/2)*s13*x13**n) + (b*S**n)/(S**n+s4*x4**n) - k*x25
    dx26 = (2*a*(s11*x11**n+s12*x12**n+s27*x27**n)/3)/(S**n+(1/3)*s11*x11**n+(1/3)*s12*x12**n+(1/3)*s27*x27**n) - k*x26
    dx27 = (2*a*s28*x28**n)/(S**n+s28*x28**n)-k*x27
    dx28 = -k*x28
    dx29 = (2*a*s14*x14**n)/(S**n+s14*x14**n)-k*x29
    dx30 = (2*a*s19*x19**n)/(S**n+s19*x19**n)-k*x30
    dx31 = (a*(s10*x10**n+s32*x32**n)/2)/(S**n+(1/2)*s10*x10**n+(1/2)*s32*x32**n) + (b*S**n)/(S**n+(1/2)*s7*x7**n+(1/2)*s16*x16**n) - k*x31
    dx32 = (2*a*s2*x2**n)/(S**n+s2*x2**n)-k*x32
    return [dx1,dx2,dx3,dx4,dx5,dx6,dx7,dx8,dx9,dx10,dx11,dx12,dx13,dx14,dx15,dx16,dx17,dx18,dx19,dx20,dx21,dx22,dx23,dx24,dx25,dx26,dx27,dx28,dx29,dx30,dx31,dx32]

# Controlled nonlinear system
def derivC(X,t,u1,u2):
    x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32 = X
    dx1 = (2*b*S**n)/(S**n+s32*x32**n)-k*x1
    dx2 = (a*(s1*x1**n+s9*x9**n+s14*x14**n)/3)/(S**n+(1/3)*s1*x1**n+(1/3)*s9*x9**n+(1/3)*s14*x14**n) + (2*b*S**n)/(2*S**n+s16*x16**n+s31*x31**n) - k*x2
    dx3 = (a*(s2*x2**n+s8*x8**n+s29*x29**n)/3)/(S**n+(1/3)*s2*x2**n+(1/3)*s8*x8**n+(1/3)*s29*x29**n) + (3*b*S**n)/(3*S**n+s9*x9**n+s10*x10**n+s16*x16**n) - k*x3
    dx4 = (a*s2*x2**n)/(S**n+s2*x2**n) + (b*S**n)/(S**n+s25*x25**n) - k*x4
    dx5 = (a*s13*x13**n)/(S**n+s13*x13**n) + (b*S**n)/(S**n+(1/3)*s14*x14**n+(1/3)*s17*x17**n+(1/3)*s19*x19**n) - k*x5
    dx6 = (2*b*S**n)/(S**n+(1/2)*s17*x17**n+(1/2)*s18*x18**n)-k*x6 + u2
    dx7 = (a*s20*x20**n)/(S**n+s20*x20**n) + (b*S**n)/(S**n+(1/2)*s15*x15**n+(1/2)*s32*x32**n) - k*x7
    dx8 = (2*b*S**n)/(S**n+(1/3)*s4*x4**n+(1/3)*s10*x10**n+(1/3)*s16*x16**n)-k*x8
    dx9 = (a*(s11*x11**n+s13*x13**n+s25*x25**n+s26*x26**n)/4)/(S**n+(1/4)*s11*x11**n+(1/4)*s13*x13**n+(1/4)*s25*x25**n+(1/4)*s26*x26**n) + (b*S**n)/(S**n+s29*x29**n) - k*x9
    dx10 = (a*(s11*x11**n+s12*x12**n+s13*x13**n)/3)/(S**n+(1/3)*s11*x11**n+(1/3)*s12*x12**n+(1/3)*s13*x13**n) + (b*S**n)/(S**n+s4*x4**n) - k*x10 +u1
    dx11 = (a*(s10*x10**n+s13*x13**n+s14*x14**n+s27*x27**n+s28*x28**n))/(5*S**n+s10*x10**n+s13*x13**n+s14*x14**n+s27*x27**n+s28*x28**n) + (b*S**n)/(S**n+s29*x29**n) - k*x11
    dx12 = (a*(s9*x9**n+s10*x10**n+s11*x11**n+s13*x13**n+s14*x14**n+s15*x15**n))/(6*S**n+s9*x9**n+s10*x10**n+s11*x11**n+s13*x13**n+s14*x14**n+s15*x15**n) + (b*S**n)/(S**n+s2*x2**n) - k*x12
    dx13 = (2*a*(s12*x12**n+s14*x14**n+s28*x28**n)/3)/(S**n+(1/3)*s12*x12**n+(1/3)*s14*x14**n+(1/3)*s28*x28**n) - k*x13
    dx14 = (a*(s10*x10**n+s13*x13**n+s25*x25**n+s26*x26**n+s28*x28**n))/(5*S**n+s10*x10**n+s13*x13**n+s25*x25**n+s26*x26**n+s28*x28**n) + (b*S**n)/(S**n+s2*x2**n) - k*x14
    dx15 = (a*s14*x14**n)/(S**n+s14*x14**n) + (b*S**n)/(S**n+(1/2)*s2*x2**n+(1/2)*s29*x29**n) - k*x15
    dx16 = (a*(s2*x2**n+s10*x10**n+s26*x26**n+s32*x32**n))/(4*S**n+s2*x2**n+s10*x10**n+s26*x26**n+s32*x32**n) + (3*b*S**n)/(3*S**n+s1*x1**n+s6*x6**n+s7*x7**n) - k*x16
    dx17 = (a*(s9*x9**n+s10*x10**n+s20*x20**n))/(3*S**n+s9*x9**n+s10*x10**n+s20*x20**n) + (2*b*S**n)/(2*S**n+s3*x3**n+s6*x6**n) - k*x17
    dx18 = (a*(s9*x9**n+s25*x25**n+s26*x26**n)/3)/(S**n+(1/3)*s9*x9**n+(1/3)*s25*x25**n+(1/3)*s26*x26**n) + (b*S**n)/(S**n+s6*x6**n) - k*x18
    dx19 = (2*b*S**n)/(S**n+(1/3)*s3*x3**n+(1/3)*s5*x5**n+(1/3)*s30*x30**n)-k*x19
    dx20 = (a*s1*x1**n)/(S**n+s1*x1**n) + (b*S**n)/(S**n+(1/2)*s6*x6**n+(1/2)*s17*x17**n) - k*x20
    dx21 = (a*(s22*x22**n+s23*x23**n)/2)/(S**n+(1/2)*s22*x22**n+(1/2)*s23*x23**n) + (b*S**n)/(S**n+(1/2)*s10*x10**n+(1/2)*s24*x24**n) - k*x21
    dx22 = (a*(s2*x2**n+s9*x9**n)/2)/(S**n+(1/2)*s2*x2**n+(1/2)*s9*x9**n) + (b*S**n)/(S**n+s24*x24**n) - k*x22
    dx23 = (2*b*S**n)/(S**n+s10*x10**n)-k*x23
    dx24 = (a*(s12*x12**n+s13*x13**n+s25*x25**n)/3)/(S**n+(1/3)*s12*x12**n+(1/3)*s13*x13**n+(1/3)*s25*x25**n) + (b*S**n)/(S**n+(1/2)*s2*x2**n+(1/2)*s21*x21**n) - k*x24
    dx25 = (a*(s10*x10**n+s13*x13**n)/2)/(S**n+(1/2)*s10*x10**n+(1/2)*s13*x13**n) + (b*S**n)/(S**n+s4*x4**n) - k*x25
    dx26 = (2*a*(s11*x11**n+s12*x12**n+s27*x27**n)/3)/(S**n+(1/3)*s11*x11**n+(1/3)*s12*x12**n+(1/3)*s27*x27**n) - k*x26
    dx27 = (2*a*s28*x28**n)/(S**n+s28*x28**n)-k*x27
    dx28 = -k*x28
    dx29 = (2*a*s14*x14**n)/(S**n+s14*x14**n)-k*x29
    dx30 = (2*a*s19*x19**n)/(S**n+s19*x19**n)-k*x30
    dx31 = (a*(s10*x10**n+s32*x32**n)/2)/(S**n+(1/2)*s10*x10**n+(1/2)*s32*x32**n) + (b*S**n)/(S**n+(1/2)*s7*x7**n+(1/2)*s16*x16**n) - k*x31
    dx32 = (2*a*s2*x2**n)/(S**n+s2*x2**n)-k*x32
    return [dx1,dx2,dx3,dx4,dx5,dx6,dx7,dx8,dx9,dx10,dx11,dx12,dx13,dx14,dx15,dx16,dx17,dx18,dx19,dx20,dx21,dx22,dx23,dx24,dx25,dx26,dx27,dx28,dx29,dx30,dx31,dx32]

# Controlled nonlinear system
def derivCSIMO(X,t,u):
    x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32 = X
    dx1 = (2*b*S**n)/(S**n+s32*x32**n)-k*x1
    dx2 = (a*(s1*x1**n+s9*x9**n+s14*x14**n)/3)/(S**n+(1/3)*s1*x1**n+(1/3)*s9*x9**n+(1/3)*s14*x14**n) + (2*b*S**n)/(2*S**n+s16*x16**n+s31*x31**n) - k*x2
    dx3 = (a*(s2*x2**n+s8*x8**n+s29*x29**n)/3)/(S**n+(1/3)*s2*x2**n+(1/3)*s8*x8**n+(1/3)*s29*x29**n) + (3*b*S**n)/(3*S**n+s9*x9**n+s10*x10**n+s16*x16**n) - k*x3
    dx4 = (a*s2*x2**n)/(S**n+s2*x2**n) + (b*S**n)/(S**n+s25*x25**n) - k*x4
    dx5 = (a*s13*x13**n)/(S**n+s13*x13**n) + (b*S**n)/(S**n+(1/3)*s14*x14**n+(1/3)*s17*x17**n+(1/3)*s19*x19**n) - k*x5
    dx6 = (2*b*S**n)/(S**n+(1/2)*s17*x17**n+(1/2)*s18*x18**n)-k*x6
    dx7 = (a*s20*x20**n)/(S**n+s20*x20**n) + (b*S**n)/(S**n+(1/2)*s15*x15**n+(1/2)*s32*x32**n) - k*x7
    dx8 = (2*b*S**n)/(S**n+(1/3)*s4*x4**n+(1/3)*s10*x10**n+(1/3)*s16*x16**n)-k*x8
    dx9 = (a*(s11*x11**n+s13*x13**n+s25*x25**n+s26*x26**n)/4)/(S**n+(1/4)*s11*x11**n+(1/4)*s13*x13**n+(1/4)*s25*x25**n+(1/4)*s26*x26**n) + (b*S**n)/(S**n+s29*x29**n) - k*x9
    dx10 = (a*(s11*x11**n+s12*x12**n+s13*x13**n)/3)/(S**n+(1/3)*s11*x11**n+(1/3)*s12*x12**n+(1/3)*s13*x13**n) + (b*S**n)/(S**n+s4*x4**n) - k*x10 + u
    dx11 = (a*(s10*x10**n+s13*x13**n+s14*x14**n+s27*x27**n+s28*x28**n))/(5*S**n+s10*x10**n+s13*x13**n+s14*x14**n+s27*x27**n+s28*x28**n) + (b*S**n)/(S**n+s29*x29**n) - k*x11
    dx12 = (a*(s9*x9**n+s10*x10**n+s11*x11**n+s13*x13**n+s14*x14**n+s15*x15**n))/(6*S**n+s9*x9**n+s10*x10**n+s11*x11**n+s13*x13**n+s14*x14**n+s15*x15**n) + (b*S**n)/(S**n+s2*x2**n) - k*x12
    dx13 = (2*a*(s12*x12**n+s14*x14**n+s28*x28**n)/3)/(S**n+(1/3)*s12*x12**n+(1/3)*s14*x14**n+(1/3)*s28*x28**n) - k*x13
    dx14 = (a*(s10*x10**n+s13*x13**n+s25*x25**n+s26*x26**n+s28*x28**n))/(5*S**n+s10*x10**n+s13*x13**n+s25*x25**n+s26*x26**n+s28*x28**n) + (b*S**n)/(S**n+s2*x2**n) - k*x14
    dx15 = (a*s14*x14**n)/(S**n+s14*x14**n) + (b*S**n)/(S**n+(1/2)*s2*x2**n+(1/2)*s29*x29**n) - k*x15
    dx16 = (a*(s2*x2**n+s10*x10**n+s26*x26**n+s32*x32**n))/(4*S**n+s2*x2**n+s10*x10**n+s26*x26**n+s32*x32**n) + (3*b*S**n)/(3*S**n+s1*x1**n+s6*x6**n+s7*x7**n) - k*x16
    dx17 = (a*(s9*x9**n+s10*x10**n+s20*x20**n))/(3*S**n+s9*x9**n+s10*x10**n+s20*x20**n) + (2*b*S**n)/(2*S**n+s3*x3**n+s6*x6**n) - k*x17
    dx18 = (a*(s9*x9**n+s25*x25**n+s26*x26**n)/3)/(S**n+(1/3)*s9*x9**n+(1/3)*s25*x25**n+(1/3)*s26*x26**n) + (b*S**n)/(S**n+s6*x6**n) - k*x18
    dx19 = (2*b*S**n)/(S**n+(1/3)*s3*x3**n+(1/3)*s5*x5**n+(1/3)*s30*x30**n)-k*x19
    dx20 = (a*s1*x1**n)/(S**n+s1*x1**n) + (b*S**n)/(S**n+(1/2)*s6*x6**n+(1/2)*s17*x17**n) - k*x20
    dx21 = (a*(s22*x22**n+s23*x23**n)/2)/(S**n+(1/2)*s22*x22**n+(1/2)*s23*x23**n) + (b*S**n)/(S**n+(1/2)*s10*x10**n+(1/2)*s24*x24**n) - k*x21
    dx22 = (a*(s2*x2**n+s9*x9**n)/2)/(S**n+(1/2)*s2*x2**n+(1/2)*s9*x9**n) + (b*S**n)/(S**n+s24*x24**n) - k*x22
    dx23 = (2*b*S**n)/(S**n+s10*x10**n)-k*x23
    dx24 = (a*(s12*x12**n+s13*x13**n+s25*x25**n)/3)/(S**n+(1/3)*s12*x12**n+(1/3)*s13*x13**n+(1/3)*s25*x25**n) + (b*S**n)/(S**n+(1/2)*s2*x2**n+(1/2)*s21*x21**n) - k*x24
    dx25 = (a*(s10*x10**n+s13*x13**n)/2)/(S**n+(1/2)*s10*x10**n+(1/2)*s13*x13**n) + (b*S**n)/(S**n+s4*x4**n) - k*x25
    dx26 = (2*a*(s11*x11**n+s12*x12**n+s27*x27**n)/3)/(S**n+(1/3)*s11*x11**n+(1/3)*s12*x12**n+(1/3)*s27*x27**n) - k*x26
    dx27 = (2*a*s28*x28**n)/(S**n+s28*x28**n)-k*x27
    dx28 = -k*x28
    dx29 = (2*a*s14*x14**n)/(S**n+s14*x14**n)-k*x29
    dx30 = (2*a*s19*x19**n)/(S**n+s19*x19**n)-k*x30
    dx31 = (a*(s10*x10**n+s32*x32**n)/2)/(S**n+(1/2)*s10*x10**n+(1/2)*s32*x32**n) + (b*S**n)/(S**n+(1/2)*s7*x7**n+(1/2)*s16*x16**n) - k*x31
    dx32 = (2*a*s2*x2**n)/(S**n+s2*x2**n)-k*x32
    return [dx1,dx2,dx3,dx4,dx5,dx6,dx7,dx8,dx9,dx10,dx11,dx12,dx13,dx14,dx15,dx16,dx17,dx18,dx19,dx20,dx21,dx22,dx23,dx24,dx25,dx26,dx27,dx28,dx29,dx30,dx31,dx32]


# Controlled nonlinear system
def derivCMIMO(X,t,u1,u2):
    x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32 = X
    dx1 = (2*b*S**n)/(S**n+s32*x32**n)-k*x1
    dx2 = (a*(s1*x1**n+s9*x9**n+s14*x14**n)/3)/(S**n+(1/3)*s1*x1**n+(1/3)*s9*x9**n+(1/3)*s14*x14**n) + (2*b*S**n)/(2*S**n+s16*x16**n+s31*x31**n) - k*x2
    dx3 = (a*(s2*x2**n+s8*x8**n+s29*x29**n)/3)/(S**n+(1/3)*s2*x2**n+(1/3)*s8*x8**n+(1/3)*s29*x29**n) + (3*b*S**n)/(3*S**n+s9*x9**n+s10*x10**n+s16*x16**n) - k*x3
    dx4 = (a*s2*x2**n)/(S**n+s2*x2**n) + (b*S**n)/(S**n+s25*x25**n) - k*x4
    dx5 = (a*s13*x13**n)/(S**n+s13*x13**n) + (b*S**n)/(S**n+(1/3)*s14*x14**n+(1/3)*s17*x17**n+(1/3)*s19*x19**n) - k*x5
    dx6 = (2*b*S**n)/(S**n+(1/2)*s17*x17**n+(1/2)*s18*x18**n)-k*x6 + u1
    dx7 = (a*s20*x20**n)/(S**n+s20*x20**n) + (b*S**n)/(S**n+(1/2)*s15*x15**n+(1/2)*s32*x32**n) - k*x7
    dx8 = (2*b*S**n)/(S**n+(1/3)*s4*x4**n+(1/3)*s10*x10**n+(1/3)*s16*x16**n)-k*x8
    dx9 = (a*(s11*x11**n+s13*x13**n+s25*x25**n+s26*x26**n)/4)/(S**n+(1/4)*s11*x11**n+(1/4)*s13*x13**n+(1/4)*s25*x25**n+(1/4)*s26*x26**n) + (b*S**n)/(S**n+s29*x29**n) - k*x9
    dx10 = (a*(s11*x11**n+s12*x12**n+s13*x13**n)/3)/(S**n+(1/3)*s11*x11**n+(1/3)*s12*x12**n+(1/3)*s13*x13**n) + (b*S**n)/(S**n+s4*x4**n) - k*x10 + u2
    dx11 = (a*(s10*x10**n+s13*x13**n+s14*x14**n+s27*x27**n+s28*x28**n))/(5*S**n+s10*x10**n+s13*x13**n+s14*x14**n+s27*x27**n+s28*x28**n) + (b*S**n)/(S**n+s29*x29**n) - k*x11
    dx12 = (a*(s9*x9**n+s10*x10**n+s11*x11**n+s13*x13**n+s14*x14**n+s15*x15**n))/(6*S**n+s9*x9**n+s10*x10**n+s11*x11**n+s13*x13**n+s14*x14**n+s15*x15**n) + (b*S**n)/(S**n+s2*x2**n) - k*x12
    dx13 = (2*a*(s12*x12**n+s14*x14**n+s28*x28**n)/3)/(S**n+(1/3)*s12*x12**n+(1/3)*s14*x14**n+(1/3)*s28*x28**n) - k*x13
    dx14 = (a*(s10*x10**n+s13*x13**n+s25*x25**n+s26*x26**n+s28*x28**n))/(5*S**n+s10*x10**n+s13*x13**n+s25*x25**n+s26*x26**n+s28*x28**n) + (b*S**n)/(S**n+s2*x2**n) - k*x14
    dx15 = (a*s14*x14**n)/(S**n+s14*x14**n) + (b*S**n)/(S**n+(1/2)*s2*x2**n+(1/2)*s29*x29**n) - k*x15
    dx16 = (a*(s2*x2**n+s10*x10**n+s26*x26**n+s32*x32**n))/(4*S**n+s2*x2**n+s10*x10**n+s26*x26**n+s32*x32**n) + (3*b*S**n)/(3*S**n+s1*x1**n+s6*x6**n+s7*x7**n) - k*x16
    dx17 = (a*(s9*x9**n+s10*x10**n+s20*x20**n))/(3*S**n+s9*x9**n+s10*x10**n+s20*x20**n) + (2*b*S**n)/(2*S**n+s3*x3**n+s6*x6**n) - k*x17
    dx18 = (a*(s9*x9**n+s25*x25**n+s26*x26**n)/3)/(S**n+(1/3)*s9*x9**n+(1/3)*s25*x25**n+(1/3)*s26*x26**n) + (b*S**n)/(S**n+s6*x6**n) - k*x18
    dx19 = (2*b*S**n)/(S**n+(1/3)*s3*x3**n+(1/3)*s5*x5**n+(1/3)*s30*x30**n)-k*x19
    dx20 = (a*s1*x1**n)/(S**n+s1*x1**n) + (b*S**n)/(S**n+(1/2)*s6*x6**n+(1/2)*s17*x17**n) - k*x20
    dx21 = (a*(s22*x22**n+s23*x23**n)/2)/(S**n+(1/2)*s22*x22**n+(1/2)*s23*x23**n) + (b*S**n)/(S**n+(1/2)*s10*x10**n+(1/2)*s24*x24**n) - k*x21
    dx22 = (a*(s2*x2**n+s9*x9**n)/2)/(S**n+(1/2)*s2*x2**n+(1/2)*s9*x9**n) + (b*S**n)/(S**n+s24*x24**n) - k*x22
    dx23 = (2*b*S**n)/(S**n+s10*x10**n)-k*x23
    dx24 = (a*(s12*x12**n+s13*x13**n+s25*x25**n)/3)/(S**n+(1/3)*s12*x12**n+(1/3)*s13*x13**n+(1/3)*s25*x25**n) + (b*S**n)/(S**n+(1/2)*s2*x2**n+(1/2)*s21*x21**n) - k*x24
    dx25 = (a*(s10*x10**n+s13*x13**n)/2)/(S**n+(1/2)*s10*x10**n+(1/2)*s13*x13**n) + (b*S**n)/(S**n+s4*x4**n) - k*x25
    dx26 = (2*a*(s11*x11**n+s12*x12**n+s27*x27**n)/3)/(S**n+(1/3)*s11*x11**n+(1/3)*s12*x12**n+(1/3)*s27*x27**n) - k*x26
    dx27 = (2*a*s28*x28**n)/(S**n+s28*x28**n)-k*x27
    dx28 = -k*x28
    dx29 = (2*a*s14*x14**n)/(S**n+s14*x14**n)-k*x29
    dx30 = (2*a*s19*x19**n)/(S**n+s19*x19**n)-k*x30
    dx31 = (a*(s10*x10**n+s32*x32**n)/2)/(S**n+(1/2)*s10*x10**n+(1/2)*s32*x32**n) + (b*S**n)/(S**n+(1/2)*s7*x7**n+(1/2)*s16*x16**n) - k*x31
    dx32 = (2*a*s2*x2**n)/(S**n+s2*x2**n)-k*x32
    return [dx1,dx2,dx3,dx4,dx5,dx6,dx7,dx8,dx9,dx10,dx11,dx12,dx13,dx14,dx15,dx16,dx17,dx18,dx19,dx20,dx21,dx22,dx23,dx24,dx25,dx26,dx27,dx28,dx29,dx30,dx31,dx32]

t_step = 1e-2
t = np.arange(0, 20, t_step)

outo = odeint(deriv,xo,t)

#%% Polynomial Dynamic Inversion
## Control C(Cancer) to A(Apoptosis)
x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32 = xo
# create python list to log results
log1 = []
# lamb1 = 0.25999941
# lamb2 = 3.50313917
# lamb1 = 0.5116485
# lamb2 = 0.43259995
lamb1 = 0.5116
lamb2 = 0.4325
# lamb1 = -1.33915846
# lamb2 = -0.12120216
# lamb1 = 0.26661271
# lamb2 = 3.3251774
# lamb1 = 1.51713358
# lamb2 = -3.06105057
error = 0
u_sum_PDI = 0
error_sum_PDI = 0

# Polynomial Dynamic Inversion
for i in range(1,len(t)):
    x = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32]
    #x6d = (2*b*S**n)/(S**n+(1/2)*s17*x17**n+(1/2)*s18*x18**n)-k*x6
    e6 = x6-xeA[5]
    x10d = (a*(s11*x11**n+s12*x12**n+s13*x13**n)/3)/(S**n+(1/3)*s11*x11**n+(1/3)*s12*x12**n+(1/3)*s13*x13**n) + (b*S**n)/(S**n+s4*x4**n) - k*x10
    e10 = x10-xeA[9]
    u = -lamb1*e10 - lamb2*e10**3 - x10d
    error = np.sqrt(np.sum(np.power(np.asarray(x)-np.asarray(xeA),2))/len(xeA))
    log1.append([t[i-1],x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,error,u])
    # span for next time step
    tspan = [t[i-1],t[i]]
    x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32 = odeint(derivCSIMO,x,tspan,args=(u,))[-1]
    u_sum_PDI = u_sum_PDI + abs(u) * t_step
    error_sum_PDI = error_sum_PDI + abs(error) * t_step

#%% Domain control
## Control C(Cancer) to A(Apoptosis)
x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32 = xo
# create python list to log results
log2 = []
# lamb = -0.58277389
# lamb = -0.56886579
lamb = -0.5688
# lamb = -1.37762436
error = 0
u_sum_DI = 0
error_sum_DI = 0

for i in range(1,len(t)):
    x = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32]
    u = -((a*(s11*x11**n+s12*x12**n+s13*x13**n)/3)/(S**n+(1/3)*s11*x11**n+(1/3)*s12*x12**n+(1/3)*s13*x13**n) + (b*S**n)/(S**n+s4*x4**n) - k*x10)+lamb*(x10-xeA[9])
    error = np.sqrt(np.sum(np.power(np.asarray(x)-np.asarray(xeA),2))/len(xeA))
    log2.append([t[i-1],x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,error,u])
    # span for next time step
    tspan = [t[i-1],t[i]]
    x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32 = odeint(derivCSIMO,x,tspan,args=(u,))[-1]
    u_sum_DI = u_sum_DI + abs(u) * t_step
    error_sum_DI = error_sum_DI + abs(error) * t_step
    
       
def qplot(logno, log,log2, t):
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.figure(figsize=(16,8))
    logno = np.asarray(logno).T
    log = np.asarray(log).T
    log2 = np.asarray(log2).T
    ref1 = np.ones(logno[5].shape)*xeA[5]
    ref2 = np.ones(logno[5].shape)*xeA[9]
    refe = np.zeros(logno[5].shape)
    plt.subplot(2,2,1)
    plt.plot(t,ref1,linewidth = 3,color = 'r',linestyle = 'dotted')
    plt.plot(t,logno[5],linewidth = 3,color = 'k',linestyle = 'dotted')
    plt.plot(log[0],log[6],linewidth = 3, color = '#4CAF50')
    plt.plot(log2[0],log2[6],linewidth = 3, color = '#EF6C00',linestyle = 'dashed')
    #plt.title('nutlin input')
    plt.ylabel('$x_6$', fontsize=40)
    plt.xlabel('Time [a.u.]', fontsize=30)
    plt.xticks(np.arange(0, max(log[0])+1, 5), fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid()
    plt.legend(['Apoptosis target','Cancerous (no control)', 'Polynomial dynamic\ninversion', 'Domain control'], fontsize=20, loc='lower right')
    
    plt.subplot(2,2,2)
    plt.plot(t,ref2,linewidth = 3,color = 'r',linestyle = 'dotted')
    plt.plot(t,logno[9],linewidth = 3,color = 'k',linestyle = 'dotted')
    plt.plot(log[0],log[10],linewidth = 3, color = '#4CAF50')
    plt.plot(log2[0],log2[10],linewidth = 3, color = '#EF6C00',linestyle = 'dashed')
    #plt.title('nutlin input')
    plt.ylabel('$x_{10}$', fontsize=40)
    plt.xlabel('Time [a.u.]', fontsize=30)
    plt.xticks(np.arange(0, max(log[0])+1, 5), fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid()
    
    plt.subplot(2,2,3)
    plt.plot(t,refe,linewidth = 3,color = 'r',linestyle = 'dotted')
    plt.plot(log[0],log[-2],linewidth = 3, color = '#4CAF50')
    plt.plot(log2[0],log2[-2],linewidth = 3, color = '#EF6C00',linestyle = 'dashed')
    #plt.title('nutlin input')
    plt.ylabel('$e$', fontsize=40)
    plt.xlabel('Time [a.u.]', fontsize=30)
    plt.xticks(np.arange(0, max(log[0])+1, 5), fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid()
    #plt.yticks(np.arange(0, 2.2, 1))
    #plt.legend(['PDI', 'DI'])
    #plt.ylim([0.01,2.2])
    
    plt.subplot(2,2,4)
    plt.plot(log[0],log[-1],linewidth = 3, color = '#4CAF50')
    plt.plot(log2[0],log2[-1],linestyle = 'dashed',linewidth = 3, color = '#EF6C00')
    #plt.title('nutlin input')
    plt.ylabel('$u_{10}$', fontsize=40)
    plt.xlabel('Time [a.u.]', fontsize=30)
    plt.xticks(np.arange(0, max(log[0])+1, 5), fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid()
    #plt.legend(['PDI: u$_{10}$', 'DI: u$_{10}$'])
    plt.tight_layout()
    
Linewidth_nonL = 3
qplot(outo,log1,log2,t)
plt.show()

print(u_sum_PDI, error_sum_PDI, u_sum_DI, error_sum_DI)
# 2.899043278993609 3.2746594218222476 2.8803181620410525 3.2900573773708164

#%% Settling time
logno = np.asarray(outo).T
log = np.asarray(log1).T
log3 = np.asarray(log2).T

PDI_settling_index = np.argmin(log[-2][log[-2]>5*1e-2])
PDI_settling_time = log[0][PDI_settling_index]
# 12.15

DC_settling_index = np.argmin(log3[-2][log3[-2]>5*1e-2])
DC_settling_time = log3[0][DC_settling_index]
# 12.12
