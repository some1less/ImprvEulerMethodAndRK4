import math

from plotter import plot_energies
from simulation import run_simulation


a0 = math.radians(30) # angle between edge positions
w0 = 0.1 # angular speed
dt = 0.01
n_steps = 1000     # number of steps (e.g 10 sec)

df = run_simulation(a0, w0, dt, n_steps)

plot_energies(df)
