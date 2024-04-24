# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mCcZ9nq89HSZxHyTDGZMxcRFFhdbW3uB
"""

import matplotlib.pyplot as plt
import numpy as np

#for 850nm
f1=0.025
M1=(f1/((3*10**5)*850))

#for 1300nm
f2=0.004
M2=(f2/((3*10**5)*1300))

#delta=[10,20,30,40,50,60,70,80,90,100]
#for i in range(10,100,10)

sig_lam=np.arange(10,100,10)
sig_m1=sig_lam*M1

sig_lam1=np.arange(10,100,10)
sig_m2=sig_lam1*M2

plt.title("RMS PULSE BROADNING")
plt.xlabel("Sigma Lambda")
plt.ylabel("RMS")
plt.plot(sig_lam,sig_m1,color="r",label="850nm")
plt.plot(sig_lam1,sig_m2,color="g",label="1300nm")
plt.legend()
plt.show()