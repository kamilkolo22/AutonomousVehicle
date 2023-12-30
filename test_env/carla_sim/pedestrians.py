import carla
import random
import time


p_num = 200
client = carla.Client('localhost', 2000)
world = client.get_world()

walker_bp = world.get_blueprint_library().filter("walker.pedestrian.*")
controller_bp = world.get_blueprint_library().find("controller.ai.walker")

actors = []
for i in range(p_num):
    # location
    trans = carla.Transform()
    trans.location = world.get_random_location_from_navigation()
    trans.location.z += 1

    # walker actor
    walker = random.choice(walker_bp)
    actor = world.spawn_actor(walker, trans)
    world.wait_for_tick()

    # walker AI controller
    controller = world.spawn_actor(controller_bp, carla.Transform(), actor)
    world.wait_for_tick()

    # managing pedestrians through controller
    controller.start()
    controller.go_to_location(world.get_random_location_from_navigation())

print(f"{p_num} pedestrians spawned, press ctr+C to stop controller...")

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    client.apply_batch([carla.command.DestroyActor(x) for x in actors])
    print("KeyboardInterrupt: Pedestrians controller stopped, actors destroyed!")
    time.sleep(2)
