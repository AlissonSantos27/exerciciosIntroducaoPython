# Exercício 3.10 do livro Introdução à Programação com Python - 4ª edição
# Cap. 3 - Variáveis e entrada de dados

salario = float(input("Insira o salário: "))
porcentagem = float(input("Insira a porcentagem do aumento: "))

aumento = salario * (porcentagem / 100) # calcula o aumento a partir de (porcentagem / 100) * salario

salario = salario + aumento

print(f"O aumento é de R${aumento:.2f}. O novo salário é de R${salario:.2f} ")