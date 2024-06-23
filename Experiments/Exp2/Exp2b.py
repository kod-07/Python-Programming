while(True):
    print("1. TO PERFORM ADDITITON")
    print("2. TO PERFORM SUBTRACTION")
    print("3. TO PERFORM MULTIPICATION")
    print("4. TO PERFORM DIVISION")
    print("5. Exit")
    a = int(input("Choice any one of the above option : "))
    if a == 1:
        b = int(input("Enter first number : "))
        c = int(input("Enter second number : "))
        print("The addition of 2 number is ",b+c)
    elif a == 2:
        b = int(input("Enter first number : "))
        c = int(input("Enter second number : "))
        print("The Subtraction of 2 number is ",b+c)
    elif a == 3:
        b = int(input("Enter first number : "))
        c = int(input("Enter second number : "))
        print("The Multiplication of 2 number is ",b+c)
    elif a == 4:
        b = int(input("Enter first number : "))
        c = int(input("Enter second number : "))
        print("The Division of 2 number is ",a/b)
    elif a == 5:
        print("!!!!!!!Exiting the program!!!!!!!")
        break
    else:
        print("Invalid input ")