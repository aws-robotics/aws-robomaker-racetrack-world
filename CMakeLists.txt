cmake_minimum_required(VERSION 3.5)

project(aws_robomaker_racetrack_world)

find_package(ament_cmake REQUIRED)
find_package(gazebo_ros REQUIRED)

install(
  DIRECTORY launch models worlds
  DESTINATION share/${PROJECT_NAME}
)

ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/env-hooks/aws_robomaker_racetrack_world.dsv.in")

ament_export_dependencies(ament_cmake)
ament_export_dependencies(gazebo_ros)

ament_package()