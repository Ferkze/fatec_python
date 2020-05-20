def pascal(linhas):
  arr = [[0 for x in range(linhas)]  for y in range(linhas)]  

  for linha in range (0, linhas):
    for i in range (0, linha + 1):
      if (i == 0 or i == linha):
        arr[linha][i] = 1
        print(arr[linha][i], end = " ")
      else:
        arr[linha][i] = (arr[linha - 1][i - 1] + arr[linha - 1][i])
        print(arr[linha][i], end = " ")

    print("\n", end = "") 

linhas = int(input("Quantas linhas? "))
pascal(linhas)
