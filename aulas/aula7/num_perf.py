def num_perf(n):
  'Checa se o número é perfeito, ou seja, igual a soma de todos seus divisores exceto ele próprio'
  def sum_divisors(a,b):
    if b == 1:
      return 1
    elif a == b or a % b != 0:
      return sum_divisors(a, b-1)
    elif a % b == 0:
      return b + sum_divisors(a, b-1)

  sum = sum_divisors(n, n-1)
  return sum == n
  
print(num_perf(6))
print(num_perf(5))
