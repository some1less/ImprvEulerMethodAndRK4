from pendulum import derivative, euler

def rk2_step(a, w, dt):

    k1a, k1w = derivative(a, w)
    a_2, w_2 = euler(a, w, k1a, k1w, dt/2)
    k2a, k2w = derivative(a_2, w_2)

    a_next = a + (k1a + k2a) * dt / 2
    w_next = w + (k1w + k2w) * dt / 2

    return a_next, w_next