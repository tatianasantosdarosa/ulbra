#idade e faixa etaria
i=0
pessoas_faixa1=0
pessoas_faixa5=0


for i in range (3):
    idade=int(input('Informe a sua idade:\n'))
    if idade <=15:
        pessoas_faixa1+=1
    if idade > 60:
        pessoas_faixa5+=1
print(f'A porcentagem de pessoas na primeira faixa etária é: {(pessoas_faixa1*100)/3}%.\n '
f'A porcentagem de pessoas na última faixa etária é: {(pessoas_faixa5*100)/3}%.\n')

