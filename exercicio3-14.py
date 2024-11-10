# Exercício 3.14 do livro Introdução à Programação com Python - 4ª edição
# Cap. 3 - Variáveis e entrada de dados

km_percorridos = float(input("Insira a quantidade de Km percorridos: "))
dias = int(input("Insira a quantidade de dias: "))

km_percorridos = km_percorridos * 0.15
dias = dias * 60
soma = km_percorridos + dias

print(f"Valor a pagar: R${soma:.2f}")