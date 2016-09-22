"""Make IACT DL3 example plot.
"""
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
plt.style.use('ggplot')

import astropy.units as u
from gammapy.data import DataStore

def peek_plots(obs):
    fig = obs.aeff.peek()
    fig.savefig('iact-dl3-aeff.png')

    fig = obs.edisp.peek()
    fig.savefig('iact-dl3-edisp.png')

    fig = obs.psf.peek()
    fig.savefig('iact-dl3-psf.png')

def proceeding_plot(obs):
    # import IPython; IPython.embed()
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

    obs.aeff.plot_energy_dependence(ax=axes[0])

    edisp = obs.edisp.to_energy_dispersion(offset='1 deg')
    edisp.plot_matrix(ax=axes[1])

    psf_edep = obs.psf.to_table_psf(theta='1 deg')
    for energy in [1, 3, 10] * u.TeV:
        psf = psf_edep.table_psf_at_energy(energy)
        psf.plot_psf_vs_theta()

    fig.tight_layout()

    filename = 'iact-dl3.png'
    print('Writing ', filename)
    fig.savefig(filename)


if __name__ == '__main__':
    data_store = DataStore.from_dir('$HOME/code/HESS-DL3-DR1/release_store/')
    obs = data_store.obs(obs_id=23592)

    proceeding_plot(obs)
