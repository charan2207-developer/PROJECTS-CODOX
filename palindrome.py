print("WELCOME TO PALINDROME CHECKER")
x = input("ENTER THE STRING TO CHECK PALINDROME OR NOT : ")
if x == x[::-1]:
    print("IT IS PALINDROME")
else:
    print("IT IS NOT PALINDROME ")