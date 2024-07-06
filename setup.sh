#!/bin/sh

curl -L https://github.com/pkaodev/Manageur/raw/main/manageur_setup.zip -o manageur_setup.zip \
&& unzip manageur_setup.zip -d setup_manageur \
&& rm manageur_setup.zip \
&& setup_manageur/src/run.sh