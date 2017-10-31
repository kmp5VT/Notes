import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

width = .35 # width of a bar

m1_t = pd.DataFrame({
 'H2O' : [61.45210672, 77.7227001, 88.6280799],
 'CH4' : [72.25281499, 82.77307471, 90.89340018],
 'C2H4' : [75.62585344, 86.68639053, 93.17250797],
 'MP2_H2O' : [0.033826163, -0.170727316, 4.551016472],
 'MP2_CH4' : [0.009890113, 0.576737263, 1.33415142],
 'MP2_C2H4': [0.031067971, -0.59997931, -2.510142603]})

m1_t[['H2O','CH4','C2H4']].plot(kind='bar', width = width)
#m1_t['MP2_H2O'].plot(secondary_y=False)
#m1_t['MP2_CH4'].plot(secondary_y=False)
#m1_t['MP2_C2H4'].plot(secondary_y=False)

ax = plt.gca()
#plt.xlim([-width])#, len(m1_t['MP2_H2O'])-width])
ax.set_xticklabels(('1.00E-02', '1.00E-01', '1.00E+00'))
plt.show()
