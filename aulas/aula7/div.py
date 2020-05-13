def div(m,n):
  if n > m:
    return 0
  elif n == m:
    return 1
  else:
    return 1 + div(m-n,n)

print(div(7,2))
print(div(3,4))
