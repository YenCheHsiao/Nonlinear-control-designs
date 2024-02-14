# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 09:18:11 2023

@author: ych22001
"""

# Perturb one parameters

import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.integrate import odeint
from SALib.sample import saltelli
from SALib.analyze import sobol
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

percent = 0.05
# Define the parameter ranges and their names
problem = {
    'num_vars': 37,  # Number of parameters to analyze
    'names': [r'$S$', r'$n$', r'$a$', r'$b$', r'$k$', 
              r'$s_1$', r'$s_2$', r'$s_3$', r'$s_4$', '$s_5$', 
              r'$s_6$', r'$s_7$', r'$s_8$', r'$s_9$', '$s_{10}$',
              r'$s_{11}$', r'$s_{12}$', r'$s_{13}$', r'$s_{14}$', '$s_{15}$',
              r'$s_{16}$', r'$s_{17}$', r'$s_{18}$', r'$s_{19}$', '$s_{20}$',
              r'$s_{21}$', r'$s_{22}$', r'$s_{23}$', r'$s_{24}$', '$s_{25}$',
              r'$s_{26}$', r'$s_{27}$', r'$s_{28}$', r'$s_{29}$', '$s_{30}$',
              r'$s_{31}$', r'$s_{32}$'],
    'bounds': [[(1-percent)*S, (1+percent)*S], 
               [(1-percent)*n, (1+percent)*n], 
               [(1-percent)*a, (1+percent)*a], 
               [(1-percent)*b, (1+percent)*b], 
               [(1-percent)*k, (1+percent)*k],
               [(1-percent)*s1, (1+percent)*s1],
               [(1-percent)*s2, (1+percent)*s2],
               [(1-percent)*s3, (1+percent)*s3],
               [(1-percent)*s4, (1+percent)*s4],
               [(1-percent)*s5, (1+percent)*s5],
               [(1-percent)*s6, (1+percent)*s6],
               [(1-percent)*s7, (1+percent)*s7],
               [(1-percent)*s8, (1+percent)*s8],
               [(1-percent)*s9, (1+percent)*s9],
               [(1-percent)*s10, (1+percent)*s10],
               [(1-percent)*s11, (1+percent)*s11],
               [(1-percent)*s12, (1+percent)*s12],
               [(1-percent)*s13, (1+percent)*s13],
               [(1-percent)*s14, (1+percent)*s14],
               [(1-percent)*s15, (1+percent)*s15],
               [(1-percent)*s16, (1+percent)*s16],
               [(1-percent)*s17, (1+percent)*s17],
               [(1-percent)*s18, (1+percent)*s18],
               [(1-percent)*s19, (1+percent)*s19],
               [(1-percent)*s20, (1+percent)*s20],
               [(1-percent)*s21, (1+percent)*s21],
               [(1-percent)*s22, (1+percent)*s22],
               [(1-percent)*s23, (1+percent)*s23],
               [(1-percent)*s24, (1+percent)*s24],
               [(1-percent)*s25, (1+percent)*s25],
               [(1-percent)*s26, (1+percent)*s26],
               [(1-percent)*s27, (1+percent)*s27],
               [(1-percent)*s28, (1+percent)*s28],
               [(1-percent)*s29, (1+percent)*s29],
               [(1-percent)*s30, (1+percent)*s30],
               [(1-percent)*s31, (1+percent)*s31],
               [(1-percent)*s32, (1+percent)*s32]
               ],
}

t_step = 1e-1
t = np.arange(0, 20, t_step)
outo = odeint(deriv,xo,t)

# for i in range(32):
#     plt.plot(t,outo.T[i])
# plt.show()

# Define the number of samples for sensitivity analysis
num_samples = 1060 # Adjust as needed
num_iterations = num_samples
# Generate a sample matrix for sensitivity analysis
param_values = saltelli.sample(problem, num_samples, calc_second_order=True)
# If calc_second_order=True
# There are N * (2D + 2) = num_samples * (2 * num_vars + 2) rows
# If calc_second_order=True
# There are N * (D + 2) = num_samples * (num_vars + 2) rows

# Initialize arrays to store the model's output for each parameter combination
# sensitivity_results = np.zeros((param_values.shape[0], len(tspan_sensitivity)-1 ))  # Assuming there are 4 output variables (B, E, Ti, Tu)
sensitivity_results = np.zeros((param_values.shape[0]))

for n, params in enumerate(param_values):
    
    sampled_params = params[:-1]  ## last term is scale

    ## Control C(Cancer) to A(Apoptosis)
    x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32 = xo
    error = 100
    # Perturbed parameters
    dS = params[0]
    dn = params[1]
    da = params[2]
    db = params[3]
    dk = params[4]
    ds1 = params[5]
    ds2 = params[6]
    ds3 = params[7]
    ds4 = params[8]
    ds5 = params[9]
    ds6 = params[10]
    ds7 = params[11]
    ds8 = params[12]
    ds9 = params[13]
    ds10 = params[14]
    ds11 = params[15]
    ds12 = params[16]
    ds13 = params[17]
    ds14 = params[18]
    ds15 = params[19]
    ds16 = params[20]
    ds17 = params[21]
    ds18 = params[22]
    ds19 = params[23]
    ds20 = params[24]
    ds21 = params[25]
    ds22 = params[26]
    ds23 = params[27]
    ds24 = params[28]
    ds25 = params[29]
    ds26 = params[30]
    ds27 = params[31]
    ds28 = params[32]
    ds29 = params[33]
    ds30 = params[34]
    ds31 = params[35]
    ds32 = params[36]
    
    # Find equilibrium
    # teq = np.arange(0, 100, 1e-1)
    # outo = odeint(derivP,xeA,teq,args=(dS,dn,da,db,dk,ds1,ds2,ds3,ds4,ds5,ds6,ds7,ds8,ds9,ds10,ds11,ds12,ds13,ds14,ds15,ds16,ds17,ds18,ds19,ds20,ds21,ds22,ds23,ds24,ds25,ds26,ds27,ds28,ds29,ds30,ds31,ds32,))
    xdP = xeC
    # x = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32]
    # if np.sqrt(np.sum(np.power(np.asarray(x)-np.asarray(xdP),2))/len(xdP)) < 0.4:
    #     itr = itr - 1
    #     continue
  
    for i in range(1,len(t)):
        x = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32]
        u = 0
        error = np.sqrt(np.sum(np.power(np.asarray(x)-np.asarray(xdP),2))/len(xdP))
        # span for next time step
        tspan = [t[i-1],t[i]]
        x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32 = odeint(derivCP,[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32],tspan,args=(u,dS,dn,da,db,dk,ds1,ds2,ds3,ds4,ds5,ds6,ds7,ds8,ds9,ds10,ds11,ds12,ds13,ds14,ds15,ds16,ds17,ds18,ds19,ds20,ds21,ds22,ds23,ds24,ds25,ds26,ds27,ds28,ds29,ds30,ds31,ds32,))[-1]
        # if error < 1e-2:
        #     settle_time = t[i]
        #     break
    if n%10 == 0:
        print(str(n) + "/" + str(param_values.shape[0]))
    
    ss_error = error
    sensitivity_results[n,] = ss_error

np.save('sensitivity_results_1060', np.asarray(sensitivity_results))

Si = sobol.analyze(problem, sensitivity_results, calc_second_order=True, print_to_console=False)

    # Print or visualize the sensitivity indices
for param_name, indices in zip(problem['names'], Si['S1']):
    print(f"First-order Sensitivity of {param_name}: {indices}")
    
for param_name, indices in zip(problem['names'], Si['ST']):
    print(f"Total-order Sensitivity of {param_name}: {indices}")    


#%% Plot Sensitivity divide-1
# Sample data (replace with your Si data)
plt.rc('font', size=40)
parameters = problem['names'][0:6]
first_order_sensitivity = Si['S1'][0:6]
first_order_confidence = Si['S1_conf'][0:6]
total_sensitivity = Si['ST'][0:6]
total_confidence = Si['ST_conf'][0:6]

# Create the first plot with the left y-axis
fig, ax1 = plt.subplots(figsize=(24, 12))

# Bar width for the left y-axis plot
bar_width = 0.4

ax1.set_xlabel('Parameters')
ax1.set_ylabel('First-order Sensitivity Indices', color='tab:blue')  # Use LaTeX notation for alpha symbol

# Create an array of x-coordinates for the first plot
x1 = np.arange(len(parameters))

ax1.bar(x1, first_order_sensitivity, width=bar_width, yerr=first_order_confidence, capsize=10, color='tab:blue', label='First-Order Sensitivity')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Create a second y-axis on the right
ax2 = ax1.twinx()
ax2.set_ylabel('Total Sensitivity Indices', color='tab:red')

# Shift the x-coordinates for the second plot to the right by adding bar_width
x2 = x1 + bar_width

ax2.bar(x2, total_sensitivity, width=bar_width, yerr=total_confidence, capsize=10, color='tab:red', label='Total Sensitivity')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Set x-tick labels to parameter names
plt.xticks(x1 + bar_width / 2, parameters, rotation=45, ha='right')

# Create a legend
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper right')

plt.title('Sensitivity Analysi-1')
plt.tight_layout()
plt.rcParams.update({'font.size': 10})
plt.show()

#%% Plot Sensitivity divide-2
# Sample data (replace with your Si data)
plt.rc('font', size=40)
parameters = problem['names']
first_order_sensitivity = Si['S1']
first_order_confidence = Si['S1_conf']
total_sensitivity = Si['ST']
total_confidence = Si['ST_conf']

# Create the first plot with the left y-axis
fig, ax1 = plt.subplots(figsize=(36, 12))

# Bar width for the left y-axis plot
bar_width = 0.4

ax1.set_xlabel('Parameters')
ax1.set_ylabel('First-order Sensitivity Indices', color='#0173b2')  # Use LaTeX notation for alpha symbol

# Create an array of x-coordinates for the first plot
x1 = np.arange(len(parameters))

ax1.bar(x1, first_order_sensitivity, width=bar_width, yerr=first_order_confidence, capsize=10, color='#0173b2', label='First-Order Sensitivity')
plt.scatter(x1, y=first_order_sensitivity, color='k', s=80)
ax1.tick_params(axis='y', labelcolor='#0173b2')
ax1.set_ylim([-0.03, 0.8])

# Create a second y-axis on the right
ax2 = ax1.twinx()
ax2.set_ylabel('Total Sensitivity Indices', color='#de8f05')

# Shift the x-coordinates for the second plot to the right by adding bar_width
x2 = x1 + bar_width

ax2.bar(x2, total_sensitivity, width=bar_width, yerr=total_confidence, capsize=10, color='#de8f05', label='Total Sensitivity')
plt.scatter(x2, y=total_sensitivity, color='k', s=80)
ax2.tick_params(axis='y', labelcolor='#de8f05')
ax2.set_ylim([-0.03, 0.8])

# Set x-tick labels to parameter names
plt.xticks(x1 + bar_width / 2, parameters, rotation=45, ha='right')

# Create a legend
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper right')

# plt.axhline(y=0,linewidth=5, color='k', alpha = 0.5)
plt.grid()
plt.title('Sensitivity Analysis')
plt.tight_layout()
plt.rcParams.update({'font.size': 10})
plt.show()