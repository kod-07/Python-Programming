t = (10,20,30,40,50,60,70,80,90,100)
print(t)
t2 = (1,2,3)
t = t+t2
print(t)
print(len(t))
for i in range(len(t)):
    print(t[i])
c = int(input("Enter element to search : "))
print(t.index(c))
