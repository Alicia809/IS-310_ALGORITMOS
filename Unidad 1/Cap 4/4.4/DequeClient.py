# importar la clase Deque
from Deque import Deque

# crear un objeto Deque con tamaño 5
d = Deque(5)

print('Capacidad inicial de la Deque: 5')

# insertar elementos por la derecha
print('Insertar elementos por la derecha')
d.insertRight(1)
d.insertRight(2)
d.insertRight(3)
d.printDeque()

# insertar elementos por la izquierda
print('Insertar elementos por la izquierda')
d.insertLeft(4)
d.insertLeft(5)
d.printDeque()

#Insertar mas elementos de los que permite
print('Insertar mas elementos de los que permite por la derecha', d.insertRight(6))
d.printDeque()
print('Insertar mas elementos de los que permite por la izquierda', d.insertLeft(0))
d.printDeque()

# Remover elementos
print('Remover elemento por la derecha')
d.removeRight()
d.printDeque()
print('Remover elemento por la izquierda')
d.removeLeft()
d.printDeque()


# Mostrar los elementos de los extremo
print('Elemento más a la derecha', d.peekRight())
print('Elemento más a la izquierda', d.peekLeft())

# Comprobar estado de la Deque
print('¿La dequesta vacia? ', d.isEmpty())
print('¿La dequesta llena? ', d.isFull())