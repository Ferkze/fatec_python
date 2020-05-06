char = input("Digite uma letra: ")

def vogal(c):
  "Checa se o caractere é uma vogal"
  return c in "AEIOUaeiou"

print(vogal(char))
