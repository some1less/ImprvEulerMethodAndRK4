import seaborn as sns
import matplotlib.pyplot as plt

def plot_energies(energies, option):
    # wide_format -> long_format in seaborn
    df_melt = energies.melt(id_vars='Time (s)',
                      value_vars=['Kinetic Energy', 'Potential Energy', 'Total Energy'],
                      var_name='Energy Type',
                      value_name='Energy')

    # seaborn graph built
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df_melt, x='Time (s)', y='Energy', hue='Energy Type')
    if option == 'rk2':
        plt.title("Dependency energy/time(secs) (improved Euler's method)")
    elif option == 'rk4':
        plt.title("Dependency energy/time(secs) (RK4 method)")
    plt.xlabel("Time (s)")
    plt.ylabel("Energy")
    plt.show()