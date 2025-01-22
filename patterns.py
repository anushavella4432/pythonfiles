''''print("program1")
for i in range(1,6):
    for j in range(1,6):
        print("*", end=" ")
    print()

print("program2")
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=" ")
    print()

print("program3")
for i in range(1,6):
    for j in range(1,6-i+1):
        print("*", end=" ")
    print()


print("program4")
for i in range(1,6):
    for s in range(1,5-i+1):
        print(" ", end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
'''

'''print("program5")
for i in range(1,5):
    for j in range(1,5):
        if i==1 or i==4 or j==1 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

