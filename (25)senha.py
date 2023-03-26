def main():
    print("A senha deve ter 4 dígitos!")
    senha = int(input("Digite a senha: "))
    igual = verify(senha)
    saida(igual)
def verify(senha):
    m = senha // 1000
    c = senha % 1000 // 100
    d = senha % 100 // 10
    u = senha % 10 
    chave = m * 1000 + c * 100 + d * 10 + u
    if chave == 1234:
        igual = 'correta'
    else:
        igual = 'incorreta'
    return igual
def saida(igual):
    print("Senha",igual,'!')
main()