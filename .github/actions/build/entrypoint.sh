#!/bin/bash
set -e

# Build 
rosdep update && \
rosdep install --from-paths . --ignore-src -r -y --rosdistro=humble && \
source /opt/ros/humble/setup.sh && \
colcon build --symlink-install