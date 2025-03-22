import math
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


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

# wide_format -> long_format in seaborn
df_melt = df.melt(id_vars='Time (s)',
                  value_vars=['Kinetic Energy', 'Potential Energy', 'Total Energy'],
                  var_name='Energy Type',
                  value_name='Energy')

# seaborn graph built
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_melt, x='Time (s)', y='Energy', hue='Energy Type')
plt.title("Dependency energy/time(secs) (RK4 method)")
plt.xlabel("Time (s)")
plt.ylabel("Energy")
plt.show()
