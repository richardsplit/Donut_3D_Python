import math

x = math.cos(0)
y = math.sin(0)

for angle in range(0, 360, 10):
    angle_radius = math.radians(angle)
    x = math.cos(angle_radius)
    y = math.sin(angle_radius)
