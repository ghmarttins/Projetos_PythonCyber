# 1 - Crie uma lista com os nomes de 5 frutas.
# - Acesse e imprima o primeiro e o último elemento da lista.
# - Adicione mais duas frutas à lista.
# - Remova a segunda fruta da lista.
frutas = ["maçã", "banana", "laranja"]
numeros = [1, 5, 10, 15, 20]
misturado = [1, "dois", 3.0, True]

print("Frutas:", frutas)
print("Números:", numeros)
print("Lista Mista:", misturado)

# Acessando elementos de uma lista
print("A primeira fruta é:", frutas[0])  # Acesso pelo índice (começa em 0)
print("A última fruta é:", frutas[-1])  # Acesso pelo índice negativo (último elemento)

# Adicionando elementos em uma lista
frutas.append("uva")
print("\nLista de frutas atualizada:", frutas)

# Removendo elementos em uma lista
frutas.remove("banana")
print("Lista de frutas atualizada:", frutas)

# Iterando em uma lista com um loop for
print("\nFrutas na lista:")
for fruta in frutas:
  print(fruta)


# Iterando em uma lista com um loop for e índice
print("\nFrutas na lista (com índice):")
for i in range(len(frutas)):
  print(f"Índice {i}: {frutas[i]}")