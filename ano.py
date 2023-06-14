#Faturamento do Melhor e do Pior Mês do Ano e Continuação
#1
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]
vendas_ano = vendas_1sem + vendas_2sem

#cod para printar melhor e pior mês do ano.
#Mês mais vendido
mais_vend_ano = max(vendas_ano)
#print(mais_vend_ano)
pos_maior_valor = vendas_ano.index(mais_vend_ano)
#print(pos_maior_valor)
i = vendas_ano.index(mais_vend_ano)
#print(i)
mes_mais_vend = meses[i]
#print(mes_mais_vend)
print(f'O maior valor vendido foi no mes de {mes_mais_vend} com R${mais_vend_ano:,.2f} reais vendidos.')

#Mês menos vendido
menos_vend_ano = min(vendas_ano)
#print(mais_vend_ano)
pos_menor_valor = vendas_ano.index(menos_vend_ano)
#print(pos_maior_valor)
i = vendas_ano.index(menos_vend_ano)
#print(i)
mes_menos_vend = meses[i]
#print(mes_menos_vend)
print(f'O menor valor vendido foi no mes de {mes_menos_vend} com R${menos_vend_ano:,.2f} reais vendidos.')

#total vendas e representação da porcentagem do maior mês vendido
total_vendas = sum(vendas_ano)
#total_vendas = total
print(f'R${total_vendas:,.2f}')
porcentagem_vendas = mais_vend_ano / total_vendas * 100
#print(porcentagem_vendas)
print(f'R${mais_vend_ano:,.2f}')
print(f'{mes_mais_vend} representou {porcentagem_vendas:.2f}% do total. ')

#top 3 valores de vendas do ano
lista_maior_vendas = sorted(vendas_ano,reverse=True)
#print(lista_maior_vendas)
top3 = lista_maior_vendas[0:3]
print(f'valor mais vendido: {lista_maior_vendas[0]:,.2f}')
print(f'segundo valor mais vendido: {lista_maior_vendas[1]:,.2f}')
print(f'terceiro valor mais vendido: {lista_maior_vendas[2]:,.2f}')
#print('fim')

#testando branch
#testando branch 3
