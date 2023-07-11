arquivo = open('Alunos.txt', 'r')
conteudo = arquivo.readlines()
del conteudo[:4]
#print(conteudo)

#criar condições
qtd_anuncio = 0
qtd_org = 0
qtd_yt = 0
qtd_igfb = 0
qtd_site = 0

#percorrer lista
for item in conteudo:
    email, origem = item.split(',')
    #print(email)
    #print(origem)
    if '_org' in origem:
        qtd_org+=1
        if 'hashtag_yt_org' in origem:
            qtd_yt+=1
        if 'hashtag_ig_org' in origem or 'hashtag_igfb_org' in origem:
            qtd_igfb+=1
        if 'hashtag_site_org' in origem:
            qtd_site+=1
    else:
        qtd_anuncio+=1
        
print(f'Quantidade Anuncio: {qtd_anuncio}')
print(f'Quantidade Organico: {qtd_org}')
print(f'Quantidade Youtube: {qtd_yt}')
print(f'Quantidade Instagram: {qtd_igfb}')
print(f'Quantidade Site: {qtd_site}')

#criar novo arquivo txt com resultados
with open ('Resultado da Pesquisa', 'w') as arquivo2:
    arquivo2.write(f'Quantidade Anuncio: {qtd_anuncio}\n')
    arquivo2.write(f'Quantidade Organico: {qtd_org}\n')
    arquivo2.write(f'Quantidade Youtube: {qtd_yt}\n')
    arquivo2.write(f'Quantidade Instagram: {qtd_igfb}\n')
    arquivo2.write(f'Quantidade Site: {qtd_site}\n')
    