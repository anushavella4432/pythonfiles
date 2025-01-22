'''s = input()
d = {
    'a': 0,"e": 0,"i": 0,"o": 0,"u": 0
}
for i in s:
    if i in "aeiou":
        d[i] += 1
ans, maxValue = '',0
for key, value in list(d.items()):
    if value > maxValue:
        ans = key
        maxValue = value
print(ans)'''

a=[1,2,3,4,5]
b=a[1:4]
print(a)