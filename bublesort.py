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
