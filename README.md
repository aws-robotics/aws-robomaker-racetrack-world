# AWS RoboMaker Racetrack World ROS package

![Gazebo01](docs/images/gazebo_01.png)

**Visit the [RoboMaker website](https://aws.amazon.com/robomaker/) to learn more about building intelligent robotic applications with Amazon Web Services.**

# Include the world from another package

* Update .rosinstall to clone this repository and run `rosws update`
```
- git: {local-name: src/aws-robomaker-racetrack-world, uri: 'https://github.com/aws-robotics/aws-robomaker-racetrack-world.git', version: ros1}
```
* Add the following to your launch file:
```xml
<launch>
  <!-- Launch World -->
  <include file="$(find aws_robomaker_racetrack_world)/launch/racetrack.launch"/>
  ...
</launch>
```

# Load directly into Gazebo (without ROS)
```bash
export GAZEBO_MODEL_PATH=`pwd`/models
gazebo worlds/racetrack_day.world
```

# ROS Launch with Gazebo viewer (without a robot)
```bash
# build for ROS
rosdep install --from-paths . --ignore-src -r -y
colcon build

# run in ROS
source install/setup.sh
roslaunch aws_robomaker_racetrack_world view_racetrack.launch
```

# Robot Simulation
A good initial robot position near the start line is (2.75, -14.00, 0.0).   

![Gazebo01](docs/images/turtlebot_burger.png)

# Building
Include this as a .rosinstall dependency in your SampleApplication simulation workspace and run the following commands:

```bash
$ rosws update
$ rosdep install --from-paths . --ignore-src -r -y
$ colcon build
```

# Modes
## Day 
```
roslaunch aws_robomaker_racetrack_world view_racetrack.launch gui:=true mode:=day
```
![Gazebo01](docs/images/day_01.png)

## Day Emtpy 
```
roslaunch aws_robomaker_racetrack_world view_racetrack.launch gui:=true mode:=day_empty
```
![Gazebo01](docs/images/day_empty_01.png)

## Night
```
roslaunch aws_robomaker_racetrack_world view_racetrack.launch gui:=true mode:=night
```
![Gazebo01](docs/images/night_01.png)

