def menor(a, b):
  if a > b:
     print(f'O valor {b} é menor')
  else:
     print(f'O valor {a} é menor')

a = int(input('informe um valor: '))
b = int(input('Informe outro valor: '))

menor(a, b)