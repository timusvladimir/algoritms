from random import randint

n = 10
spisok = []

for i in range(n):
    spisok.append(randint(1, 10))

print(spisok)

for i in range(n-1):
    for j in range(n-1-i):
        if spisok[j] > spisok[j+1]:
           spisok[j], spisok[j+1] = spisok[j+1], spisok[j]

print(spisok)

N = 10
a = [randint(1, 99) for n in range(N)]
print(a)

i = 0
while i < N-1:
    j = 0
    while j < N-1-i:
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
        j += 1
    i += 1

print(a)
