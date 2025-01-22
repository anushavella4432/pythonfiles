n=input('enter sentence: ')
m=n.split()
print(len(m))

#with recursion
def Split(n):
    m=n.split()
    print(len(m))
n=input('enter the sentence: ')
k=Split(n)
