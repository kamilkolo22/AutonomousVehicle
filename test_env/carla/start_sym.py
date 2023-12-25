import carla
import random
import os

os.system("bash start_carla.sh")

client = carla.Client('localhost', 2000) 
world = client.get_world() 

# Sync mode
settings = world.get_settings()
settings.synchronous_mode = True  # Enables synchronous mode
world.apply_settings(settings)

# Get the blueprint library and the spawn points for the map
bp_lib = world.get_blueprint_library() 
spawn_points = world.get_map().get_spawn_points() 

# Move the spectator behind the vehicle 
vehicle = world.get_actor(138)
if vehicle.type_id != "vehicle.tesla.model3":
    raise TypeError("Selected vehicle is not tesla 3!")

spectator = world.get_spectator() 
transform = carla.Transform(vehicle.get_transform().transform(carla.Location(x=-4, z=2.5)),
                            vehicle.get_transform().rotation)
spectator.set_transform(transform) 

# Add traffic to the simulation
for i in range(30): 
    vehicle_bp = random.choice(bp_lib.filter('vehicle')) 
    npc = world.try_spawn_actor(vehicle_bp, random.choice(spawn_points))

# TODO
# Set the all vehicles in motion using the Traffic Manager
#for i in range(1, 10):
#    world.tick()
#    for v in world.get_actors().filter('*vehicle*'): 
#        v.set_autopilot(True)
  