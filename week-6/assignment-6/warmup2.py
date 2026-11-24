def celcius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celcius(f):
    return (f - 32) * 5/9

print(f"12° C is = {celcius_to_fahrenheit(12):.1f}\u00b0C")
print(f"72F is = {fahrenheit_to_celcius(72):.1f}\u00b0F")