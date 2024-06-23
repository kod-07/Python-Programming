def rec(x):
    if x==0:
       return 1
    else:
        return x*rec(x-1)
X = int(input("Enter number to find factorial : "))
print("The factrial = ",rec(X))