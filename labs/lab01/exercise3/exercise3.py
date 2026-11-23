def validate_entry(name, pin):
    if (name == "Director" and pin == 1122) or (name == "Security" and pin == 9900):
        return True
    else:
        return False

print(validate_entry("Director", 1122))
print(validate_entry("Director", 9900))
print(validate_entry("director", 1122))



