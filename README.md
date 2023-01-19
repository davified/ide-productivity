# IDE productivity tips tutorial

An exercise to demonstrate how to use the features of an IDE (PyCharm and VS Code) to code effectively.

## Setup

Run the go script to install pre-requisite dependencies. 
The go script will install Python 3 and Poetry, and create a virtual environment on the host. 
This will make it easier to configure our IDE to know about the Python interpreter for this project.   

```shell script
# mac users
scripts/go-mac.sh

# linux users
scripts/go-linux-ubuntu.sh

# windows
# work in progress. in the meantime, please install Docker manually if it's not already installed
```

Configure your IDE to use the python virtual environment (`./.venv/`) created in the go script. 
- [PyCharm instructions](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#existing-environment)
- [VS Code instructions](https://code.visualstudio.com/docs/python/environments)

## Tasks that you can run

```shell script
# start docker runtime
colima start

# install dependencies
./batect --output=all setup

# start container (i.e. local dev environment)
./batect start-dev-container

### in the dev container


```
