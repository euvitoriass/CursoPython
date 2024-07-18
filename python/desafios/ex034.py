salário = float(input('Digite seu salário: '))
if salário <= 1.250:
    aumento1 = salário + (salário * 10 / 100)
    print('O aumento do seu salário foi: {:.2f}'.format(aumento1))
else:
    aumento2 = salário + (salário * 15/100)
    print('O aumento do seu salário foi: {:.2f}'.format(aumento2))