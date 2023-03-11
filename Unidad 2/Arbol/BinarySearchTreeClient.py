# Automated tests of the BinarySearchTree class

from BinarySearchTree import *
import sys

theTree = BinarySearchTree()
"""print('Created an empty binary search')
"""
# Se definen las claves que se utilizarán para insertar nodos en el árbol
# si se proporcionan argumentos de línea de comando, los utiliza para sobrescribir 
# las claves anteriores.
keys = [47, 22, 30, 68, 15, 46, 52, 83, 78, 86] 
if len(sys.argv) > 1:        # Usar argumentos de línea de comando si están presentes
   keys = [int(a) for a in sys.argv[1:]]

#Se insertan las claves en el árbol utilizando el método insert().
#El segundo argumento de insert() se incrementa en 1 con cada inserción.
count = 0
for key in keys:
   print('Inserción de llave', key, 'en retornos de árboles', 
         theTree.insert(key, count))
   count += 1

# Imprime información sobre el árbol creado, incluyendo el número
# de nodos y el número de niveles.
print('Creó un árbol de búsqueda binaria con', theTree.nodes(), 'nodos a través',
      theTree.levels(), 'niveles')

# Imprime el árbol utilizando el método print() de la clase BinarySearchTree.
theTree.print()

# Obtiene el nodo raíz del árbol utilizando el método root() de la clase
# BinarySearchTree y luego imprime la clave y los datos de dicho nodo.
root_data, root_key = theTree.root()
print('El nodo raíz del árbol tiene clave:', root_key, 'y datos:', root_data)

#Llama al método inOrderTraverse() de la clase BinarySearchTree, que realiza un
# recorrido en orden del árbol y lo imprime utilizando la función de impresión por defecto.
print('Probando el recorrido recursivo en orden usando la función de impresión')
theTree.inOrderTraverse()

# Realiza pruebas de recorrido del árbol utilizando dos generadores de recorrido 
# diferentes (traverse_rec y traverse) para cada uno de los tres órdenes de 
# recorrido (pre, in y post). Para cada recorrido, se imprime cada clave y sus datos. 
# También se prueba el manejo
for func in (theTree.traverse_rec, theTree.traverse):
   print('Usando {}generador transversal recursivo'.format(
      '' if func == theTree.traverse_rec else 'non-'))
   for order in ['pre', 'in', 'post']:
      print(' Atravesando el árbol usando', order, 'order')
      print()
      for key, data in func(order):
         print(' {' + str(key) + ', ' + str(data) + '}', end='')
      print()
