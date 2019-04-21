#!/bin/bash

git config --global user.name "maosa"

git config --global user.email "andreasmaos@gmail.com"

git config --global --list

# Check if osxkeychain is installed
git credential-osxkeychain

# Set up HTTPS
git config --global credential.helper osxkeychain
