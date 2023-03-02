from SimpleStack import *

# a) para tratar de algo se colocar en una pila completa
"""
stack = Stack(5)

for word in ['May', 'the', 'force', 'be', 'with', 'you']:
   stack.push(word)

print('Después de empujar', len(stack), 
      'palabras en la pila, contiene:\n', stack)
print('¿Está llena la pila?', stack.isFull())
"""

# b) para tratar de extraer de una pila vacía.
"""stack = Stack(10)
#agregar elementos:
stack.push(4)
stack.push(22)
stack.push(17)

print('¿Está llena la pila?', stack.isFull())

print('Sacar elementos de la pila:')
while not stack.isEmpty():
   item = stack.pop()
   print(item, end=' ')

print('\n¿Está vacía la pila?', stack.isEmpty())

print('Tratar de sacar de una pila vacía:')
item = stack.pop()
"""

#Codigo original
"""
stack = Stack(10)
for word in ['May', 'the', 'force', 'be', 'with', 'you']:
   stack.push(word)

print('Después de empujar', len(stack), 
      'palabras en la pila, contiene:\n', stack)
print('¿Está llena la pila?', stack.isFull())

print('Sacar elementos de la pila:')
while not stack.isEmpty():
   print(stack.pop(), end=' ')
print()"""
