#!/bin/bash

rm requirements.txt || true

poetry export --without-hashes --format=requirements.txt --output=requirements.txt