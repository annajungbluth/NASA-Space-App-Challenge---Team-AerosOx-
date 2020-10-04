# NASA-Space-App-Challenge---Team-AerosOx-

## Requirements
All code can be run with a jupyter notebook, Python 3, and requires the following packages:
pandas, numpy, tqdm, h5py, matplotlib, netCDF4, beautifulsoup4

The notebooks were set up to run on the Google Colab service.

## Files description

Below we include the basic description of the files. Note that these files load large dataset from the internet. Running them can take a while and requires an internet connection.

To load the data on air pollution, the file "Load AQUA\_MODIS Data.ipynb" can be used.
Once the data is loaded, notebooks listed in the next paragraph can be used to analyse it.

Files "Demo High Res.ipynb", "All AQUA\_MODIS Data.ipynb", and "AQUA\_MODIS.ipynb" can be used to load and analyse the data.
"Demo High Res" and "AQUA\_MODS" both load and display a single month of particle data over the world and the UK.
"All AQUA\_MODS Data" loads the full dataset and shows the changes in the particles over time.

File "get\_nhs.py" loads the data on NHS spending on perscriptions over time. It loads the dataset and displays the spending over time.
File "CCG\_time\_respiratory\_spend.ipynb" combines the data on NHS spending with the data on aerosol.
"test.pickle" is a dump of intermediate data created so that "CCG\_time\_respiratory\_spend.ipynb" can be ran independently from the rest of the files.
