# vehicle_classifier.py

def classify_vehicle(wheels):
    """ Returns vehicle type based on wheel count. """
    if wheels == 2:
        return "Motorcycle"
    elif wheels == 3:
        return "Trike"
    elif wheels == 4:
        return "Car"
    else:
        return "Unknown"
