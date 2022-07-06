#Programa ISBN.

import requests
import json

def es_ISBN_13(codigo):
  '''Decide si el código introducido corresponde a un código ISBN 13.'''

  acum=0
  i=1
  for n in codigo:
    n= 10 if n == 'X' else int(n) 
    acum+=n*i
    i= 1 if i==3 else 3
  return acum%10==0

def es_ISBN_10(codigo):
  '''Decide si el código introducido corresponde a un código ISBN 10.'''

  acum=0
  i=1
  for n in codigo:
    n= 10 if n == 'X' else int(n)
    acum+=n*i
    i+=1
  return acum%11==0

def es_ISBN(codigo):
  if not(codigo.isnumeric() or codigo[:-1].isnumeric() and codigo[-1]=='X'):
    return False
  if len(codigo) == 10:
    return es_ISBN_10(codigo)
  elif len(codigo) == 13:
    return es_ISBN_13(codigo)
  return False

#SOLUCIONES------------------------------------------------------------------

#Para usar esta función debe introducir el código ISBN que desea reparar y la posición - 1 donde se encuentra el error
def solucionar_ISBN(codigo, pos):
  '''Retorna el código ISBN hallandoel dígito perteneciente a en la posición pos.'''

  for i in range(10):
    if i==10: i='X'
    n=codigo[:pos]+str(i)
    if pos<len(codigo)-1:
      n+=codigo[pos+1:]
    if es_ISBN(n):
      return n
  return None 

#------------------------  DATABASE  ----------------------------------------
def titulo_ISBN(isbn):
  '''Retorna el título (o, en todo caso, el subtítulo) correspondinte al ISBN introducido. La búsqueda se realiza en la database openlibrary.org. En caso de el ISBN no sea válido o el título no se encuentre, se retornará un mensaje de error.'''

  if not es_ISBN(isbn):
    return 'Error, el código no es ISBN'

  js = requests.get('https://openlibrary.org/isbn/{}.json'.format(isbn))

  if not js.status_code == 200:
    return 'Error, título no encontrado'
    
  js = json.loads(js.text)
  titulo=js['title'] if 'title' in js else js['subtitle']
  return f'"{titulo}"'