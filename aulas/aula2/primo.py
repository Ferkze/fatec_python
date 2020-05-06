# def primo(input):
input = int(input('Digite um número: '))

def primo(input):
    antecessores = list(range(2, input+1))
    for i in antecessores:
        if i == input:
            print('O input', input, 'é primo')
            return True
        if input%i == 0:
            print(input, 'não é primo por ser divisível por', i)
            return False

if primo(input):
    print('Boa, você passou!')