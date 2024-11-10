# Exercício 3.9 do livro Introdução à Programação com Python - 4ª edição
# Cap. 3 - Variáveis e entrada de dados

dias = int(input("Insira a quantidade de dias: "))
horas = int(input("Insira a quantidade de horas: "))
minutos = int(input("Insira a quantidade de minutos: "))
segundos = int(input("Insira a quantidade de segundos: "))

minutos_convertidos = 60 # quantidade de segundos que tem em um minuto
horas_convertidas = minutos_convertidos * 60 # quantidade de segundos que tem em uma hora
dia_convertido = 24 * horas_convertidas # quantidade de segundos que tem em um dia

soma = ((dias * dia_convertido) + (horas * horas_convertidas) + (minutos * minutos_convertidos)
        + (segundos))

print(f"Em {dias} dia's, {horas} hora's, {minutos} minuto's e {segundos} segundo's tem {soma} segundo's")