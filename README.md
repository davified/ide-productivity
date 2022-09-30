# IDE productivity tips tutorial

## Prerequisites

1. [For Windows users] To install Docker Desktop, you'll need Windows 10 Pro or Enterprise version 15063.
2. Install Docker

- If you have Docker Desktop license
  - [for Mac](https://docs.docker.com/docker-for-mac/install/)
  - [for Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
  - [for Windows](https://docs.docker.com/docker-for-windows/install/)
- If you don't have a Docker Desktop license, you can use `colima`
  - Setup instructions: https://gist.github.com/jcartledge/0ce114e9719a62a4776569e80088511d

- **Important things to note**:
  - You will be prompted to create a DockerHub account. Follow the instructions in order to download Docker
  - Follow the installation prompts (go with the default options) **until you have successfully started Docker**
  - [Windows users] When prompted to enable Hyper-V and Containers features, click 'Ok' and let computer restart again.
  - You may have to restart your computer 2-3 times.

3. Start Docker on your desktop (Note: Wait for Docker to complete startup before running the subsequent commands. You'll know when startup is completed when the docker icon in your taskbar stops animating)

## Setup

```sh
# start colima (if you're not using Docker Desktop)
colima start

# build
docker build . -t ide-productivity-exercise

# run container and start dev environment
docker run -it -v $(pwd):/code ide-productivity-exercise bash
```
