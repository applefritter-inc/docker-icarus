# icarus in docker

### [source code](https://github.com/applefritter-inc/docker-icarus/)

why make this?
it allows you to run the icarus server on macOS/windows, without the need for a VM to run linux. \
it also reduces the complications of running icarus on linux.

## how to use?
1. clone docker image with `docker pull appleflyer/icarus-server`
2. run docker image `docker run -it -p 0.0.0.0:8126:8126 appleflyer/icarus-server`

## credits
icarus server: [writable](https://github.com/MunyDev) \
slapping everything in a docker image: [appleflyer](https://github.com/appleflyerv3)
