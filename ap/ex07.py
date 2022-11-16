contar_maior_50=0
tamanho=2
contar_pessoas_entre_10_e_20=0
soma_das_alturas=0
contar_peso_menor_40=0
for i in range(tamanho):
#ler idade, altura e peso
    idade=int(input(f"Informe a idade da pessoa {i+1}"))
    altura=int(input(f"Informe a altura da pessoa {i+1}"))
    peso=float(input(f" Informe o peso da pessoa {i+1}"))

    if idade>+50:
        contar_maior_50+=1 
    if idade >=10 and idade <=20:
        contar_pessoas_entre_10_e_20+=1
        soma_das_alturas+=altura
    if peso < 40:
        contar_peso_menor_40+=1

media_alturas=(soma_das_alturas/contar_pessoas_entre_10_e_20)
porcentagem=contar_peso_menor_40/tamanho*100
