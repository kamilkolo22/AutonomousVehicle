import time

import carla


def check_car_exists(timeout: int = 15):
    count: int = 0

    while True:
        client = carla.Client('localhost', 2000)
        world = client.get_world()
        world.wait_for_tick()

        for act in world.get_actors():
            try:
                if act.attributes['role_name'] == "ego_vehicle":
                    print("True")
                    return True
            except KeyError:
                pass
            except Exception as e:
                raise e

        if count > timeout:
            print("False")
            return False

        count += 1
        time.sleep(1)


if __name__ == "__main__":
    check_car_exists(15)
