# Exercício 3.12 do livro Introdução à Programação com Python - 4ª edição
# Cap. 3 - Variáveis e entrada de dados

distancia = float(input("Insira a distância em metros: "))
velocidade_media = float(input("Insira a velocidade média: "))

tempo = distancia / velocidade_media

tempo_convertido = tempo // 60

segundos = tempo - (tempo_convertido * 60)

print(f"O tempo de viagem é de {tempo_convertido:.0f} minuto's e {segundos:.0f} segundo's")