# Project - Task 3
# Assigned to Kevin Bozarth

''' 3) Next, using your cleaned-up dataset, have your code come up with an estimate
    for both the depth of the transit in units of relative flux and for its length in days.
    Using the transit depth, you can estimate the radius of the exoplanet using the following equation
    (assume the radius of the star is one solar radii):
    D = (R_planet/R_star)^2
'''

import numpy as np

# PLACEHOLDER. These two values will obtain the cleaned up data from Task 2
time = None
flux = None

if time is None or flux is None:
    raise NotImplementedError("time and flux needs cleaned up data from Task 2.")

# Transit depth
baseline = np.median(flux)
transitMin = np.min(flux)
depth = baseline - transitMin

# Identify transit region
threshold = baseline - depth/2
transitMask = flux < threshold # Assigns a bool to transitMask

timeStart = time[transitMask][0]
timeEnd = time[transitMask][-1]
duration = timeEnd - timeStart

# Planet radius
rStar = 1.0 # Solar radii
rPlanet = rStar * np.sqrt(depth)

print(f"Transit depth: {depth}")
print(f"Transit duration (days): {duration}")
print(f"Planet radius (solar radii): {rPlanet}")
