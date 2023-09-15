def binario_para_inteiro(sequencia):
    if '*' in sequencia or '-' in sequencia: 
        sequencia = sequencia.replace('*', '1')
        sequencia = sequencia.replace('-', '0')

    return int(sequencia, 2)


lista_normal = []
lista_somada = []

conta_canto = 0

while conta_canto != 3:
    print('escreva "caw" para o corvo somar')
    acao_corvo = str(input('coloque a sequencia do corvo: ').strip())
    
    if acao_corvo != 'caw':
        numero_corvo = binario_para_inteiro(acao_corvo)
        lista_normal.append(numero_corvo) 
        print(lista_normal)

    else:
        conta_canto += 1
        lista_somada.append(sum(lista_normal))
        lista_normal.clear()
        print(lista_somada)


print(f'os números falados pelo corvo foram: {lista_somada}')
