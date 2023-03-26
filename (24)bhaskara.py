def main():
    a = float(input('Digite a medida a da equação: '))
    b = float(input('Digite a medida b da equação: '))
    c = float(input('Digite a medida c da equação: '))
    x1,x2 = bhaskara(a,b,c)
    saida(x1,x2)

def bhaskara(a,b,c):
    delta = b ** 2 - 4 * a * c
    x1 = (-b + delta ** 0.5) / 2 * a
    x2 = (-b - delta ** 0.5) / 2 * a
    return x1,x2

def saida(x1,x2):
    print(f'As raízes da equação do 2º grau são {x1} e {x2}!')

main()