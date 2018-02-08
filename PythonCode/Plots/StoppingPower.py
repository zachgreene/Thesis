import numpy as np
import pandas as pd

import matplotlib
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True
import matplotlib.pyplot as plt

PathToData = '/Users/Zach/XENON/Thesis/Chapter2/data/'
Alphas = pd.read_csv(PathToData + 'AlphaMassStoppingPower.csv', delimiter=' ', header=3)
Electrons = pd.read_csv(PathToData + 'ElectronMassStoppingPower.csv', delimiter=' ', header=3)
Protons = pd.read_csv(PathToData + 'ProtonMassStoppingPower.csv', delimiter=' ', header=3)

PlotColors = {
		'alpha': 'b',
		'electron': 'g',
		'proton': 'fuchsia'
	}

fig, ax = plt.subplots(1, 1, figsize=(8, 6))

ax.plot(
	Alphas.KineticEnergy,
	Alphas.ElectronStopPow,
	linewidth=2,
#	linestyle='-.',
#	label='$\\alpha$',
	color=PlotColors['alpha']
)


ax.plot(
	Electrons.KineticEnergy,
	Electrons.ElectronStopPow,
	linewidth=2,
	linestyle='dashed',
#	label='$e^{-}$'
	color=PlotColors['electron']
)

ax.plot(
	Protons.KineticEnergy,
	Protons.ElectronStopPow,
	linewidth=2,
	linestyle='-.',
	dashes=(10,3),
#	label='$\\rm{p}$'
	color=PlotColors['proton']
)

ax.text(
	1e-2,
	50,
	r'$\boldsymbol{\alpha}$',
	color=PlotColors['alpha'],
	size='18'
)

ax.text(
	6e-2,
	4,
#	r'$\textbf{e^{-1}}$',
	r'$e^{-1}$',
	color=PlotColors['electron'],
	size='16'
)

ax.text(
	6,
	15,
	'p',
	color=PlotColors['proton'],
	size='14'
)

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim([1e-3, 1e2])
ax.xaxis.set_tick_params(labelsize=15)
ax.yaxis.set_tick_params(labelsize=15)
ax.set_xlabel('Energy [MeV]', fontsize=15)
ax.set_ylabel('Electron Mass Stopping Power [MeV cm$^{2}$ g$^{-1}$]', fontsize=15)
#ax.legend()
plt.savefig('/Users/Zach/XENON/Thesis/Chapter2/Figures/MassStoppingPower.png', format='png')
plt.show()
