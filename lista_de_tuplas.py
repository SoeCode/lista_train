#Analise simples das vendas de um Banco de Dados de um e-commerce.
#Realizando Unpacking de tuplas para manipulação.

#Faturamento de IPhone no dia 20/08/2020
vendas = [
    ('20/03/2023', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/03/2023', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/03/2023', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/03/2023', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/03/2023', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/03/2023', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/03/2023', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/03/2023', 'ipad', 'prata', '128gb', 4000, 5000),
    ('21/03/2023', 'iphone 11', 'purple', '256', 289, 3800),
    ('21/03/2023', 'iphone 13 pro', 'verde', '512', 4200, 9000),
]

faturamento = 0
for data, produto, cor, capac, quant, valor in vendas:
    if 'iphone' in produto and data == '20/03/2023':
        faturamento += quant*valor
               
print(f'o total de vendas no dia 20/03/2023 foi: R${faturamento}')

#Produto mais vendido (em unidades) no dia 21/08/2020
produto_mais_vend = ''
qtde_mais_vend = 0
for item in vendas:
    data, produto, cor, capac, quant, valor = item
    if data == '21/03/2023':
        if quant > qtde_mais_vend:
            produto_mais_vend = produto
            qtde_mais_vend = quant

print(f' A quantidade mais vendida do dia 21/03/2023 foi: {qtde_mais_vend} unidades.')