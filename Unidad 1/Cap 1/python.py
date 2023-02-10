"""Escriba una comprensión de lista de Python que devuelva los caracteres 
individuales de una cadena que no sean caracteres de espacio en blanco. Aplíquelo a la 
cadena '4 y 20 mirlos.\n'"""

lista = [c for c in '4 and 20 blackbirds.\n' if c.strip() ]
print(lista)