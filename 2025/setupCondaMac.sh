#!/bin/bash

# zum Ausführen Berechtigungen ändern mit:
# chmod +x setup_conda_environment.sh

# Anschliessend ausführen mittels:
# ./setup_conda_environment.sh

# Skript zum Erstellen und Einrichten des Conda-Umfelds

# Erstelle das conda Umfeld mit Python 3.12
conda create --name gpETHZ2025 python=3.12 -y

# Aktivieren des conda Umgebungs
source $(conda info --base)/etc/profile.d/conda.sh
conda activate gpETHZ2025

# Installiere das Notebook und GDAL aus conda-forge
conda install -c conda-forge notebook -y
conda install -c conda-forge gdal -y