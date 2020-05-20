def primo(num):
	antecessores = list(range(2, num))
	multiplos = []
	for i in antecessores:
		if i == num:
			return multiplos
		if num % i == 0:
			multiplos.append(i)

	return multiplos

num = int(input('Entre com um número inteiro positivo: '))

multiplos = primo(num)
if len(multiplos) > 0:
	print("{} é multiplo de {}".format(num, ', '.join(str(m) for m in multiplos)))
else:
	print("{} é primo".format(num))
