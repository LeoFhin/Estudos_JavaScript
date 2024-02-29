# Atividade 1 Front End 2 - Obtenha dados da altura e o sexo (M ou F) de 
# 15 pessoas e apresente os seguintes resultados:

# - A maior e a menor altura do grupo;
# - A média de altura dos homens;
# - O número de mulheres.

#Aluno - Leonardo santos de lima - P1b


altura_maxima = []
altura_minima = []
mulheres = 0
altura_homens = []
num_homens = 0

for i in range(15):
    sexo = str(input("digite seu sexo (M \ F): "))
    altura = float(input("informe a sua altura: ")) 

    altura_maxima.append(altura)  
    altura_minima.append(altura)  
    
    if sexo == 'F':
        mulheres = mulheres + 1
    elif sexo == 'M':
        altura_homens.append(altura)
        num_homens += 1

media_homens = sum(altura_homens) / num_homens if num_homens > 0 else 0

print(f"Maior altura: {max(altura_maxima)}")  
print(f'Menor altura: {min(altura_minima)}')  
print(f'Média de altura dos homens: {media_homens:.2}')
print(f'Número de mulheres: {mulheres}')