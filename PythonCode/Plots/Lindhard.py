import numpy as np

import matplotlib.pyplot as plt

Z = 54
A = 131.29

RecoilEnergies = np.linspace(1, 100, 1001)

Epsilon = 11.5 * RecoilEnergies * Z**(-7./3)
k = 0.133 * Z**(2./3) * A**(-0.5)
g = 3 * Epsilon**0.15 + 0.7*Epsilon**0.6 + Epsilon
f = k*g / (1 + k*g)

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.plot(
	RecoilEnergies,
	f,
	linewidth=2
	)

ax.set_xscale('log')
ax.set_xlabel('Nuclear Recoil Energy [keV]', size=17)
ax.set_ylabel(r'$f_{n}$', size=20)
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(15)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(15)
plt.tight_layout()
plt.savefig('/Users/Zach/XENON/Thesis/Chapter2/Figures/Lindhard.png', format='png')
plt.show()
