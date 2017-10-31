import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

h2o_mp2_error_data = [0.033826163, -0.170727316, 4.551016472]
h2o_basis_compression = [61.45210672, 77.7227001, 88.6280799]

names = ["Tcp = 1e-2", "Tcp = 1e-1", "Tcp=1"]
#values = h2o_mp2_error_data

plt.subplot(132)
plt.plot(h2o_mp2_error_data)
#plt.bar(names, h2o_mp2_error_data)
plt.suptitle('Categorical Plotting')
plt.show()
