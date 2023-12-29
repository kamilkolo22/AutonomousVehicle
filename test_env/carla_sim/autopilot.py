import carla

client = carla.Client('localhost', 2000)
world = client.get_world()
world.tick()

vehicles_ids = [vehicle.id for vehicle in world.get_actors().filter('*vehicle*')]
for vehicle_id in vehicles_ids:
    world.tick()
    world.get_actor(vehicle_id).set_autopilot(True)
print("Vehicles autopilot activated")

# Keep process up to autopilot work properly
try:
    while True:
        pass
except KeyboardInterrupt:
    print("KeyboardInterrupt: Autopilot stopped!")
