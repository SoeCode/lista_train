#Sistema de compras:
#Um programa simples que roda e adiciona ao carrinho de compras até o input do produto ser vazio.
#E no final mostra a lista de compras.
compras = []
while True:
    produto = input('Produto: ')
    if not produto:
        print('Usuário encerrou a ação.')
        break
    qtde = int(input('Quantidade: '))
    compras.append([produto,qtde])
print(f' a lista de compras foi: {compras}')

