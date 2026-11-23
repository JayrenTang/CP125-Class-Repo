def get_hourly_rate(vehicle_type, hour):
    if vehicle_type == "Electric":
        return 2.0
    elif vehicle_type == "Hybrid" and (hour >= 22 or hour <= 6):
        return 2.0
    elif vehicle_type == "Hybrid" and (hour <22 or hourse > 6):
        return 5.0
    else:
        return 5.0

print(get_hourly_rate("Hybrid", 23))
print(get_hourly_rate("Hybrid", 13))
print(get_hourly_rate("Sedan", 2))