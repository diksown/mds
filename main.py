from math import gcd

def shell():
	argumentos = input("mds> ").split()
	if len(argumentos) == 0:
		return [""]
	else:
		return argumentos
	
def socorro(op):
	print()
	print("MDS (Matematica Discreta Simulator) eh um programa interativo")
	print("com funcoes comumente utilizadas no estudo de teoria dos numeros")
	print("e criptografia.")
	print("")
	print("comandos:")
	print("    socorro    (argumentos: nenhum)")
	print("        mostra esse menu aqui")
	print("")
	print("    fatorar    (argumentos: N)")
	print("        fatora o numero N. se ele nao for muito grande, claro")
	print("")
	print("    elevar    (argumentos: A, E, [N])")
	print("        calcula A^E, ou A^E modulo N, caso esse seja dado")
	print("")
	print("    info    (argumentos: nenhum)")
	print("        mostra informacoes sobre o projeto")
	print("")
	print("    sair    (argumentos: nenhum)")
	print("        termina o programa x_X")


def elevar(op):
	if len(op) > 4 or len(op) < 3:
		print("numero de argumentos invalido.")

	for i in op[1:]:
		if not i.isdigit():
			print("apenas inteiros nao-negativos, por favor.")
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
	n = int(op[1])
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
	a, b = int(op[1]), int(op[2])
	print("mdc({a}, {b}) = {gcd(a, b)}")

def info(op):
	print("mds eh um projeto em python3. fique a vontade pra contribuir!")
	print("github.com/diksown/mds")

def sair(op):
	print("== encerrando programa. bons estudos ;) ==")
	exit()

opcoes = {
	"socorro" : socorro, 
	"elevar" : elevar, 
	"fatorar" : fatorar, 
	"mdc" : mdc,
	"info" : info,
	"sair" : sair
}


def main():
	print("bem vindo ao mds - [m]atematica [d]iscreta [s]imulator!")
	print("digite <socorro> pra ver as opcoes disponiveis.")

	while True:
		op = shell()
		if op[0] in opcoes:
			opcoes[op[0]](op)
		else:
			print(f"\"{op[0]}\" nao eh uma operacao valida.")
			print("mande <socorro> pra listar as operacoes.")


if __name__ == "__main__":
	main()
