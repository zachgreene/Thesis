import numpy as np
import pandas as pd
import matplotlib as plt
from matplotlib import gridspec

pathToData = '/Users/Zach/XENON/Thesis/Chapter1/data/COM_PowerSpect_CMB_R1.10.txt'
pathToFig = '/Users/Zach/XENON/Thesis/Chapter1/Figures/'
saveName = 'cmb_power_spectrum.pdf'

data1 = pd.read_csv(
	sep=', ',
	pathToData,
	header=7,
	skipfooter=83,
)

data2 = pd.read_csv(
	pathToData,
	sep=', ',
	header=63,
)
data2['ERRUP'] = data2['ERR']
data2['ERRDOWN'] = data2['ERR']

data = pd.concat([data1, data2], ignore_index=True)

gs1 = gridspec.GridSpec(3,1)
ax = plt.subplot(gs1[:2, :])
ax2 = plt.subplot(gs1[2:, :], sharex=ax)

# plot
ax.errorbar(data.ELL, data.D_ELL, yerr=[data.ERRDOWN, data.ERRUP], fmt='.', color='b')


# residuals


gs1.update(hspace=0)
#plt.savefig(pathToFig + saveName, fmt=saveName.split('.')[-1])
plt.show()
