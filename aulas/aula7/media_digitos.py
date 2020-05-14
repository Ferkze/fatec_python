def media_digitos(n):
  'Media dos dígitos de um número inteiro'
  def soma_digitos(n):
    nums_str = str(n)
    if len(nums_str) == 1:
      return int(n)
    else:
      return int(nums_str[0]) + soma_digitos(nums_str[1:])
  return soma_digitos(n) / len(str(n))

print(media_digitos(1234))
