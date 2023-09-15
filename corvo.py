def binario_para_inteiro(sequencia):
    if '*' in sequencia or '-' in sequencia: 
        # vejo se tem '*' na sequencia e depois eu vejo se tem '-'
        # se eu fisesse """"('*' or '-') in sequencia"""" quando um desse verdade ele não procuraria pelo outro
        sequencia = sequencia.replace('*', '1')
        sequencia = sequencia.replace('-', '0')

    return int(sequencia, 2)
    # esse 2 faz o int entender que é um binário e passa ele para um inteiro

lista_normal = []
lista_somada = []

conta_canto = 0

while conta_canto != 3:
    print('escreva "caw" para o corvo somar')
    acao_corvo = input('coloque a sequencia do corvo: ').strip()
    
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
