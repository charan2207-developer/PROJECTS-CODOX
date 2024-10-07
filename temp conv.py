x = input("enter the which value you are converting (if Celsius enter C or if Fahrenheit enter F) : ")
if x == "C" or x == "c":
    y = float(input("Enter the value in celsius to convert to Fahrenheit : "))
    z = (y * 9/5) + 32
    print(f"the value of {y}°c in Fahrenheit is {z}")
elif x == "F" or x == "f":
    a = float(input("Enter the value in Fahrenheit to convert to celsius : "))
    b = (a - 32) * 5/9
    print(f"the value of {a}°f in celsius is {b}")
else:
    print("enter the valid input either c or f")