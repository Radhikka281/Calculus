import matplotlib.pyplot as plt
import numpy as np

# Constants
initial_distance = 9.9  # Initial distance of galaxies
hubble_constant = 70  # Hubble constant (adjust as needed)
simulation_duration = 1000  # Duration of the simulation in arbitrary units
time_interval = 0.1  # Time interval for each frame in the simulation

# Function to calculate the velocity based on Hubble's law
def hubble_law(distance):
    return hubble_constant * distance

# Simulation
time_points = np.arange(0, simulation_duration, time_interval)
distances = [initial_distance]
velocities = [hubble_law(initial_distance)]

for time in time_points[1:]:
    # Update distance and velocity based on Hubble's law
    new_distance = distances[-1] + velocities[-1] * time_interval
    new_velocity = hubble_law(new_distance)

    distances.append(new_distance)
    velocities.append(new_velocity)

# Plotting
plt.plot(time_points, distances, label='Galaxy Distance')
plt.xlabel('Time (in sec)')
plt.ylabel('Distance (in lightyear)')
plt.title('Cosmic Expansion Simulation')
plt.legend()
plt.grid(True)
plt.show()
