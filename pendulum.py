# system set up
import math

m = 1 # mass, 1 kg
l = 10 # length
g = 10

def derivative(angle, ang_speed):
    k_a = ang_speed
    k_w = - ( g / l ) * math.sin(angle)
    return k_a, k_w

def euler(angle, ang_speed, k_a, k_w, dt):

    return angle + k_a * dt, ang_speed + k_w * dt

def energies(a, w):
    E_k = 0.5 * m * (l ** 2) * (w**2)
    E_p = m * g * l * (1 - math.cos(a))
    E_total = E_k + E_p
    return E_k, E_p, E_total