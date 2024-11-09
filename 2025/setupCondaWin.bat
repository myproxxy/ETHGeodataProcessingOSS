@echo off
:: Create the conda environment with python 3.12
conda create --name gpETHZ2025 python=3.12 -y

:: Activate the conda environment (this will open a new command line instance)
call conda activate gpETHZ2025

:: Install notebook and GDAL from conda-forge
conda install -c conda-forge notebook -y
conda install -c conda-forge gdal -y

:: Pause to keep the window open (optional)
pause