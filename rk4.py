from pendulum import derivative, euler

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