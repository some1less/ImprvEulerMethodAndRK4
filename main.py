import math
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

from pendulum import energies
from plotter import plot_energies
from rk4 import *

a0 = math.radians(30) # angle between edge positions
w0 = 0.1 # angular speed



dt = 0.01
n_steps = 10000     # number of steps (e.g 10 sec)
times = []
E_kinetic = []
E_potential = []
E_total = []


a = a0
w = w0
time = 0

# simulation
for i in range(n_steps):
    times.append(time)
    E_k, E_p, E_tot = energies(a, w)
    E_kinetic.append(E_k)
    E_potential.append(E_p)
    E_total.append(E_tot)
    a, w = rk4_step(a, w, dt)
    time += dt

# DataFrame creation for comfortable usage
df = pd.DataFrame({
    'Time (s)': times,
    'Kinetic Energy': E_kinetic,
    'Potential Energy': E_potential,
    'Total Energy': E_total
})

plot_energies(df)
