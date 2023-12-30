import carla
import random

v_num = 100
client = carla.Client('localhost', 2000) 
world = client.get_world() 

# Sync mode
settings = world.get_settings()
settings.synchronous_mode = True  # Enables synchronous mode
settings.fixed_delta_seconds = 0.05
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
for i in range(v_num):
    vehicle_bp = random.choice(bp_lib.filter('vehicle')) 
    npc = world.try_spawn_actor(vehicle_bp, random.choice(spawn_points))
    world.tick()

print(f"{v_num} vehicles spawned")
