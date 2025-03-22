import math

m = 1 # mass, 1 kg
l = 10 # length
a = math.radians(30) # angle between edge positions
w = 0.1 # angular speed
g = 10

def derivative(angle, ang_speed):
    k_a = ang_speed
    k_w = ( g / l ) * math.sin(angle)
    return k_a, k_w

print(derivative(a, w))

def euler(angle, ang_speed, k_a, k_w, dt):

    return angle + k_a * dt, ang_speed + k_w * dt

def rk4_step(a, w, dt):

    k1a, k1w = derivative(a, w)
    a_2, w_2 = euler(a, w, k1a, k1w, dt/2)
    k2a, k2w = derivative(a_2, w_2)
    a_2, w_2 = euler(a, w, k2a, k2w, dt)
    k3a, k3w = derivative(a_2, w_2)
    a_e, w_e = euler(a, w, k3a, k3w, dt)
    k4a, k4w = derivative(a_e, w_e)

    a_next = a + (k1a + 2 * k2a + 2 * k3a + k4a) * dt / 6
    w_next = w + (k1w + 2 * k2w + 2 * k3w + k4w) * dt / 6

    return a_next, w_next

def energies(a, w):
    E_k = 0.5 * m * (l ** 2) * (w**2)
    E_p = m * g * l * (1 - math.cos(a))
    E_total = E_k + E_p
    return E_k, E_p, E_total

dt = 0.01
a_next, w_next = rk4_step(a, w, dt)
print(a_next, w_next)

E_k, E_p, E_total = energies(a_next, w_next)

print("Кінетична енергія T =", E_k)
print("Потенційна енергія U =", E_p)
print("Повна енергія E =", E_total)
