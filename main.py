from math import gcd

def shell():
	argumentos = input("mds> ").split()
	if len(argumentos) == 0:
		return [""]
	else:
		return argumentos

	
def socorro(op):
	print()
	print("mds ([m]atematica [d]iscreta [s]imulator) eh uma shell interativa")
	print("com funcoes comumente utilizadas no estudo de teoria dos numeros")
	print("e criptografia.")
	print("")
	print("comandos:")
	print("    socorro [scr]    (argumentos: nenhum)")
	print("        mostra (esse) menu de ajuda")
	print("")
	print("    elevar [ele]    (argumentos: A, E, [N])")
	print("        calcula A^E, ou A^E modulo N, caso esse seja dado")
	print("")
	print("    fatorar [fat]    (argumentos: N)")
	print("        fatora o numero N. (se ele nao for muito grande, claro)")
	print("")
	print("    mdc    (argumentos: A, B)")
	print("        calcula o mdc entre A e B")
	print("")
	print("    info    (argumentos: nenhum)")
	print("        mostra informacoes sobre o projeto")
	print("")
	print("    sair    (argumentos: nenhum)")
	print("        termina o programa x_X")


def elevar(op):
	if len(op) > 4 or len(op) < 3:
		print("numero de argumentos invalido.")
		return

	for i in op[1:]:
		if not i.isdigit():
			print("use apenas inteiros nao-negativos")
			return

	if len(op) == 3:
		a, e = map(int, op[1:])
		print(f"{a}^{e} = {pow(a, e)}")

	elif len(op) == 4:
		a, e, n = map(int, op[1:])
		if n == 0:
			print("o modulo precisa ser >0.")
			return
		print(f"{a}^{e} (mod {n}) = {pow(a, e, n)}")


def fatorar(op):
	if len(op) != 2:
		print("numero de argumentos invalido.")
		return 

	if not op[1].isdigit() or int(op[1]) <= 1:
		print("o numero precisa ser um inteiro >1.")
		return

	n = int(op[1])

	if n > 10**14:
		print("esse numero eh muito grande pra ser fatorado.")
		return

	i = 2
	div = []
	while i*i <= n:
		while n % i == 0:
			div.append(i)
			n //= i
		i += 1
	if n > 1:
		div.append(n)

	div.sort()
	div = list(map(str, div))
	n = int(op[1])
	print(f"{n} = {'*'.join(div)}")


def mdc(op):
	if len(op) != 3:
		print("numero de argumentos invalido.")
		return

	a, b = op[1], op[2]
	if not a.isdigit() or not b.isdigit() or int(a) == 0 or int(b) == 0:
		print("os argumentos precisam ser dois inteiros positivos.")
		return

	a, b = int(a), int(b)
	print(f"mdc({a}, {b}) = {gcd(a, b)}")
	

def info(op):
	print("mds eh um projeto em python3 mantido por @diksown no github.")
	print("fique a vontade pra contribuir!")
	print("github.com/diksown/mds")


def sair(op):
	print("==] encerrando programa. bons estudos ;) [==")
	exit()


def main():
	print("[mds] -  digite <socorro> ou <info> para mais informacoes.")

	opcoes = {
		"socorro" : socorro, 
		"scr" : socorro,
		"elevar" : elevar, 
		"ele" : elevar,
		"fatorar" : fatorar, 
		"fat": fatorar,
		"mdc" : mdc,
		"info" : info,
		"sair" : sair
	}

	while True:
		op = shell()
		if op[0] in opcoes:
			opcoes[op[0]](op)
		else:
			print(f"\"{op[0]}\" nao eh uma operacao valida.")
			print("mande <socorro> pra listar as operacoes.")


if __name__ == "__main__":
	main()
