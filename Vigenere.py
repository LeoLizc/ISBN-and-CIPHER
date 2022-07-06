#Programa Vigenère.

import Cesar

def vigenere(texto, clave, cifrar=True):
  '''Retorna la codificación/decodificación bajo el método Vigenère con la cadena y clave introducidas. Si cifrar==True, entonces el método codifica; caso contrario, decodifica.'''

  #EJEMPLO:
  #codigos + queso = sihauem

  abc=Cesar.alfabeto.lower()
  l, c, cod, s, clave = len(abc), len(clave), "", 1 if cifrar else -1, clave.lower()
  
  i=0
  for char in texto:
    
    if char.lower() in abc:
      if char.isupper():
        c2=abc[(abc.find(char.lower())+s*abc.find(clave[(i%c)]))%l].upper()
      elif char.islower():
        c2=abc[(abc.find(char)+s*abc.find(clave[i%c]))%l]
      i=i+1
    else:
      c2=char
    
    cod+=c2
  
  return cod

#def cifrar_vigenere(texto, clave):
#  texto=texto.upper()
#  nT=''
#  i=-1
#  for car in texto:
#    i=(i+1)%len(clave)
#    if not (car in Cesar.alfabeto and clave[i] in Cesar.alfabeto):
#      nT+=car
#      continue
#    ni = (Cesar.alfabeto.index(car) + Cesar.alfabeto.index(clave[i]))%len(Cesar.alfabeto)
#
#    nT+=Cesar.alfabeto[ni]
#  return nT


#def descifrar_vigenere(texto, clave):
#  texto=texto.upper()
#  nT=''
#  i=-1
#  for car in texto:
#    i=(i+1)%len(clave)
#    if not (car in Cesar.alfabeto and clave[i] in Cesar.alfabeto):
#      nT+=car
#      continue
#    ni = Cesar.alfabeto.index(car) - Cesar.alfabeto.index(clave[i])
#
#    nT+=Cesar.alfabeto[ni]
#  return nT
