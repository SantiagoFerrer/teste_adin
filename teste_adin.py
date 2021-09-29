import random
randomlist = []
d = 500000
for i in range (d):
    randomlist.append(random.randint(0,d))

ordenado = []

while randomlist:
    menor = randomlist[0]
    for x in randomlist: 
        if x < menor:
            menor = x
    ordenado.append(menor)
