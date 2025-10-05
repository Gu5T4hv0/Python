# Create a function that converts speed from km/h to m/s:
def kmh_to_ms(v):
    vms = v/3.6
    print(f"The velocity in meters per second is {vms:.2f}m/s²")
    return vms
kmh_to_ms(20)