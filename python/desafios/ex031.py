distância = float(input('Digite qual a distância da sua viagem? '))
if distância <= 200:
    opcao1 = distância * 0.50
    print('O preço da sua passagem é R${:.2f}'.format(opcao1))
else:
    opcao2 = distância * 0.45
    print('O preço da sua passagem é R${:.2f}'.format(opcao2))