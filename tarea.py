A=["for","if","else","int","while","string","char","return", ]
def analizar_token(cadena):
	cadena = cadena.strip()
	if not cadena:
		return "Cadena vacía"
	estado = 0
	a=""
	i = 0
	while i < len(cadena):
		c = cadena[i]
		if estado == 0:
			if c.isalpha() or c == '_':
				estado = 1 # Estado para Identificador
				a=c
			elif c.isdigit():
				estado = 2 # Estado para Número (Entero)
		elif estado == 1: # Procesando Identificador
			if not (c.isalnum() or c == '_'):
				return "Identificador no válido"
			else:
				a=a+c
		elif estado == 2: # Procesando Número
			if c == '.':
				estado = 3 # Transición a número decimal
		elif not c.isdigit():
			return "Número no válido"
		elif estado == 3: # Procesando parte decimal
			if not c.isdigit():
				return "Número decimal no válido"
		i += 1
	# Clasificación final según el estado en el que terminó
	if estado == 1 and a in A:
		return "Palabra reservada valido"
	elif estado in (2, 3):
		return "Número válido"
	return "Cadena no válida"
# --- Pruebas ---
entradas = ["jklsadfjlsadjf", "45.67", "for", "if", "ekse", "xd"]
for e in entradas:
	print(f"'{e}' -> {analizar_token(e)}")
