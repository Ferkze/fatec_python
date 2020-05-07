def maximo(*valores):
  "Retorna maior valor numérico passado nos argumentos"
  max = valores[0]
  for val in valores:
    if max <= val:
      max = val
  return max

print(maximo(3,4,1))
print(maximo(0,-1,-5))
