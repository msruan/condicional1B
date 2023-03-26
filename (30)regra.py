def main():
    num = int(input("Digite um número de 4 dígitos: "))
    regra = calculo(num)
    saida(regra)
def calculo(num):
    milhar = num // 1000
    cen = num % 1000 // 100
    dez = num % 1000 % 100 // 10
    uni = num % 1000 % 100 % 10

    if num == ((milhar*10 + cen) + (dez*10+uni)) ** 2:
        return "segue a regra"
    else:
        return "não segue a regra"
def saida(regra):
    print(f'O número {regra}!')
main()