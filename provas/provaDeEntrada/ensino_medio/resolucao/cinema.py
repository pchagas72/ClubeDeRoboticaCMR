# recebe as idades

idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))

# verifica a idade e preço
idades = [idade1, idade2]
preco = 0

# Calcula valor dos ingressos
for idade in idades:
    if idade <= 17:
        preco += 20
    elif idade >= 18 and idade <= 59:
        preco += 30
    elif idade >= 60:
        preco += 25
        
# Printa o valor dos ingressos
print(preco)
