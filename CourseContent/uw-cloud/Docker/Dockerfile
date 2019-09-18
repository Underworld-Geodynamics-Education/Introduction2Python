FROM lmoresi/uw_user_cloud:2019.09.13ix_dev

## =============================================================
## base - image ... whatever functionality you want to provide !
## This is my unix / python stuff (but it doesn't have underworld)
##
## This dockerfile builds an image from this content, and serves the
## sample web pages and notebooks at port 8080
##
## docker run -p 8181:8080 --name="docker-web-notebooks-test" -t lmoresi/lmoresi/docker-web-notebooks-module
## and then browse the docker VM ip address on port 8181 (for example)
##
## OR just use kitematic and click on the preview image
##
## =============================================================

USER root

# The following installations are required for:
# various: build-essential
# stripy: gcc,  gfortran
# lavavu: libgl*mesa*, libpng-dev, libtiff-dev, libx11-dev
# lavavu: freeglut*, xvfb

RUN apt-get update -y ;
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends --fix-missing \
        gcc gfortran \
        libpng-dev \
        libtiff-dev \
        libx11-dev \
        build-essential \
        libgl1-mesa-dri \
        libgl1-mesa-glx \
        freeglut3 \
        freeglut3-dev \
        xvfb \
        git \
        libproj-dev \
        libhdf5-dev netcdf-bin libnetcdf-dev \
        libgdal-dev \
        && rm -rf /var/lib/apt/lists/*

RUN pip3 install numpy scipy
RUN pip3 install h5py
RUN pip3 install obspy
RUN pip3 install cartopy
RUN pip3 uninstall stripy -y
RUN pip3 install stripy git+https://github.com/underworldcode/stripy.git@dev
RUN pip3 install litho1pt0 --upgrade
RUN pip3 install lavavu --upgrade
RUN pip3 install imageio
RUN pip3 uninstall webdav -y
# RUN rm -rf /usr/local/lib/python3.5/site-packages/webdav
RUN pip3 install git+https://github.com/lmoresi/webdav.git --no-cache-dir
RUN pip3 install cloudstor
RUN pip3 install pillow

USER jovyan
WORKDIR  /home/jovyan
