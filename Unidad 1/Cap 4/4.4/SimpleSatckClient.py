# importar la clase stackeque
from SimpleStack import Stack

# Crear un objeto stackeque con tamaño 5
stack = Stack(5)

# Insertar elementos por la derecha
stack.insertRight(1)
stack.insertRight(2)
stack.insertRight(3)
print('Insertar elementos por la derecha')
print('Elementos: ', stack.printDeque())

# Insertar elementos por la izquierda
stack.insertLeft(4)
stack.insertLeft(5)
print('Insertar elementos por la izquierda')
print('Elementos: ', len(stack))

#Insertar mas elementos de los que permite
print('Insertar mas elementos de los que permite')
#Por derecha:
stack.insertRight(6)
print('Elemento por la derecha: ', len(stack))
#Por izquierda:
stack.insertLeft(0)
print('Elemento por la izquierda: ', len(stack))

# Remover elementos por la derecha
stack.removeRight()
print('Remover elemento por la derecha: ', len(stack))
# Remover elementos por la izquierda
stack.removeLeft()
print('Remover elemento por la izquierda: ', len(stack))

#stackevuelve el elemento más a la derecha
print('Elemento mas a la derecha: ', stack.peekRight())
#stackevuelve el elemento más a la izquierda
print('Elemento mas a la izquierda: ', stack.peekLeft())

#Verificar si stackeque esta llena
print('¿Deque esta llena? : ', stack.disFull())
#Verificar si stackeque esta vacia
print('¿Deque esta vacia? : ', stack.disEmpty())