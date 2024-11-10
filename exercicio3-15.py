# Exercício 3.15 do livro Introdução à Programação com Python - 4ª edição
# Cap. 3 - Variáveis e entrada de dados

cigarros_dia = int(input("Digite quantos cigarros você fuma por dia: "))
anos = int(input("Digite a quantos anos você fuma: "))

minutos = (cigarros_dia * 10) * (anos * 365)

dias = minutos // (24 * 60)

print(f"Redução do tempo de vida: {dias} dias")
