

i=0

while i <5:
    idade=int(input("Digite  sua idade"))
    if i==0:
        menor_idade_sistema=idade
        maior_idade_sistema=idade

    if menor_idade_sistema > idade:
        menor_idade_sistema=idade
    if maior_idade_sistema < idade:
        maior_idade_sistema=idade
    i=i+1

print ({menor_idade_sistema})
print ({maior_idade_sistema})