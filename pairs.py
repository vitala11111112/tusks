from random import*
a = [randint(-10,10) for i in range(100)]
b = int(input())
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] + a[j] == b:
            print(a[i],a[j])