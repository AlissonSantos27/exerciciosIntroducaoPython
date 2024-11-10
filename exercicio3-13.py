# Exercício 3.13 do livro Introdução à Programação com Python - 4ª edição
# Cap. 3 - Variáveis e entrada de dados

celsius = float(input("Escreva uma temperatura em graus celsius: "))

fahrenheit = (9 * celsius / 5) + 32

print(f"{celsius:.2f} ºC é equivalente a {fahrenheit:.2f} ºF.")