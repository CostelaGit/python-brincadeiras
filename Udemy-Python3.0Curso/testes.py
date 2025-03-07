# função q multiplica argumentos não nomeados

def multiplica(x,y):
    x = x*y
    return x

a = float(input('digite o numero a ser multiplicado: '))
b = float(input('digite o por quanto ele será multiplicado: '))

c = multiplica(a, b)

print(f'{c} é a multiplicação de {a} por {b}')