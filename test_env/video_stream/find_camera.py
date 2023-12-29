import carla


def find_camera():
    # Get world
    client = carla.Client('localhost', 2000)
    world = client.get_world()
    world.tick()

    # Find camera
    actors = world.get_actors()
    camera = None

    for a in actors:
        if a.type_id == "sensor.camera.rgb":
            camera = a
            break

    if camera is None:
        raise Exception("No camera detected!")

    return camera
