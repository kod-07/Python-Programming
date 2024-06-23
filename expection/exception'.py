try:
    print("Resource open ")
    a = int(input("Enter 1st number : "))
    b = int(input("Enter 2nd number : "))
    print(a/b)

except ZeroDivisionError as e :
    print("You cannot divide by 0 ")
except ValueError as e:
    print("Enter integer value ")
except Exception as e:
    print("Invalid Error")
finally:
    print("Resource Closed")