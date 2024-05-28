a = input("напишите два слова с той же длиной")
b = input()
k = 0
if len(a) != len(b):
    print("дебил для кого писали С ОДИНАКОВОЙ ДЛИНОЙ")
else:
    for i in range(len(a)):
        if a[i] != b[i]:
            k += 1
print("расстояние хэминга равна",k)
