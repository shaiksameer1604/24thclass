n=int(input("Enter no of sequence to be printed:"))
a=0
b=1
if n<2:
    print("invaid")
else:
    print(a,end=" ")
    print(b,end=" ")
    for i in range(n-2):
        c=a+b
        print(c,end=" ")
        a=b
        b=c