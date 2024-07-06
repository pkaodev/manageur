#!/bin/sh

curl https://github.com/pkaodev/Manageur/raw/main/manageur_setup.zip -o manageur_setup.zip \
&& unzip manageur_setup.zip \
&& rm manageur_setup.zip \
&& setup_manageur/run.sh