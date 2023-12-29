############################################################
# Help                                                     #
############################################################
display_help() {
    echo "Usage: $0 [OPTIONS]"
    echo "Options:"
    echo "  --spawn-vehicles     Spawn ego vehicle and traffic"
    echo "  --autopilot          Start autopilot on spawned vehicles"
    echo "  --record             Start recording and saving from rgb camera"
    echo "  --manual             Run with manual steering of the car"
    echo "  --rviz               Run with RViz graphical interface"
    echo "  --help               Display this help message"
}

# Default parameter
include_manual=false
include_rviz=false
spawn_vehicles=false
autopilot=false
record=false

# Process command-line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --manual) include_manual=true;;
        --spawn-vehicles) spawn_vehicles=true;;
        --autopilot) autopilot=true;;
        --record) record=true;;
        --rviz) include_rviz=true;;
        --help) display_help; exit 0;;
        *) echo "Unknown parameter: $1"; exit 1;;
    esac
    shift
done

############################################################
# Start Carla                                              #
############################################################
gnome-terminal --tab -- /opt/carla-simulator/CarlaUE4.sh

# Check if Carla is running
output_carla=$(python3 toolbox/check_carla_running.py)

# Check the result
if [ "$output_carla" = "True" ]; then
    echo "Carla simulator is active."
elif [ "$output_carla" = "False" ]; then
    echo "Carla simulator is not active."
    exit
else
    echo "Error: Unable to determine Carla simulator status."
    exit
fi

############################################################
# Run ros bridge and spam objects                          #
############################################################
source ~/carla-ros-bridge/catkin_ws/devel/setup.bash
gnome-terminal --tab -- roslaunch carla_ros_bridge carla_ros_bridge.launch town:='town05'

# objects
sleep 1
source ~/carla-ros-bridge/catkin_ws/devel/setup.bash
gnome-terminal --tab -- roslaunch carla_spawn_objects carla_spawn_objects.launch objects_definition_file:="$(pwd)/car_spawn.json"

# Check if ego_vehicle exists
output_car=$(python3 toolbox/check_car_exists.py)

# Check the result
if [ "$output_car" = "True" ]; then
    echo "ego_vehicle has been spawned."
    is_car_spawned=true
elif [ "$output_car" = "False" ]; then
    echo "Warning! ego_vehicle has not been spawned!"
    is_car_spawned=false
else
    echo "Error: Unable to determine ego_vehicle status."
    exit
fi

############################################################
# Manual steering of the car                               #
############################################################

if [ "$include_manual" = true ]; then

  if [ "$is_car_spawned" = true ]; then
    gnome-terminal --tab -- roslaunch carla_manual_control carla_manual_control.launch
  else
    echo "Carla manual steering cannot be set, no ego_vehicle detected!"
  fi

fi

############################################################
# Configuration of Rviz                                    #
############################################################

if [ "$include_rviz" = true ]; then

  if [ "$is_car_spawned" = true ]; then
    gnome-terminal --tab -- rosrun rviz rviz -d "$(pwd)/visual_settings.rviz"
  else
    echo "Rviz graphical interface cannot be displayed, no ego_vehicle detected!"
  fi

fi

############################################################
# Spawn vehicles and run autopilot                         #
############################################################

if [ "$spawn_vehicles" = true ]; then
  python3 spawn_vehicles.py
fi

if [ "$autopilot" = true ]; then
  gnome-terminal --tab -- python3 autopilot.py
fi

############################################################
# Video recording                                          #
############################################################

if [ "$record" = true ]; then
  gnome-terminal --tab -- python3 record_data.py
fi
