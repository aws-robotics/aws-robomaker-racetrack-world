#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ROS2 AWS Robomaker Racetrack World Launch File.

This script launches AWS Racetrack World in ROS2. 

Revision History:

        2021-12-25 (Animesh): Baseline Software.

Example:
        $ ros2 launch aws_robomaker_racetrack_world racetrack.launch.py

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
	
    # set directories
    aws_robomaker_racetrack_world_DIR = get_package_share_directory('aws_robomaker_racetrack_world')
    
    # launch arguments
    use_sim_time_launch_argument = DeclareLaunchArgument(
		name = 'use_sim_time',
		default_value = 'True',
		description = 'Use simulation (Gazebo) clock if true',
        )
    
    headless_launch_argument = DeclareLaunchArgument(
		name = 'headless',
		default_value = 'False',
		description = 'Run gzclient or not for GUI',
        )
    
    world_launch_argument = DeclareLaunchArgument(
		name = 'world',
		default_value = os.path.join(aws_robomaker_racetrack_world_DIR, 'worlds', 'racetrack_day.world'),
		description = 'Full path to world model file to load',
        )
    
	# execute processes
    start_gazebo_server = ExecuteProcess(
		cmd = ['gzserver', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so', LaunchConfiguration('world')],
		cwd = [aws_robomaker_racetrack_world_DIR],
        output = 'screen',
        )
    
    start_gazebo_client = ExecuteProcess(
		condition = IfCondition(PythonExpression(['not ', LaunchConfiguration('headless')])),
		cmd = ['gzclient'],
        cwd = [aws_robomaker_racetrack_world_DIR], 
        output = 'screen',
        )
        
    # return launch description
    return LaunchDescription([
        use_sim_time_launch_argument,
        headless_launch_argument,
        world_launch_argument,
        start_gazebo_server,
        start_gazebo_client,
        ])


#                                                                              
# end of file
"""ANI717"""
