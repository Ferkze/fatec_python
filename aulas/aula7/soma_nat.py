def soma_nat(n):
  if n == 1:
    return n
  else:
    return n + soma_nat(n-1)

print(soma_nat(5))
