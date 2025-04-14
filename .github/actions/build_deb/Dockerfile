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
    debhelper \
    dh-python

# use only bash shell
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# workdir
# WORKDIR /ws
# RUN mkdir -p /ws/src && \
#     cd /ws/src && \
#     git clone -b humble https://github.com/InnoboticsSRL/awtube_interfaces.git

# install rosdep
# RUN rosdep init; rosdep update; apt update
# RUN apt update; rosdep install --from-paths src --ignore-src -r -y --rosdistro=humble

# compile
# RUN . /opt/ros/humble/setup.sh; colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release

# Generate Debian packaging files using bloom and build the Debian package
# RUN source /opt/ros/humble/setup.sh && \
#     cd src/awtube_interfaces && \
#     bloom-generate rosdebian && \
#     fakeroot debian/rules binary

# Copy the entrypoint script into the container
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Specify the entrypoint
ENTRYPOINT ["/entrypoint.sh"]