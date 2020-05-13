def fibonacci_recursive(n):
  if n == 1: return 0
  elif n == 2: return 1
  else: return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

for i in range(1,11):
  print(fibonacci_recursive(i), end=',')