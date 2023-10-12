#!/bin/sh

set -e

echo "Installing homebrew if it's not installed..."
which brew || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

echo "Installing Python 3 if it's not installed..."
which python3 || brew install python3

echo "Installing lefthook if it's not installed..."
which lefthook || brew install lefthook

echo "Setting up git hooks for this project"
lefthook install

echo "Installing dependencies on host (so that we can configure a virtual environment for our IDE)"
./scripts/go/install-dependencies-on-host.sh
