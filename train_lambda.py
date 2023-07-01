preco_tecnologia = {
    'notebook asus': 2450,
    'iphone': 4500,
    'samsung galaxy': 3000,
    'tv samsung': 1000,
    'ps5': 3000,
    'tablet': 1000,
    'notebook dell': 3000,
    'ipad': 3000,
    'tv philco': 800,
    'notebook hp': 1700
}

#Fazendo por function

def calcular_imposto(item):
    return item * 1.3

preco_imposto = list(map(calcular_imposto, preco_tecnologia.values()))   #funcao, iterable
#print(preco_imposto)

#POR LAMBDA

preco_imposto2 = list(map(lambda item: item * 1.3, preco_tecnologia.values()))   #lambda item: retorno do item, iterable
#print(preco_imposto2)

#----------------------------------------------------------------

#FILTER()
#fazendo por function

def maiorque2000(item):
    return item[1] > 2000     #retorna False or True
 
produtos_acima_2000 = dict(list(filter(maiorque2000, preco_tecnologia.items())))    #funcao , iterable
#print(produtos_acima_2000)

#fazendo por lambda
produtos2_acima_2000 = dict(list(filter(lambda item: item[1] > 2000, preco_tecnologia.items())))  #lambda item: retorno do item, iterable
#print(produtos2_acima_2000)
