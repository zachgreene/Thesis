import numpy as np
import pandas as pd

import matplotlib
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True
matplotlib.rcParams['axes.linewidth'] = 2.
import matplotlib.pyplot as plt

pathToData = '/Users/Zach/XENON/Thesis/Chapter2/data/'
pathToFigures = '/Users/Zach/XENON/Thesis/Chapter2/Figures/'
erFile = 'data_Rn220_SR1_6.8.0_cs1_0_200PE_v6.csv'
nrFile = 'data_AmBe_SR1_6.8.0_cs1_0_200PE_v6.csv'

radialCut = 36.94
zMinCut = -92.9
zMaxCut = -9.
erToKeep = 3000
figScale = 2


df_er = pd.read_csv(pathToData + erFile)
df_nr = pd.read_csv(pathToData + nrFile)

df_er['r'] = (df_er['x']**2 + df_er['y']**2)**0.5
df_nr['r'] = (df_nr['x']**2 + df_nr['y']**2)**0.5

df_er = df_er[df_er.r < radialCut]
df_nr = df_nr[df_nr.r < radialCut]


df_er = df_er[(df_er.z > zMinCut) & (df_er.z < zMaxCut)]
df_nr = df_nr[(df_nr.z > zMinCut) & (df_nr.z < zMaxCut)]

df_er = df_er[:erToKeep]

fig, ax = plt.subplots(1, 1, figsize=(figScale*10, figScale*5))

ax.scatter(
	df_er.cs1,
	df_er.cs2_bottom,
	color='r',
	linewidth=0,
	s=figScale*5,
	label='Electronic Recoils'
)

ax.scatter(
	df_nr.cs1,
	df_nr.cs2_bottom,
	color='b',
	linewidth=0,
	s=figScale*5,
	label='Nuclear Recoils'
)

ax.text(
	70,
	200,
	'Electronic Recoils',
	color='r',
	size=figScale*16
)

ax.text(
	70,
	140,
	'Nuclear Recoils',
	color='b',
	size=figScale*16
)

	

ax.set_xlim([0, 100])
ax.set_ylim([100, 1e4])
ax.set_xlabel('\\rm{S1\ [pe]}', fontsize=figScale*15)
ax.set_ylabel('\\rm{S2\ [pe]}', fontsize=figScale*15)
ax.tick_params(axis='x', length=figScale*4, width=figScale*1, which='both', labelsize=figScale*15)
ax.tick_params(axis='y', length=figScale*4, width=figScale*1, which='both', labelsize=figScale*15)

#ax.set_xticks(ax.get_xticks()[1:-1])
#ax.xaxis.get_major_ticks()[0].set_visible(False)
#ax.yaxis.get_major_ticks()[0].set_visible(False)
#ax.xaxis.get_major_ticks()[-1].set_visible(False)
#ax.yaxis.get_major_ticks()[-1].set_visible(False)

ax.set_yscale('log')

plt.savefig(pathToFigures + 'ERNRComparison.png', format='png')
plt.show()
