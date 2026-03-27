# Os dois últimos dígitos de um CPF são validadores.
# Indicam se um CPF é válido ou não.
# Existe um algoritmo que faz essa verificação. Pesquise na internet.


def __validar_cpf(self, cpf_teste):
	somatorio_valida_ultimo = 0
	somatorio_valida_penultimo = 0
	ultimo = cpf_teste % 10
	cpf_teste //= 10
	penultimo = cpf_teste % 10
	cpf_teste //= 10
	somatorio_valida_ultimo = penultimo * 2
	for i in range(2, 12):
		modulo = cpf_teste % 10
		cpf_teste //= 10
		somatorio_valida_penultimo += modulo * i
		somatorio_valida_ultimo += modulo * (i + 1)
	modulo = somatorio_valida_penultimo % 11
	if modulo < 2:
		if penultimo != 0:
			return False # CPF inválido
	else:
		if penultimo != 11 - modulo:
			return False # CPF inválido
	modulo = somatorio_valida_ultimo % 11
	if modulo < 2:
		if ultimo != 0:
			return False # CPF inválido
	else:
		if ultimo != 11 - modulo:
			return False # CPF inválido
	return True # CPF válido