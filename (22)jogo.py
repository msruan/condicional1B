def main():
    horas1 = int(input('Digite a hora em que o jogo iniciou: '))
    min1 = int(input('Digite os minutos: '))
    horas2 = int(input('Digite a hora em que o jogo terminou: '))
    min2 = int(input('Digite os minutos: '))
    duracao = verify(horas1, min1,horas2,min2)
    saida(duracao)

def verify(horas1,min1,horas2,min2):
    mins_inicio = horas1 * 60 + min1
    mins_fim = horas2 * 60 + min2
    return mins_fim - mins_inicio

def saida(mins):
    print(f'O jogo durou {mins} minutos!')

main()