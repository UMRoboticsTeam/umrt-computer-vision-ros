from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.actions import LifecycleNode


def generate_launch_description():
    return LaunchDescription([


   config_path = os.path.join(
        get_package_share_directory('umrt-aruco-detection-ros'),
        'launch',
        'aruco_params.yaml'
        )
    
    aruco_node = LifecycleNode(
        package='aruco_opencv',
        executable='aruco_tracker',
        name='aruco_tracker',
        output='screen',
        parameters=[config_path]
    )


#to check state of lifecycle node:
    #ros2 lifecycle set /aruco_tracker configure
    #ros2 lifecycle set /aruco_tracker activate


    ])
