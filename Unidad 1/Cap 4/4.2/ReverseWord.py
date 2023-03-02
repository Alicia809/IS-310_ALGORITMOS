# Un programa para invertir las letras de una frase o palabra
import re
from SimpleStack import *
# El módulo re de Python para eliminar cualquier espacio en blanco, 
# puntuación o carácter especial de la cadena original y compararla con su reverso.
stack = Stack(100)          # Create a stack to hold letters

word = input("Word to reverse: ")

for letter in word:         # Loop over letters in word
   if not stack.isFull():   # Push letters on stack if not full
      stack.push(letter)
    
reverse = ''                # Build the reversed version
while not stack.isEmpty():  # by popping the stack until empty
   reverse += stack.pop()

print('El reverso de', word, 'es', reverse)
word2 = re.sub('[^\w]', '', word.lower())
reverse2 = re.sub('[^\w]', '', reverse.lower())

print('Ignorando espacios y puntuacion:')
print('El reverso de', word, 'es', reverse2)
if word2 == reverse2:
   print('La cadena es un palindromo')
else :
   print('La cadena NO es un palindromo')

#Frases palindromo para probar el programa:
#A man, a plan, a canal, Panama.
# Luz azul
# Ateo poco poeta 