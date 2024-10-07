import string
x = input("ENTER YOUR PASSWORD : ")
a = 8
has_upper = any(i.isupper() for i in x)
has_lower = any(i.islower() for i in x)
has_digit = any(i.isdigit() for i in x)
has_special = any(i in string.punctuation for i in x)
if len(x) >= a and has_digit and has_lower and has_upper and has_special:
    print("PASSWORD IS STRONG")
elif len(x) >= a and has_digit and (has_lower or has_upper ) :
    print("PASSWORD IS moderate")
else:
    print("weak")




