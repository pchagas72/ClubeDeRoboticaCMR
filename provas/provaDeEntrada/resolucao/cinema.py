# recebe as idades

idade1 = int(input(""))
idade2 = int(input(""))

# verifica a idade e preço
l = [idade1, idade2]

preco = 0

# calcula valor
for i in l:
    if i <= 17:
        preco += 20
    elif i >= 18 and i <= 59:
        preco += 30
    elif i >= 60:
        preco += 25
#valor dos ingressos
print(preco)
