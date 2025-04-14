FROM ros:humble-ros-base

# Install build tool
RUN apt update && apt install -y python3-colcon-common-extensions git ros-dev-tools 

# install tools
RUN apt update && apt install -y \
    python3-colcon-common-extensions \
    git \
    ros-dev-tools \
    autoconf \
    libtool \
    python3-vcstool \
    tmux \
    vim \
    python3-pip \
    fakeroot \
    python3-bloom \
    build-essential \
    debhelper

# use only bash shell
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Copy the entrypoint script into the container
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Specify the entrypoint
ENTRYPOINT ["/entrypoint.sh"]