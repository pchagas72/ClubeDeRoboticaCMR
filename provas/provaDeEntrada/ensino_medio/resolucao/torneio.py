lista_de_inputs = [] # Cria uma lista vazia para receber os inputs

for input_atual in range(0,6): # Recebe o input 6 vezes
    resultado_da_partida = input(f"Digite o resultado da {input_atual+1} partida: ").upper()
    lista_de_inputs.append(resultado_da_partida)

vitorias = lista_de_inputs.count('V') # Conta quantos Vs existem na lista de inputs

# Verificação do grupo
if vitorias == 6 or vitorias == 5: 
    print(1)
    
elif vitorias == 3 or vitorias == 4:
    print(2)

elif vitorias == 1 or vitorias == 2:
    print(3)
    
else:
    print(-1)
    
