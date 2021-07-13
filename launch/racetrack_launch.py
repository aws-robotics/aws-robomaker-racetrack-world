#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ROS2 AWS Robomaker Racetrack World Launch File.

This script launches AWS Racetrack World in ROS2. 

Revision History:

        2021-07-09 (Animesh): Baseline Software.

Example:
        $ colcon build && source install/setup.bash && ros2 launch aws_robomaker_racetrack_world racetrack_launch.py

"""


#___Import Modules:
import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PythonExpression


#___Function:
def generate_launch_description():
	
    # Get the package directory
    package_dir = get_package_share_directory('aws_robomaker_racetrack_world')
    
    
    # Create launch configuration variables
    use_simulator = LaunchConfiguration('use_simulator')
    headless = LaunchConfiguration('headless')
    world = LaunchConfiguration('world')
    
    
    # Declare the launch arguments
    declare_use_simulator_cmd = DeclareLaunchArgument(
        'use_simulator',
        default_value='True',
        description='Whether to start the simulator')
    
    declare_simulator_cmd = DeclareLaunchArgument(
        'headless',
        default_value='False',
        description='Whether to execute gzclient)')
    
    declare_world_cmd = DeclareLaunchArgument(
        'world',
        default_value=os.path.join(package_dir, 'worlds', 'racetrack_day.world'),
        description='Full path to world model file to load')
    
    # Specify the actions
    start_gazebo_server_cmd = ExecuteProcess(
        condition=IfCondition(use_simulator),
        cmd=['gzserver', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so', world],
        cwd=[package_dir],
        output='screen')
    
    start_gazebo_client_cmd = ExecuteProcess(
        condition=IfCondition(PythonExpression([use_simulator, ' and not ', headless])),
        cmd=['gzclient'],
        cwd=[package_dir],
        output='screen')
    
    
    # Create the launch description and populate
    ld = LaunchDescription()
    
    # Declare the launch options
    ld.add_action(declare_use_simulator_cmd)
    ld.add_action(declare_simulator_cmd)
    ld.add_action(declare_world_cmd)
    
    # Add all actions
    ld.add_action(start_gazebo_server_cmd)
    ld.add_action(start_gazebo_client_cmd)
        
    return ld


#                                                                              
# end of file
"""ANI717"""