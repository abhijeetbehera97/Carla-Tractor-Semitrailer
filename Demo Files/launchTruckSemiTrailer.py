import glob
import os
import sys
import time
import random
import math

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla


client = carla.Client('localhost', 2000)
world = client.get_world()

bp_lib = world.get_blueprint_library()
spawn_points=world.get_map().get_spawn_points()

vehicle_bp1= bp_lib.find('vehicle.daf.dafxf')
vehicle_bp2=bp_lib.find('vehicle.trailer.trailer')

# Set the spawn point
spawn_point1 = carla.Transform(carla.Location(x=10, y=10, z=2), carla.Rotation())
spawn_point2 = carla.Transform(carla.Location(x=5, y=10, z=2), carla.Rotation())

# Spawn the vehicle
vehicle1 = world.spawn_actor(vehicle_bp1, spawn_point1)
vehicle2 = world.spawn_actor(vehicle_bp2, spawn_point2)




