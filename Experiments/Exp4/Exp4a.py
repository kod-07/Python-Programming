#b) Write a program to read 3 subject marks and display pass or failed using class and object
class marks:
    def __init__(self):
        self.sub1 = int(input("Enter marks of subject 1 out of 100: "))
        self.sub2 = int(input("Enter marks of subject 2 out of 100: "))
        self.sub3 = int(input("Enter marks of subject 3 out of 100: "))
    def result(self):
        sum = (self.sub1+self.sub2+self.sub3)/3
        if sum<36:
            print("Fail")
        else:
            print("Pass")
def main():
    A = marks()
    A.result()
main()