def is_leap_year(year):
    if year % 4 == 0 and (year / 100 != 0 or year % 400 == 0):
        return "Yes"
    else:
        return "No"

print(is_leap_year(2024))
print(is_leap_year(1900))
print(is_leap_year(2000))
