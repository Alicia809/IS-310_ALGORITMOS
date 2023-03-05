from PriorityQueue import *

def first(x): return x[0]  # Use first element of item as priority

priority = PriorityQueue(5)
priority.insert(2)
priority.insert(4)
priority.insert(1)
priority.insert(3)
priority.insert(5)
print("Contenido de la PriorityQueue: ", priority)

print("Removing:", priority.remove())
print("Contenido de la PriorityQueue: ", priority)


print("Ultimo elemento de la lista: ", priority.peek())


print("¿La lista esta vacía? ", priority.isEmpty())


print("¿La lista esta llena? ", priority.isFull())
