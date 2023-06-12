#Identificando o crescimento de um produto de um e-commerce de um ano para o outro.
#manipulando listas de tuplas e fazendo o Unpacking de uma tupla para facilitar o código.


#Lógica da tupla = produto , vendas 2019, vendas 2020:
vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]


for nome, vendas2019, vendas2020 in vendas_produtos:
    if vendas2020 > vendas2019:
        crescimento = vendas2020/vendas2019-1
        print(f'{nome} Vendeu {vendas2020} unidades em 2020, {crescimento:.2%} a mais do que no ano de 2019.')
