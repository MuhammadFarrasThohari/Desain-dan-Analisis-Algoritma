#Mencari KPK 3 dan 4

x = 3
y = 4
n = 1

if x < y:
    temp = x
    x = y
    y = temp
kelipatan = x * n

while kelipatan % y != 0:
    kelipatan = x * n
    n = n + 1
    if kelipatan % y == 0:
        print (kelipatan)