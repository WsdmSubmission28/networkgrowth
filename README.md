![alt tag](https://raw.githubusercontent.com/WsdmSubmission28/networkgrowth/master/content/viz_oc.png  =250x)

# Raising graphs from randomness - revealing information networks

This repo is the collection of the codes used in the experiments of [Raising graphs from randomness - revealing information networks](https://drive.google.com/open?id=0B_3Dz2J_fhmTYXg5MlViOFpmemM).

## Datasets

Datasets can be found [here](https://drive.google.com/drive/folders/0B_3Dz2J_fhmTVzFrdkFOVjdIeEE).
* The Google Drive folder contains the time series of the six observed networks.
* All files have three columns: 1 unix timestamp, 2 user id, 3 user id.
* If the value in the 3rd column is "-1", then instead of an edge a root adopter was observed.
* Each undirected edge occurs once in the file, when it appeared first in the time series.
* Files are indexed by the same codes used in the submitted paper.

## Installation and requirements

* For compling the cpp part, we use SCons.
* The following modules are required to run codes written in Python:
   * Numpy
   * Scipy
   * Matplotlib
   * Pandas
   * Seaborn
   * Networkx

### Measurements covered by IPython notebooks

* [Average degree](https://github.com/WsdmSubmission28/networkgrowth/blob/master/ipython/es_avgdeg.ipynb)
* [Evolving power-law degree distributions](https://github.com/WsdmSubmission28/networkgrowth/blob/master/ipython/es_dist.ipynb)
* [Average degree and the exponent of the power-law degree distribution](https://github.com/WsdmSubmission28/networkgrowth/blob/master/ipython/es_degdist.ipynb)
