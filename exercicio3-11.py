# Exercício 3.11 do livro Introdução à Programação com Python - 4ª edição
# Cap. 3 - Variáveis e entrada de dados

mercadoria = float(input("Insira o preço da mercadoria: "))
porcentagem = float(input("Insira a porcentagem do desconto: "))

desconto = mercadoria * (porcentagem / 100) # calcula o desconto a partir de (porcentagem / 100) * mercadoria

mercadoria = mercadoria - desconto

print(f"O desconto é de R${desconto:.2f}. O novo valor da mercadoria é de R${mercadoria:.2f} ")