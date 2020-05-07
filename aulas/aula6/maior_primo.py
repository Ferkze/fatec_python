input = int(input("Digite um número: "))

def maior_primo(max=0):
  "Retorna o maior número primo passado até o valor do argumento"

  def primo(input):
    "Verifica se o argumento passado é um número primo"
    antecessores = list(range(2, input+1))
    for i in antecessores:
      if i == input:
        return True
      if input%i == 0:
        return False

  if max <= 2:
    return
  for i in range(3, max+1):
    val = max - i + 3
    if primo(val):
      return val

print(maior_primo(input))
