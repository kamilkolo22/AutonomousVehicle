import carla


def check_carla_running(timeout: int = 30):
    count: int = 0

    while True:
        client = carla.Client('localhost', 2000)
        client.set_timeout(1.0)
        try:
            world = client.get_world()
            world.wait_for_tick()
            print("True")
            return True
        except RuntimeError:
            pass
        except Exception as e:
            raise e

        count += 1
        if count >= timeout:
            print("False")
            return False


if __name__ == "__main__":
    check_carla_running(30)
