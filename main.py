import math

from plotter import plot_energies
from simulation import run_simulation

a0 = math.radians(30) # angle between edge positions
w0 = 0.1 # angular speed
dt = 0.01
n_steps = 10000     # number of steps (10 sec)

option = 'rk2'
# You have two options:
# 1. rk2 (improved Euler's method);
# 2. rk4

df = run_simulation(a0, w0, dt, n_steps, option)
plot_energies(df, option)
