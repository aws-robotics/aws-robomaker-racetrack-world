import os
import sys

import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                [get_package_share_directory(
                    'aws_robomaker_racetrack_world'), '/launch/racetrack.launch.py']
            ),
            launch_arguments={
                'gui': 'true',
                'mode': 'day'
            }.items()
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
