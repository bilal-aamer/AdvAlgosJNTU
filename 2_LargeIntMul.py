def mul (A, B):
    if(A == 1 or B == 1):
        return A*B
    else:
        a1,a0 = divmod(A, 10**(A//2))
        b1,b0 = divmod(B, 10**(B//2))
        n = max(len(str(A)), len(str(B)))
        c2 = mul(a1,b1)
        c0 = mul(a0,b0)
        x = mul(a0+a1, b0+b1)
        return c2(*10**(n)) + (x-c2-c0)*(10**(n//2)) + c0

A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
C = mul(A,B)

print("The product of the two numbers is: ", C)
