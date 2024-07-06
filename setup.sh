#!/bin/sh

curl -LO https://github.com/pkeraoe/Manageur/raw/main/setup_manageur.zip \
&& unzip setup_manageur.zip \
&& rm setup_manageur.zip \
&& setup_manageur/run.sh