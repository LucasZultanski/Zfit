# CADASTRO 
print ("INFORMAÇÕES BASICAS:")
print("NOME:")
nome = str(input())
print("======================")
print ("IDADE:")
idade = int(input())
print("======================")
print("ALTURA (em CM):")
altura = float(input())
print("======================")
print ("PESO ATUAL: ")
peso_atual = int(input())
print("======================")

while True:
    print("Qual é seu nivel de atividade física:")
    print("0 - Sedentário (pouco ou nenhum exercício)")
    print("1 - Leve (exercício leve ou esportes 1-3 dias por semana)")
    print("2 - Moderado (exercício moderado ou esportes 3-5 dias por semana)")
    print("3 - Intenso (exercício intenso ou esportes 6-7 dias por semana)")
    print("4 - Muito intenso (exercício muito intenso, esportes e um trabalho fisicamente exigente):")
    nivel_de_atividade_fisica = int(input())

    if nivel_de_atividade_fisica == 0:
        nivel_de_atividade_fisica =  1.2
        break
    
    if nivel_de_atividade_fisica == 1:
        nivel_de_atividade_fisica =  1.375
        break

    if nivel_de_atividade_fisica == 2:
        nivel_de_atividade_fisica =  1.55
        break

    if nivel_de_atividade_fisica == 3:
        nivel_de_atividade_fisica =  1.725
        break

    if nivel_de_atividade_fisica == 4:
        nivel_de_atividade_fisica =  1.9
        break
    else:
        print("Esse numero não faz parte das alternativas")
print("======================")
print("Qual é o seu sexo: ")
tmb = 0
while True:
    print("1 - Homem")
    print("2 - Mulher")

    sexo = int(input())
    if sexo == 1:
        tmb = 88.362 + (13.397 * peso_atual) + (4.799 * altura) - (5.677 * idade)
        break
    if sexo == 2:
        tmb = 447.593  + (9.247 * peso_atual) + (3.098 * altura) - (4.330 * idade)
        break
    else:
        print("Esse numero não faz parte das alternativas")

# CALCULO PARA BULKING ADD 500 DE CALORIAS (excedente de 500 calorias para o bulking.)
calorias_diarias = str((tmb * nivel_de_atividade_fisica) + 250)[:4]
print("======================")
print(f"{nome} suas calorias diarias são: {calorias_diarias} no seu primeiro mês vai ser ")

calorias_diarias = str((tmb * nivel_de_atividade_fisica) + 350)[:4]
print("======================")
print(f"{nome} suas calorias diarias são: {calorias_diarias} no seu segundo mês vai ser ")

calorias_diarias = str((tmb * nivel_de_atividade_fisica) + 500)[:4]

print("======================")
print(f"{nome} suas calorias diarias são: {calorias_diarias} no seu terceiro mês vai ser ")

# CALCULAR AS PROTEINAS
proteinas = peso_atual * 1.6

# CALCULAR AS PROTEINAS CARBOIDRATOS
carboidratos = (calorias_diarias * 0.50) / 4

# CALCULAR AS GORDURAS
gorduras = (calorias_diarias * 0.25) / 9


