# 1 - Crie uma lista com os nomes de 5 frutas.
# - Acesse e imprima o primeiro e o último elemento da lista.
# - Adicione mais duas frutas à lista.
# - Remova a segunda fruta da lista.
frutas = ["maçã", "banana", "laranja"]

print("Frutas na lista: ", frutas)
print("A primeira fruta é:", frutas[0])
print("A última fruta é:", frutas[-1])  

frutas.append("uva")
print("\nLista de frutas atualizada:", frutas)

frutas.remove("uva")
print("Lista de frutas atualizada:", frutas)

