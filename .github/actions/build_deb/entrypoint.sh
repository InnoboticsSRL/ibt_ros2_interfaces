#!/bin/bash
set -e

# Create a .deb package
rosdep update && \
rosdep install --from-paths . --ignore-src -r -y --rosdistro=humble && \
source /opt/ros/humble/setup.sh && \
bloom-generate rosdebian && \
fakeroot debian/rules binary

# Move any generated .deb packages to the GitHub workspace
mkdir -p /github/workspace/deb
mv ../*.deb /github/workspace/deb/