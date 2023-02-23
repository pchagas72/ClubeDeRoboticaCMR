l = [] # cria uma lista vazia para receber os inputs

for i in range(0,6): # recebe o input 6 vezes
    g = input().upper()
    l.append(g)

v = l.count('V') # conta quantos Vs existem na lista l

# verificação do grupo
if v == 6 or v == 5: 
    print(1)
    
elif v == 3 or v == 4:
    print(2)

elif v == 1 or v == 2:
    print(3)
    
else:
    print(-1)
    