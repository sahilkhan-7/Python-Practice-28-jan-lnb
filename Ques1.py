print("Printing current and previous number sum in a range(10)")

i = 0 # Previous number
for k in range(10): # k represent current number 
    print(f"Current Number {k} Previous Number {i} , Sum is : {i + k}")
    i = k
    
