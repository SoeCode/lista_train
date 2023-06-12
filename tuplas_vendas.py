#Unpacking de tuplas para facilitar o nosso código.
#Exercicío simples simples de atingimento de Meta manipulando lista de tuplas.


#identificar quais os vendedores que bateram a meta e qual foi o valor que eles venderam.
meta = 10000
vendas = [
    ('Lidia', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Suzi', 3750),
    ('Ana', 10300),
    ('Alison', 7870),
]

for item in vendas:
    nome, total_vendas = item
    if total_vendas>meta:
        print(f'{nome} bateu a meta, com {total_vendas} produtos vendidos.')
    else:
        restante = meta - total_vendas
        print(f'{nome} NÃO bateu a meta, faltaram {restante} produtos.')