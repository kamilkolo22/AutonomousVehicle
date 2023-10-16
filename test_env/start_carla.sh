# Uruchomienie Carla
gnome-terminal --tab -- /opt/carla-simulator/CarlaUE4.sh

# Run ros bridge
sleep 3
source ~/carla-ros-bridge/catkin_ws/devel/setup.bash 
gnome-terminal --tab -- roslaunch carla_ros_bridge carla_ros_bridge.launch town:='town05'

# objects
sleep 3
# cd /carla-ros-bridge/catkin_ws
source ~/carla-ros-bridge/catkin_ws/devel/setup.bash
gnome-terminal --tab -- roslaunch carla_spawn_objects carla_spawn_objects.launch objects_definition_file:=/home/kamil/Pulpit/AV/test_env/car_spawn.json

sleep 3
gnome-terminal --tab -- roslaunch carla_manual_control carla_manual_control.launch

# Configuration
# Rviz
sleep 3
gnome-terminal --tab -- rosrun rviz rviz -d /home/kamil/Pulpit/AV/test_env/visual_settings.rviz
