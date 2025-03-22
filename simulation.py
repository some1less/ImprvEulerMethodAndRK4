import pandas as pd
from pendulum import energies
from rk4 import rk4_step
from rk2 import rk2_step

def run_simulation(a0, w0, dt, n_steps, option):
    times = []
    E_kinetic = []
    E_potential = []
    E_total = []

    a = a0
    w = w0
    time = 0

    # simulation
    if option == 'rk4':

        for i in range(n_steps):
            times.append(time)
            E_k, E_p, E_tot = energies(a, w)
            E_kinetic.append(E_k)
            E_potential.append(E_p)
            E_total.append(E_tot)
            a, w = rk4_step(a, w, dt)
            time += dt

    elif option == 'rk2':

        for i in range(n_steps):
            times.append(time)
            E_k, E_p, E_tot = energies(a, w)
            E_kinetic.append(E_k)
            E_potential.append(E_p)
            E_total.append(E_tot)
            a, w = rk2_step(a, w, dt)
            time += dt

    # DataFrame creation for comfortable usage
    df = pd.DataFrame({
        'Time (s)': times,
        'Kinetic Energy': E_kinetic,
        'Potential Energy': E_potential,
        'Total Energy': E_total
    })

    return df