def main():
    num = int(input("Digite um número de 4 dígitos: "))
    quadrado = calculo(num)
    saida(quadrado)
def calculo(num):
    milhar = num // 1000
    cen = num % 1000 // 100
    dez = num % 1000 % 100 // 10
    uni = num % 1000 % 100 % 10

    if num ** 0.5 == (milhar*10 + cen) + (dez*10+uni):
        return "quadrado perfeito"
    else:
        return "não é um quadrado perfeito"
def saida(quadrado):
    print(f'O número {quadrado}!')
main()