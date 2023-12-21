# arm_11_src
Ros2 packages for ARM 11 laboratory. Implementation of TurtleBot3 Waffle robot unknown maze solving. \
Based on [ROS2-FrontierBaseExplorationForAutonomousRobot](https://github.com/abdulkadrtr/ROS2-FrontierBaseExplorationForAutonomousRobot.git) repository.

## Launch docker
For this example you need [ARM 11](https://github.com/kamilmlodzikowski/LabARM/tree/6f20e80ae233c7e7465553be193223bb00a0f2de/Lab11-Problem2) docker container.

## How to use
After creating docker container place these packages into your ```arm_ws/src/``` directory.
Don't forget to build your workspace.
```bash
colcon build --symlink-install
```
To enable navigation for robot run map node:
```bash
ros2 launch slam_toolbox online_async_launch.py
```
After that run Gazebo simulation using one of commands: \
Simple maze:
```bash
ros2 launch arm_11_sim simple_maze.launch.py
```
Complicated maze:
```bash
ros2 launch arm_11_sim complicated_maze.launch.py
```
To start autonomous frontier based exploration use:
```bash
ros2 run autonomous_exploration control
```
To measure time elapsed and check if robot reached maze goal run:
```bash
ros2 run maze_goal maze_goal 
```