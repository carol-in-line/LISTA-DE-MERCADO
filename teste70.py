s = 0
t = 0
mais = 0
menos = 0
barato = ' '
while True:
    nome = str(input('digite o nome do produto :'))
    valor = int(input('digite o val;or do produto :'))
    s += valor
    t +=1
    if valor >= 1000:
        mais += 1
    if t == 1:
        menos = valor 
        barato = nome 
    else: 
        valor < menos
        menos = valor
        barato = nome
    
    c = ' '
    while c not in 'SN':
        c = str(input('quer continuar? [s/n]')).strip().upper()[0]
    if c == 'N':
        break

print(f'o gasto da compra foi R${s} \n a quantidade de produtos com o valor maior q R$1000 foi {mais} \n o produto mais barato foi {barato } e custou {menos}')