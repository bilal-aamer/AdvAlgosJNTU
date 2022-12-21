def mul (A, B):
    if(A == 1 or B == 1):
        return A*B
    else:
        a1 = str(A)[0:len(str(A))//2]
        a0 = str(A)[len(str(A))//2:len(str(A))]
        
        print(type(a1),a0,b1,type(b0))
        
        n = max(len(A), len(B))
        
        
        c2 = mul(str(a1),str(b1))
        c0 = mul(str(a0),str(b0))
        x = mul(str(a0+a1), str(b0+b1))
        
        return c2(*10**(n)) + (x-c2-c0)*(10**(n//2)) + c0

A = int(input("Enter first number(4 digit): "))
B = int(input("Enter second number(4 digit): "))
C = mul(A,B)

print("The product of the two numbers is: ", C)
