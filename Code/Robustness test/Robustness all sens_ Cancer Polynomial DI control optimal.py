# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 11:53:56 2023

@author: xiaoyenche
"""

# Perturb all parameters

import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.integrate import odeint
#import seaborn as sns
#sns.set_context('talk')

random.seed(0)
#random.random()
np.random.seed(0)
#np.random.rand(4)

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

# Nonlinear system
def derivP(X,t,dS,dn,da,db,dk,ds1,ds2,ds3,ds4,ds5,ds6,ds7,ds8,ds9,ds10,ds11,ds12,ds13,ds14,ds15,ds16,ds17,ds18,ds19,ds20,ds21,ds22,ds23,ds24,ds25,ds26,ds27,ds28,ds29,ds30,ds31,ds32):
    x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32 = X
    dx1 = (2*db*dS**dn)/(dS**dn+ds32*x32**dn)-dk*x1
    dx2 = (da*(ds1*x1**dn+ds9*x9**dn+ds14*x14**dn)/3)/(dS**dn+(1/3)*ds1*x1**dn+(1/3)*ds9*x9**dn+(1/3)*ds14*x14**dn) + (2*db*dS**dn)/(2*dS**dn+ds16*x16**dn+ds31*x31**dn) - dk*x2
    dx3 = (da*(ds2*x2**dn+ds8*x8**dn+ds29*x29**dn)/3)/(dS**dn+(1/3)*ds2*x2**dn+(1/3)*ds8*x8**dn+(1/3)*ds29*x29**dn) + (3*db*dS**dn)/(3*dS**dn+ds9*x9**dn+ds10*x10**dn+ds16*x16**dn) - dk*x3
    dx4 = (da*ds2*x2**dn)/(dS**dn+ds2*x2**dn) + (db*dS**dn)/(dS**dn+ds25*x25**dn) - dk*x4
    dx5 = (da*ds13*x13**dn)/(dS**dn+ds13*x13**dn) + (db*dS**dn)/(dS**dn+(1/3)*ds14*x14**dn+(1/3)*ds17*x17**dn+(1/3)*ds19*x19**dn) - dk*x5
    dx6 = (2*db*dS**dn)/(dS**dn+(1/2)*ds17*x17**dn+(1/2)*ds18*x18**dn)-dk*x6
    dx7 = (da*ds20*x20**dn)/(dS**dn+ds20*x20**dn) + (db*dS**dn)/(dS**dn+(1/2)*ds15*x15**dn+(1/2)*ds32*x32**dn) - dk*x7
    dx8 = (2*db*dS**dn)/(dS**dn+(1/3)*ds4*x4**dn+(1/3)*ds10*x10**dn+(1/3)*ds16*x16**dn)-dk*x8
    dx9 = (da*(ds11*x11**dn+ds13*x13**dn+ds25*x25**dn+ds26*x26**dn)/4)/(dS**dn+(1/4)*ds11*x11**dn+(1/4)*ds13*x13**dn+(1/4)*ds25*x25**dn+(1/4)*ds26*x26**dn) + (db*dS**dn)/(dS**dn+ds29*x29**dn) - dk*x9
    dx10 = (da*(ds11*x11**dn+ds12*x12**dn+ds13*x13**dn)/3)/(dS**dn+(1/3)*ds11*x11**dn+(1/3)*ds12*x12**dn+(1/3)*ds13*x13**dn) + (db*dS**dn)/(dS**dn+ds4*x4**dn) - dk*x10
    dx11 = (da*(ds10*x10**dn+ds13*x13**dn+ds14*x14**dn+ds27*x27**dn+ds28*x28**dn))/(5*dS**dn+ds10*x10**dn+ds13*x13**dn+ds14*x14**dn+ds27*x27**dn+ds28*x28**dn) + (db*dS**dn)/(dS**dn+ds29*x29**dn) - dk*x11
    dx12 = (da*(ds9*x9**dn+ds10*x10**dn+ds11*x11**dn+ds13*x13**dn+ds14*x14**dn+ds15*x15**dn))/(6*dS**dn+ds9*x9**dn+ds10*x10**dn+ds11*x11**dn+ds13*x13**dn+ds14*x14**dn+ds15*x15**dn) + (db*dS**dn)/(dS**dn+ds2*x2**dn) - dk*x12
    dx13 = (2*da*(ds12*x12**dn+ds14*x14**dn+ds28*x28**dn)/3)/(dS**dn+(1/3)*ds12*x12**dn+(1/3)*ds14*x14**dn+(1/3)*ds28*x28**dn) - dk*x13
    dx14 = (da*(ds10*x10**dn+ds13*x13**dn+ds25*x25**dn+ds26*x26**dn+ds28*x28**dn))/(5*dS**dn+ds10*x10**dn+ds13*x13**dn+ds25*x25**dn+ds26*x26**dn+ds28*x28**dn) + (db*dS**dn)/(dS**dn+ds2*x2**dn) - dk*x14
    dx15 = (da*ds14*x14**dn)/(dS**dn+ds14*x14**dn) + (db*dS**dn)/(dS**dn+(1/2)*ds2*x2**dn+(1/2)*ds29*x29**dn) - dk*x15
    dx16 = (da*(ds2*x2**dn+ds10*x10**dn+ds26*x26**dn+ds32*x32**dn))/(4*dS**dn+ds2*x2**dn+ds10*x10**dn+ds26*x26**dn+ds32*x32**dn) + (3*db*dS**dn)/(3*dS**dn+ds1*x1**dn+ds6*x6**dn+ds7*x7**dn) - dk*x16
    dx17 = (da*(ds9*x9**dn+ds10*x10**dn+ds20*x20**dn))/(3*dS**dn+ds9*x9**dn+ds10*x10**dn+ds20*x20**dn) + (2*db*dS**dn)/(2*dS**dn+ds3*x3**dn+ds6*x6**dn) - dk*x17
    dx18 = (da*(ds9*x9**dn+ds25*x25**dn+ds26*x26**dn)/3)/(dS**dn+(1/3)*ds9*x9**dn+(1/3)*ds25*x25**dn+(1/3)*ds26*x26**dn) + (db*dS**dn)/(dS**dn+ds6*x6**dn) - dk*x18
    dx19 = (2*db*dS**dn)/(dS**dn+(1/3)*ds3*x3**dn+(1/3)*ds5*x5**dn+(1/3)*ds30*x30**dn)-dk*x19
    dx20 = (da*ds1*x1**dn)/(dS**dn+ds1*x1**dn) + (db*dS**dn)/(dS**dn+(1/2)*ds6*x6**dn+(1/2)*ds17*x17**dn) - dk*x20
    dx21 = (da*(ds22*x22**dn+ds23*x23**dn)/2)/(dS**dn+(1/2)*ds22*x22**dn+(1/2)*ds23*x23**dn) + (db*dS**dn)/(dS**dn+(1/2)*ds10*x10**dn+(1/2)*ds24*x24**dn) - dk*x21
    dx22 = (da*(ds2*x2**dn+ds9*x9**dn)/2)/(dS**dn+(1/2)*ds2*x2**dn+(1/2)*ds9*x9**dn) + (db*dS**dn)/(dS**dn+ds24*x24**dn) - dk*x22
    dx23 = (2*db*dS**dn)/(dS**dn+ds10*x10**dn)-dk*x23
    dx24 = (da*(ds12*x12**dn+ds13*x13**dn+ds25*x25**dn)/3)/(dS**dn+(1/3)*ds12*x12**dn+(1/3)*ds13*x13**dn+(1/3)*ds25*x25**dn) + (db*dS**dn)/(dS**dn+(1/2)*ds2*x2**dn+(1/2)*ds21*x21**dn) - dk*x24
    dx25 = (da*(ds10*x10**dn+ds13*x13**dn)/2)/(dS**dn+(1/2)*ds10*x10**dn+(1/2)*ds13*x13**dn) + (db*dS**dn)/(dS**dn+ds4*x4**dn) - dk*x25
    dx26 = (2*da*(ds11*x11**dn+ds12*x12**dn+ds27*x27**dn)/3)/(dS**dn+(1/3)*ds11*x11**dn+(1/3)*ds12*x12**dn+(1/3)*ds27*x27**dn) - dk*x26
    dx27 = (2*da*ds28*x28**dn)/(dS**dn+ds28*x28**dn)-dk*x27
    dx28 = -dk*x28
    dx29 = (2*da*ds14*x14**dn)/(dS**dn+ds14*x14**dn)-dk*x29
    dx30 = (2*da*ds19*x19**dn)/(dS**dn+ds19*x19**dn)-dk*x30
    dx31 = (da*(ds10*x10**dn+ds32*x32**dn)/2)/(dS**dn+(1/2)*ds10*x10**dn+(1/2)*ds32*x32**dn) + (db*dS**dn)/(dS**dn+(1/2)*ds7*x7**dn+(1/2)*ds16*x16**dn) - dk*x31
    dx32 = (2*da*ds2*x2**dn)/(dS**dn+ds2*x2**dn)-dk*x32
    return [dx1,dx2,dx3,dx4,dx5,dx6,dx7,dx8,dx9,dx10,dx11,dx12,dx13,dx14,dx15,dx16,dx17,dx18,dx19,dx20,dx21,dx22,dx23,dx24,dx25,dx26,dx27,dx28,dx29,dx30,dx31,dx32]

# Controlled nonlinear system
def derivC(X,t,u):
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

# Nonlinear system
def derivCP(X,t,u,dS,dn,da,db,dk,ds1,ds2,ds3,ds4,ds5,ds6,ds7,ds8,ds9,ds10,ds11,ds12,ds13,ds14,ds15,ds16,ds17,ds18,ds19,ds20,ds21,ds22,ds23,ds24,ds25,ds26,ds27,ds28,ds29,ds30,ds31,ds32):
    x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32 = X
    dx1 = (2*db*dS**dn)/(dS**dn+ds32*x32**dn)-dk*x1
    dx2 = (da*(ds1*x1**dn+ds9*x9**dn+ds14*x14**dn)/3)/(dS**dn+(1/3)*ds1*x1**dn+(1/3)*ds9*x9**dn+(1/3)*ds14*x14**dn) + (2*db*dS**dn)/(2*dS**dn+ds16*x16**dn+ds31*x31**dn) - dk*x2
    dx3 = (da*(ds2*x2**dn+ds8*x8**dn+ds29*x29**dn)/3)/(dS**dn+(1/3)*ds2*x2**dn+(1/3)*ds8*x8**dn+(1/3)*ds29*x29**dn) + (3*db*dS**dn)/(3*dS**dn+ds9*x9**dn+ds10*x10**dn+ds16*x16**dn) - dk*x3
    dx4 = (da*ds2*x2**dn)/(dS**dn+ds2*x2**dn) + (db*dS**dn)/(dS**dn+ds25*x25**dn) - dk*x4
    dx5 = (da*ds13*x13**dn)/(dS**dn+ds13*x13**dn) + (db*dS**dn)/(dS**dn+(1/3)*ds14*x14**dn+(1/3)*ds17*x17**dn+(1/3)*ds19*x19**dn) - dk*x5
    dx6 = (2*db*dS**dn)/(dS**dn+(1/2)*ds17*x17**dn+(1/2)*ds18*x18**dn)-dk*x6
    dx7 = (da*ds20*x20**dn)/(dS**dn+ds20*x20**dn) + (db*dS**dn)/(dS**dn+(1/2)*ds15*x15**dn+(1/2)*ds32*x32**dn) - dk*x7
    dx8 = (2*db*dS**dn)/(dS**dn+(1/3)*ds4*x4**dn+(1/3)*ds10*x10**dn+(1/3)*ds16*x16**dn)-dk*x8
    dx9 = (da*(ds11*x11**dn+ds13*x13**dn+ds25*x25**dn+ds26*x26**dn)/4)/(dS**dn+(1/4)*ds11*x11**dn+(1/4)*ds13*x13**dn+(1/4)*ds25*x25**dn+(1/4)*ds26*x26**dn) + (db*dS**dn)/(dS**dn+ds29*x29**dn) - dk*x9
    dx10 = (da*(ds11*x11**dn+ds12*x12**dn+ds13*x13**dn)/3)/(dS**dn+(1/3)*ds11*x11**dn+(1/3)*ds12*x12**dn+(1/3)*ds13*x13**dn) + (db*dS**dn)/(dS**dn+ds4*x4**dn) - dk*x10 + u
    dx11 = (da*(ds10*x10**dn+ds13*x13**dn+ds14*x14**dn+ds27*x27**dn+ds28*x28**dn))/(5*dS**dn+ds10*x10**dn+ds13*x13**dn+ds14*x14**dn+ds27*x27**dn+ds28*x28**dn) + (db*dS**dn)/(dS**dn+ds29*x29**dn) - dk*x11
    dx12 = (da*(ds9*x9**dn+ds10*x10**dn+ds11*x11**dn+ds13*x13**dn+ds14*x14**dn+ds15*x15**dn))/(6*dS**dn+ds9*x9**dn+ds10*x10**dn+ds11*x11**dn+ds13*x13**dn+ds14*x14**dn+ds15*x15**dn) + (db*dS**dn)/(dS**dn+ds2*x2**dn) - dk*x12
    dx13 = (2*da*(ds12*x12**dn+ds14*x14**dn+ds28*x28**dn)/3)/(dS**dn+(1/3)*ds12*x12**dn+(1/3)*ds14*x14**dn+(1/3)*ds28*x28**dn) - dk*x13
    dx14 = (da*(ds10*x10**dn+ds13*x13**dn+ds25*x25**dn+ds26*x26**dn+ds28*x28**dn))/(5*dS**dn+ds10*x10**dn+ds13*x13**dn+ds25*x25**dn+ds26*x26**dn+ds28*x28**dn) + (db*dS**dn)/(dS**dn+ds2*x2**dn) - dk*x14
    dx15 = (da*ds14*x14**dn)/(dS**dn+ds14*x14**dn) + (db*dS**dn)/(dS**dn+(1/2)*ds2*x2**dn+(1/2)*ds29*x29**dn) - dk*x15
    dx16 = (da*(ds2*x2**dn+ds10*x10**dn+ds26*x26**dn+ds32*x32**dn))/(4*dS**dn+ds2*x2**dn+ds10*x10**dn+ds26*x26**dn+ds32*x32**dn) + (3*db*dS**dn)/(3*dS**dn+ds1*x1**dn+ds6*x6**dn+ds7*x7**dn) - dk*x16
    dx17 = (da*(ds9*x9**dn+ds10*x10**dn+ds20*x20**dn))/(3*dS**dn+ds9*x9**dn+ds10*x10**dn+ds20*x20**dn) + (2*db*dS**dn)/(2*dS**dn+ds3*x3**dn+ds6*x6**dn) - dk*x17
    dx18 = (da*(ds9*x9**dn+ds25*x25**dn+ds26*x26**dn)/3)/(dS**dn+(1/3)*ds9*x9**dn+(1/3)*ds25*x25**dn+(1/3)*ds26*x26**dn) + (db*dS**dn)/(dS**dn+ds6*x6**dn) - dk*x18
    dx19 = (2*db*dS**dn)/(dS**dn+(1/3)*ds3*x3**dn+(1/3)*ds5*x5**dn+(1/3)*ds30*x30**dn)-dk*x19
    dx20 = (da*ds1*x1**dn)/(dS**dn+ds1*x1**dn) + (db*dS**dn)/(dS**dn+(1/2)*ds6*x6**dn+(1/2)*ds17*x17**dn) - dk*x20
    dx21 = (da*(ds22*x22**dn+ds23*x23**dn)/2)/(dS**dn+(1/2)*ds22*x22**dn+(1/2)*ds23*x23**dn) + (db*dS**dn)/(dS**dn+(1/2)*ds10*x10**dn+(1/2)*ds24*x24**dn) - dk*x21
    dx22 = (da*(ds2*x2**dn+ds9*x9**dn)/2)/(dS**dn+(1/2)*ds2*x2**dn+(1/2)*ds9*x9**dn) + (db*dS**dn)/(dS**dn+ds24*x24**dn) - dk*x22
    dx23 = (2*db*dS**dn)/(dS**dn+ds10*x10**dn)-dk*x23
    dx24 = (da*(ds12*x12**dn+ds13*x13**dn+ds25*x25**dn)/3)/(dS**dn+(1/3)*ds12*x12**dn+(1/3)*ds13*x13**dn+(1/3)*ds25*x25**dn) + (db*dS**dn)/(dS**dn+(1/2)*ds2*x2**dn+(1/2)*ds21*x21**dn) - dk*x24
    dx25 = (da*(ds10*x10**dn+ds13*x13**dn)/2)/(dS**dn+(1/2)*ds10*x10**dn+(1/2)*ds13*x13**dn) + (db*dS**dn)/(dS**dn+ds4*x4**dn) - dk*x25
    dx26 = (2*da*(ds11*x11**dn+ds12*x12**dn+ds27*x27**dn)/3)/(dS**dn+(1/3)*ds11*x11**dn+(1/3)*ds12*x12**dn+(1/3)*ds27*x27**dn) - dk*x26
    dx27 = (2*da*ds28*x28**dn)/(dS**dn+ds28*x28**dn)-dk*x27
    dx28 = -dk*x28
    dx29 = (2*da*ds14*x14**dn)/(dS**dn+ds14*x14**dn)-dk*x29
    dx30 = (2*da*ds19*x19**dn)/(dS**dn+ds19*x19**dn)-dk*x30
    dx31 = (da*(ds10*x10**dn+ds32*x32**dn)/2)/(dS**dn+(1/2)*ds10*x10**dn+(1/2)*ds32*x32**dn) + (db*dS**dn)/(dS**dn+(1/2)*ds7*x7**dn+(1/2)*ds16*x16**dn) - dk*x31
    dx32 = (2*da*ds2*x2**dn)/(dS**dn+ds2*x2**dn)-dk*x32
    return [dx1,dx2,dx3,dx4,dx5,dx6,dx7,dx8,dx9,dx10,dx11,dx12,dx13,dx14,dx15,dx16,dx17,dx18,dx19,dx20,dx21,dx22,dx23,dx24,dx25,dx26,dx27,dx28,dx29,dx30,dx31,dx32]

t = np.arange(0, 20, 1e-2)

#outo = odeint(deriv,xo,t)
plt.rcParams["xtick.labelsize"] = 20
plt.rcParams["ytick.labelsize"] = 20
plt.rcParams['mathtext.fontset'] = 'cm'
fig = plt.figure(figsize=(16,4))
fax1 = fig.add_subplot(1, 2, 1)
fax1.set_xlabel('Time', fontsize=30)
fax1.set_ylabel('$u_{10}$', fontsize=40)
fax2 = fig.add_subplot(1, 2, 2)
fax2.set_xlabel('Time', fontsize=30)
fax2.set_ylabel('$e$', fontsize=40)
#ax1 = fig.add_axes([0.25, 0.25, 0.2, 0.5])
#ax2 = fig.add_axes([0.68, 0.3, 0.2, 0.5])

def qplot(log, t):
    log = np.asarray(log).T    
    fax1.plot(log[0],log[-1],'k')
    #ax1.plot(log[0][log[0]<=6],log[-1][log[0]<=6],'k')    
    fax2.plot(log[0],log[-2],'k') 
    #ax2.plot(log[0][log[0]<=6],log[-2][log[0]<=6],'k')
    
all_param = np.load('PID_Imp_sens_robust_model_param.npy')

dSV = all_param.T[0]
dnV = all_param.T[1]
daV = all_param.T[2]
dbV = all_param.T[3]
dkV = all_param.T[4]
ds1V = all_param.T[5]
ds2V = all_param.T[6]
ds3V = all_param.T[7]
ds4V = all_param.T[8]
ds5V = all_param.T[9]
ds6V = all_param.T[10]
ds7V = all_param.T[11]
ds8V = all_param.T[12]
ds9V = all_param.T[13]
ds10V = all_param.T[14]
ds11V = all_param.T[15]
ds12V = all_param.T[16]
ds13V = all_param.T[17]
ds14V = all_param.T[18]
ds15V = all_param.T[19]
ds16V = all_param.T[20]
ds17V = all_param.T[21]
ds18V = all_param.T[22]
ds19V = all_param.T[23]
ds20V = all_param.T[24]
ds21V = all_param.T[25]
ds22V = all_param.T[26]
ds23V = all_param.T[27]
ds24V = all_param.T[28]
ds25V = all_param.T[29]
ds26V = all_param.T[30]
ds27V = all_param.T[31]
ds28V = all_param.T[32]
ds29V = all_param.T[33]
ds30V = all_param.T[34]
ds31V = all_param.T[35]
ds32V = all_param.T[36]

# Control parameter
# lamb1 = -0.5116485
# lamb2 = -0.43259995
lamb1 = -0.5116
lamb2 = -0.4325

param_index = 0
Converge_count = 0
all_log = []
for itr in range(0, 1060):# run 1060 times
    ## Control C(Cancer) to A(Apoptosis)
    x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32 = xo
    # create python list to log results
    log = []
    error = 0
    # Perturbed parameters
    dS = dSV[param_index]
    dn = dnV[param_index]
    da = daV[param_index]
    db = dbV[param_index]
    dk = dkV[param_index]
    ds1 = ds1V[param_index]
    ds2 = ds2V[param_index]
    ds3 = ds3V[param_index]
    ds4 = ds4V[param_index]
    ds5 = ds5V[param_index]
    ds6 = ds6V[param_index]
    ds7 = ds7V[param_index]
    ds8 = ds8V[param_index]
    ds9 = ds9V[param_index]
    ds10 = ds10V[param_index]
    ds11 = ds11V[param_index]
    ds12 = ds12V[param_index]
    ds13 = ds13V[param_index]
    ds14 = ds14V[param_index]
    ds15 = ds15V[param_index]
    ds16 = ds16V[param_index]
    ds17 = ds17V[param_index]
    ds18 = ds18V[param_index]
    ds19 = ds19V[param_index]
    ds20 = ds20V[param_index]
    ds21 = ds21V[param_index]
    ds22 = ds22V[param_index]
    ds23 = ds23V[param_index]
    ds24 = ds24V[param_index]
    ds25 = ds25V[param_index]
    ds26 = ds26V[param_index]
    ds27 = ds27V[param_index]
    ds28 = ds28V[param_index]
    ds29 = ds29V[param_index]
    ds30 = ds30V[param_index]
    ds31 = ds31V[param_index]
    ds32 = ds32V[param_index]
    
    param_index = param_index + 1
    
    # dS = S
    # dn = n
    # da = a
    # db = b
    # dk = k
    # ds1 = s1
    # ds2 = s2
    # ds3 = s3
    # ds4 = s4
    # ds5 = s5
    # ds6 = s6
    # ds7 = s7
    # ds8 = s8
    # ds9 = s9
    # ds10 = s10
    # ds11 = s11
    # ds12 = s12
    # ds13 = s13
    # ds14 = s14
    # ds15 = s15
    # ds16 = s16
    # ds17 = s17
    # ds18 = s18
    # ds19 = s19
    # ds20 = s20
    # ds21 = s21
    # ds22 = s22
    # ds23 = s23
    # ds24 = s24
    # ds25 = s25
    # ds26 = s26
    # ds27 = s27
    # ds28 = s28
    # ds29 = s29
    # ds30 = s30
    # ds31 = s31
    # ds32 = s32
    
    # Find equilibrium
    # teq = np.arange(0, 100, 1e-1)
    # outo = odeint(derivP,xeA,teq,args=(dS,dn,da,db,dk,ds1,ds2,ds3,ds4,ds5,ds6,ds7,ds8,ds9,ds10,ds11,ds12,ds13,ds14,ds15,ds16,ds17,ds18,ds19,ds20,ds21,ds22,ds23,ds24,ds25,ds26,ds27,ds28,ds29,ds30,ds31,ds32,))
    xdP = xeA
    # x = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32]
    # if np.sqrt(np.sum(np.power(np.asarray(x)-np.asarray(xdP),2))/len(xdP)) < 0.4:
    #     itr = itr - 1
    #     continue
  
    for i in range(1,len(t)):
        x = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32]
        #u = lamb/(1+np.exp(-((x4-xdP[3])**2+(x18-xdP[17])**2)))*(x18-xdP[17])-(Kij*x3+Kij*x15-d18*x18)
        x10d = (a*(s11*x11**n+s12*x12**n+s13*x13**n)/3)/(S**n+(1/3)*s11*x11**n+(1/3)*s12*x12**n+(1/3)*s13*x13**n) + (b*S**n)/(S**n+s4*x4**n) - k*x10
        e10 = x10-xdP[9]
        u = lamb1*e10 + lamb2*e10**3 - x10d
        if u > 0:
            u = 0
        error = np.sqrt(np.sum(np.power(np.asarray(x)-np.asarray(xdP),2))/len(xdP))
        log.append([t[i-1],x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,error,u])
        # span for next time step
        tspan = [t[i-1],t[i]]
        x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32 = odeint(derivCP,[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32],tspan,args=(u,dS,dn,da,db,dk,ds1,ds2,ds3,ds4,ds5,ds6,ds7,ds8,ds9,ds10,ds11,ds12,ds13,ds14,ds15,ds16,ds17,ds18,ds19,ds20,ds21,ds22,ds23,ds24,ds25,ds26,ds27,ds28,ds29,ds30,ds31,ds32,))[-1]
    if error < 1e-1:
        Converge_count = Converge_count + 1
    if itr%5 == 0:
        print(itr)
    
    # qplot(log,t)
    all_log.append(log)

print('number of converge trajectories = ' + str(Converge_count))

# Plot nominal case
## Control A to B
x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32 = xo
# create python list to log results
log = []
for i in range(1,len(t)):
    x = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32]
    x10d = (a*(s11*x11**n+s12*x12**n+s13*x13**n)/3)/(S**n+(1/3)*s11*x11**n+(1/3)*s12*x12**n+(1/3)*s13*x13**n) + (b*S**n)/(S**n+s4*x4**n) - k*x10
    e10 = x10-xeA[9]
    u = lamb1*e10 + lamb2*e10**3 - x10d
    error = np.sqrt(np.sum(np.power(np.asarray(x)-np.asarray(xeA),2))/len(xeA))
    log.append([t[i-1],x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,error,u])
    # span for next time step
    tspan = [t[i-1],t[i]]
    x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32 = odeint(derivC,[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32],tspan,args=(u,))[-1]
       
log = np.asarray(log).T    
# fax1.plot(log[0],log[-1],'r',linewidth=3)  
# fax2.plot(log[0],log[-2],'r',linewidth=3)

# plt.show()

plt.rcParams["xtick.labelsize"] = 20
plt.rcParams["ytick.labelsize"] = 20
plt.rcParams['mathtext.fontset'] = 'cm'
fig = plt.figure(figsize=(16,4))
fax1 = fig.add_subplot(1, 2, 1)
fax1.set_xlabel('Time [a.u.]', fontsize=30)
fax1.set_ylabel('${u_{10}}_{sat}$', fontsize=40)
fax2 = fig.add_subplot(1, 2, 2)
fax2.set_xlabel('Time [a.u.]', fontsize=30)
fax2.set_ylabel('$e$', fontsize=40)

# Plot every simulation
fax1.plot(log[0],np.asarray(all_log).T[-1],'tab:gray', alpha = 0.1)
fax2.plot(log[0],np.asarray(all_log).T[-2],'tab:gray', alpha = 0.1) 

fax1.plot(log[0],log[-1],'r',linewidth=2)  
fax2.plot(log[0],log[-2],'r',linewidth=2)

fax1.plot(log[0],np.max(np.asarray(all_log).T[-1], axis=1),'b',linewidth=2,linestyle='dashed')
fax1.plot(log[0],np.min(np.asarray(all_log).T[-1], axis=1),'b',linewidth=2,linestyle='dashed')
fax2.plot(log[0],np.max(np.asarray(all_log).T[-2], axis=1),'b',linewidth=2,linestyle='dashed')
fax2.plot(log[0],np.min(np.asarray(all_log).T[-2], axis=1),'b',linewidth=2,linestyle='dashed')

fax1.grid()
fax2.grid()
plt.show()

np.save('PDI_sens_robust_trjs', np.asarray(all_log))