def somar_numeros(*args):
  soma = 0
  for num in args:
    soma += num
  return soma

print(somar_numeros(1, 2, 3, 4, 5)) # Saída: 15

print("carro"*30)