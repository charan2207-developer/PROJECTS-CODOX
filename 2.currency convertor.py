print("welcome to currency convertor : ")
print("YOU CAN CHANGE INDIAN CURRENCY TO OTHER COUNTRIES CURRENCY : ")
print("SELECT THE CURRENCY THAT YOU WANT TO CHANGE FROM IND TO OTHER : ")
print("1.USD\n"
      "2.AUD\n"
      "3.EUR")
x = int(input("PLEASE ENTER YOUR CHOICE : "))
if x == 1:
    c = int(input("ENTER THE INDIAN RUPEES : "))
    d = c//85
    print(f"THE VALUE OF {c} RUPEES IS {d} USD ")
elif x == 2:
    a = int(input("ENTER THE INDIAN RUPEES : "))
    b = a//54
    print(f"THE VALUE OF {a} RUPEES IS {b} AUD ")
elif x == 3:
    q = int(input("ENTER THE INDIAN RUPEES : "))
    r = q//84
    print(f"THE VALUE OF {q} RUPEES IS {r} EUR ")
else:
    print("ENTER THE VALID NUMBER ")