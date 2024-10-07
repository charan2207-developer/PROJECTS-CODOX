
#this project is done using the regular expression
#we import the regular expression
import re
x=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
# (This is a regular expression (regex) used to match email addresses. Here's a breakdown of what each part does:
#
# \b: Word boundary. Ensures the match is a whole word.
# [A-Za-z0-9._%+-]+: Matches one or more of the characters: letters (A-Z, a-z), digits (0-9), and these special characters: ., _, %, +, -.
# @: Matches the "@" symbol.
# [A-Za-z0-9.-]+: Matches one or more of the characters: letters (A-Z, a-z), digits (0-9), dots (.), and hyphens (-).
# \.: Matches a literal dot (".").
# [A-Z|a-z]{2,7}: Matches 2 to 7 letters, either uppercase (A-Z) or lowercase (a-z).
# \b: Another word boundary to ensure the match is complete.)
def check(email):
    if(re.search(x,email)):
        print("Valid Email")
    else:
        print("Invalid Email")
email = input("Enter your email : ")
check(email)
