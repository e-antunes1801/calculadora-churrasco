homem = input("Quantos homens participarão do churrasco? ")
mulher = input("Quantas mulheres participarão do churrasco? ")
criancas = input("Quantas crianças participarão do churrasco? ")
refri = input("Quantos pessoas beberão bebidas não alcoolicas? ")
cerva = input("Quantas adultos beberão cerveja? ")
carne_homem = float(homem)*0.5
carne_mulher = float(mulher)*0.4
carne_crianca = float(criancas)*0.2
refri_adulto = float(refri)*1.5
refri_crianca = float(criancas)*0.75
total_cerva = float(cerva)*5
acompanhamentos = (float(homem) + float(mulher) + float(criancas)*0.2)
total_carnes = carne_homem + carne_mulher + carne_crianca
total_refri = refri_adulto + refri_crianca
print(f'O total de carnes é de {total_carnes}kg')
print(f'O total de bebidas NÃO alcoolicas é de {total_refri} litros')
print(f'O total de cervejas é de {total_cerva} latas')
