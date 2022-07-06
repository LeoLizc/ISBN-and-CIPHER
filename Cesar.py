#Programa Cesar.

alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def cesar(cadena, n=0, freq='e', cifrar=True):
  '''Retorna la codificación/decodificación bajo el método César de la cadena introducida. Si n==0, entonces el cifrado se hará con base en la frecuencia de las letras. Si no, si cifrar==False, entonces n se tomará como -n para decodificar.'''

  #EJEMPLO (n==0):
  #PXPXKXENVDRUXVTNLXHYMXGMAXYKXJNXGVRFXMAHWGXXWLEHGZXKVBIAXKMXQM

  abc=alfabeto.lower()
  l, cod=len(abc), ""

  if n==0:
    n=abc.find(freq)-abc.find(max_freq(cadena.lower()))

  for char in cadena:
    if char.isupper():
      c2=abc[(abc.find(char.lower())+n)%l].upper()
    elif char.islower():
      c2=abc[(abc.find(char)+n)%l]
    else: c2=char
    cod+=c2
  
  return cod

def max_freq(cadena):
  '''Retorna el caracter con mayor frecuencia dentro de la cadena introducida.'''

  max=0
  letter=""
  d={}
  for char in cadena:
    if char not in d:
      d[char]=0
    d[char]+=1
    
    if d[char]>max:
      max=d[char]
      letter=char;
  
  return letter

# #Lectura
# def cifrar(texto,n):
#   descifrado = ""
#   for l in texto:
#     if not l in alfabeto:
#       descifrado +=l
#       continue
#     pos_letra = alfabeto.index(l)
#     nueva_pos = (pos_letra + n) % len(alfabeto)
#     descifrado += alfabeto[nueva_pos]
#   return descifrado

# def decodificar_cesar_avanzado(texto, freq):
#   texto=texto.upper()
#   frec={}   
#   for car in texto:
#     if not car in alfabeto:
#       continue
#     if not car in frec:
#       frec[car]=0
#     frec[car]+=1
#   ilfrec=alfabeto.index(max(frec, key= lambda k: frec[k]))
#   return decodifcar_cesar(texto,ilfrec-alfabeto.index(freq))

#Programa cesar
# def decodifcar_cesar(texto,n):
#   descifrado = ""

#   for l in texto:
#     if not l in alfabeto:
#       descifrado +=l
#       continue
#     pos_letra = alfabeto.index(l)
#     nueva_pos = (pos_letra - n) % len(alfabeto)
#     descifrado += alfabeto[nueva_pos]
#   return descifrado

