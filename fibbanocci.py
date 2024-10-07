print("ENTER INTO FIBONACCI SERIES : ")
def x(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b 
        b=c
        print(c)
x(int(input("ENTER THE FIB NUMBER : ")))