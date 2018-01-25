import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


df = pd.read_csv('/Users/Zach/XENON/Thesis/Chapter2/data/PhotonCrossSection.csv', delimiter=' ')

columnsToPlot= [
		'CoherentScat',
		'IncoherScatt',
		'PhotoelAbsorb',
		'NuclearPr',
		'ElectronPrd',
		'TotwCoherent',
		'TotwoCoherent'
		]

#colorsToPlot = {
#		'CoherentScat': ,
#		'IncoherScatt': ,
#		'PhotoelAbsorb': ,
#		'NuclearPr': ,
#		'ElectronPrd': ,
#		'TotwCoherent': ,
#		'TotwoCoherent'
#		}

fig, ax = plt.subplots(1, 1, figsize=(16, 12))

ax.plot(
	df.PhotonEnergy,
	df.PhotoelAbsorb,
	color='r',
	linewidth=3,
	linestyle='dashed',
	label='Photoelectric Absorption'
)

ax.plot(
	df.PhotonEnergy,
	df.IncoherScatt,
	color='g',
	linewidth=3,
	linestyle='dashed',
	dashes=(10, 4),
	label='Compton Scattering'
)

ax.plot(
	df.PhotonEnergy,
	df.ElectronPrd + df.NuclearPr,
#	color='fuchsia',
	color='b',
	linewidth=3,
	linestyle='dashed',
	dashes=(4, 3),
	label='Pair Production'
)


ax.plot(
	df.PhotonEnergy,
	df.TotwCoherent,
	color='k',
	linewidth=3,
	label='Total'
)

ax.set_xlim([1e-3, 1e4])
ax.set_ylim([1e-5, 1e4])
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Photon Energy [MeV]', size=25)
#ax.set_ylabel('$\\rm{Mass\ Attenution\ Coefficiency\ [cm^{2}\ g^{-1}}$]', size=15)
ax.set_ylabel('Mass Attenution Coefficiency [cm$^{2}$ g$^{-1}$]', size=25)
ax.legend(fontsize=25)
plt.savefig('/Users/Zach/XENON/Thesis/Chapter2/Figures/PhotonAttenuation.png', format='png')
plt.show()
