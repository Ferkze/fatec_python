def maximo(*valores):
  "Retorna maior valor numérico passado nos argumentos"
  max = valores[0]
  for val in valores:
    if max <= val:
      max = val
  return max

print(maximo(1,2,3,4,5,6,7,2,3,5,3,10,2,4,1,0))