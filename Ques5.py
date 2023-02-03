def exponent(b, e):
    if e >= 0:
        return b**e
    
base = int(input("Enter Base : "))
exp = int(input("Enter exponent or power : "))

print(f"{base} raise to power {exp} is {exponent(base, exp)}")