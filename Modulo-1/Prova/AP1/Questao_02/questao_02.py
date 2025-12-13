# Exiba: -> lembrar questão das frutas
# ● O total arrecadado na semana -> .sum() da receita
# ● A média das receitas -> .mean()
# ● O nome do associado que mais arrecadou -> .max()
# ● Exiba apenas os associados que arrecadaram acima da média, mostrando o nome e o valor correspondente (use operação booleana sobre a própria Series).

import pandas as pd

receita_associados = pd.Series(
    [12000, 17500, 14300, 16000, 19500], 
    index = ["Luca Brasi", "Peter Clemenza", "Sal Tessio", "Tom Hagen", "Michael Corleone"]
)

print("Família : ") # exibindoa series
print(receita_associados)

print("======================================")
#● O total arrecadado na semana -> .sum() da receita:
total_semana = receita_associados.sum()
print(f"Arrecadamento Total da Semana : {total_semana}")

print("======================================")
# ● A média das receitas -> .mean()
media_semana = receita_associados.mean()
print(f"Média da Semana : {media_semana}")

print("======================================")
# ● O nome do associado que mais arrecadou -> .idmax() 
associado_max = receita_associados.idxmax()
print(f"Associado que Mais Arrecadou : {associado_max} com {receita_associados["Michael Corleone"]}") # deixei mockado só para a visualização ficar melhor

print("======================================")
# ● Exiba apenas os associados que arrecadaram acima da média, mostrando o nome e o valor correspondente (use operação booleana sobre a própria Series).
acima_media = receita_associados[receita_associados >= media_semana]
print(acima_media)
print("======================================")
