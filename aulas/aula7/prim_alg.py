def prim_alg(n):
  'Primeiro algarismo de um número inteiro'
  if n < 10: return n
  else: return int(prim_alg(n/10))

print(prim_alg(5629))
print(prim_alg(7))
