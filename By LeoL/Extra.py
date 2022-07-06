import ISBN

caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l=len(caracteres)

def menu1():
    print('1. Códigos ISBN')
    print('2. Codificación y descodificación')

def decodificar_cesar(texto, d):
  texto=texto.upper()
  nT=''
  for car in texto:
    if not car in caracteres:
      continue
    nT+=caracteres[(caracteres.index(car)-d)]
  return nT

def codificar_cesar(texto, d):
  texto=texto.upper()
  nT=''
  for car in texto:
    if not car in caracteres:
      continue
    nT+=caracteres[(caracteres.index(car)+d)%l]
  return nT

def decodificar_cesar_avanzado(texto):
  texto=texto.upper()
  frec={}
  for car in texto:
    if not car in caracteres:
      continue
    if not car in frec:
      frec[car]=0
    frec[car]+=1
  ilfrec=caracteres.index(max(frec, key= lambda k: frec[k]))
  return decodificar_cesar(texto,ilfrec-4)

# print(titulo_ISBN(input('Ingrese el ISBN de su libro:\n')))

# print(ISBN.es_ISBN('8498751934'))
# print(ISBN.titulo_ISBN(ISBN.solucionar_ISBN('8398751934',2)))
print(ISBN.solucionar_ISBN('9780321573913',10))
# ese 9 es un 5

def digito_de_control13(codigo):
  suma=0
  i=1
  for dig in codigo:
    suma+=int(dig)*i

    i=3 if(i==1) else 1
    print()
  return (10-suma%10)%10
