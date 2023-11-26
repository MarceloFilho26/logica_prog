eleitores = int(input("Informe o total de eleitores: "))
brancos = int(input("Informe o total de votos brancos: "))
nulos = int(input("Informe o total de votos Nulos: "))
validos = int(input("Informe o total de votos válidos: "))

percentual_brancos = (brancos/eleitores) * 100
percentual_nulos = (nulos/eleitores) * 100
percentual_validos = (validos/eleitores) * 100

print(f"O percentutal de votos brancos corresponde a {percentual_brancos}%.")
print(f"O percentutal de votos nulos corresponde a {percentual_nulos}%.")
print(f"O percentutal de votos válidos corresponde a {percentual_validos}%.")
