nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format(nome[:6] == 'Silva'))