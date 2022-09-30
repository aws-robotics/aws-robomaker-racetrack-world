import os
import sys

import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    mode = 'day' # Change mode
    package_dir = get_package_share_directory('aws_robomaker_racetrack_world')
    gazebo_ros = get_package_share_directory('gazebo_ros')

    gazebo_client = launch.actions.IncludeLaunchDescription(
	launch.launch_description_sources.PythonLaunchDescriptionSource(
            os.path.join(gazebo_ros, 'launch', 'gzclient.launch.py')),
        condition=launch.conditions.IfCondition(launch.substitutions.LaunchConfiguration('gui'))
     )
    gazebo_server = launch.actions.IncludeLaunchDescription(
        launch.launch_description_sources.PythonLaunchDescriptionSource(
            os.path.join(gazebo_ros, 'launch', 'gzserver.launch.py'))
    )
    
    return LaunchDescription([
        DeclareLaunchArgument(
          'world',
          default_value=[os.path.join(package_dir, 'worlds', 'racetrack_' + mode + '.world'), ''],
          description='SDF world file'),
        DeclareLaunchArgument(
            name='gui',
            default_value='false'
        ),
        DeclareLaunchArgument(
            name='use_sim_time',
            default_value='true'
        ),
        DeclareLaunchArgument('state',
            default_value='true',
            description='Set "true" to load "libgazebo_ros_state.so"'),
        gazebo_server,
        gazebo_client,
    ])


if __name__ == '__main__':
    generate_launch_description()
