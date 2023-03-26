def main():
    x1 = float(input('Digite a coordenada x do primeiro ponto: '))
    y1 = float(input('Digite a coordenada y do primeiro ponto: '))
    x2 = float(input('Digite a coordenada x do segundo ponto: '))
    y2 = float(input('Digite a coordenada y do segundo ponto: '))
    area = retangulo(x1,x2,y1,y2)
    saida(area)

def retangulo(x1,x2,y1,y2):
    largura = x2 - x1
    altura = y2 - y1

    return altura * largura
def saida(area):
    print(f'A área do retângulo mede {area}.')

main()