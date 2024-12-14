# 2 - Crie uma lista com as notas de um aluno.
# - Calcule a média das notas.
# - Verifique se o aluno foi aprovado (média >= 7).
# - Imprima a média e a situação do aluno.

notas = [4, 5, 6, 8]

soma_notas = 0
for nota in notas:
    soma_notas += nota

media = soma_notas / len(notas)

if media >= 7:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

print("Media: ", media)
print("Situacao: ", situacao)



