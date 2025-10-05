# Create a function that calculates the kinetic energy of a body:
def kinetic_energy(m, v):
    e = 0.5*m*(v**2)
    print(e)
    return e
kinetic_energy(2, 3)