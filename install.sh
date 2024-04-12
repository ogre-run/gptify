#!/bin/bash

# Install ogre-gptrepo wheel

## uninstall older versions
rm -r dist
pipx uninstall gptify

## Build wheel and install miniogre
poetry build && pipx install dist/*.whl
