def main():
    print("Informe a primeira data!")
    dia1 = int(input('Digite o dia da primeira data: '))
    mes1 = int(input('Digite o mês da primeira data: '))
    ano1 = int(input('Digite o ano da primeira data: '))
    print("Informe a segunda data!")
    dia2 = int(input('Informe o dia da segunda data: '))
    mes2 = int(input('Informe o mês da segunda data: '))
    ano2 = int(input('Informe o ano da segunda data: '))
    data = verify(dia1,mes1,ano1,dia2,mes2,ano2)
    saida(data)
    
def verify(dia1,mes1,ano1,dia2,mes2,ano2):
    if (ano1 > 0 and ano2 > 0) and (31 >= dia1 > 0 and 31 >= dia2 > 0) and (0 < mes1 <= 12 and 0 < mes2 <= 12):
        if ano1 > ano2:
            data = "primeira"
        if ano2 > ano1:
            data = "segunda"
        elif ano1 == ano2:
            if mes1 > mes2:
                data = "primeira"
            if mes2 > mes1:
                data = "segunda"
            elif mes1 == mes2:
                if dia1 > dia2:
                    data = "primeira"
                if dia2 > dia1:
                    data = "segunda"
                elif dia1 == dia2:
                    data = 0
    else:
        data = None
    return data


    
def saida(data):
    if data == None:
        print('Datas inválidas!')
    else:
        if data == 0:
            print('As datas são iguais!')
        else:
            print('A',data,'é a mais recente!')

main()