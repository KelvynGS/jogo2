import random

numero_atual = random.randint(1,100)
print(f"O número atual é {numero_atual}.")
proximo_numero = random.randint(1,100)
escolha = input("O próximo número será maior ou menor? ").lower()
if escolha == "maior" and proximo_numero > numero_atual:
  print(f'Você Acertou! é {proximo_numero}.')
elif escolha == "menor" and proximo_numero < numero_atual:
  print(f'Você Acertou! é {proximo_numero}.')
if escolha == "maior" and proximo_numero < numero_atual:
  print(f'Você Errou! é {proximo_numero}.')
elif escolha == "menor" and proximo_numero > numero_atual:
  print(f'Você Errou! é {proximo_numero}.')
