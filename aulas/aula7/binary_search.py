def binary_search(lista, valor):
  def search(min, max):
    if min == max: return min
    else:
      meio = int((min+max)/2)
      if valor > lista[meio]:
        return search(meio+1, max)
      else:
        return search(min, meio)

  i = search(0, len(lista)-1)
  if lista[i] == valor:
    print(valor,'encontrado na posicao',i)
  else:
    print(valor,'nao encontrado')

binary_search([1,2,5,6,9,12],3)
binary_search([1,2,5,6,9,12],5)