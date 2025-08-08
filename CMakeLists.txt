cmake_minimum_required(VERSION 3.8)
project(ibt_ros2_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(builtin_interfaces REQUIRED)


# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)
ament_export_dependencies(rosidl_default_runtime)
ament_export_dependencies(geometry_msgs std_msgs)


rosidl_generate_interfaces(${PROJECT_NAME}
  "action/MoveArm.action"
  "action/Docking.action"
  "msg/Waypoint.msg"
  "msg/MoveReq.msg"
  "msg/PoseRPY.msg"
  "msg/PoseRPYStamped.msg"
  "msg/VectorBool.msg"
  "srv/SetOutput.srv"
  "srv/GetInput.srv"
  "srv/SetAttrAll.srv"
  "srv/GetAttrAll.srv"
  DEPENDENCIES geometry_msgs std_msgs builtin_interfaces
)

# Export dependencies


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
