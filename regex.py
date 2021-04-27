import re
r = re.compile(r'(\d{2}/\d{2}/\d{4}) (\d{2}:\d{2}) - ([^:]+)')
itens = []
with open('nome.txt') as arq:
    for linha in arq: # para cada linha do arquivo
        m = r.match(linha)
        print("\a", linha)
        print(m)
        if m: # se a regex encontrou um match, adiciona na lista
            itens.append(m.groups())
        

