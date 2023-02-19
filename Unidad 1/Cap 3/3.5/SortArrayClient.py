from SortArray import *
import random
import timeit

def initArray(size=10, maxValue=100, seed=3.14159):
    """Create an Array of the specified size with a fixed sequence of
       'random' elements"""
    arr = Array(size)                   # Create the Array object
    random.seed(seed)                   # Set random number generator
    for i in range(size):               # to known state, then loop
        arr.insert(random.randrange(maxValue)) # Insert random numbers
    return arr                          # Return the filled Array

arr = initArray()
print("Array containing", len(arr), "items:\n", arr)

for test in ['initArray().bubbleSort()',
             'initArray().selectionSort()',
             'initArray().insertionSort()']:
    elapsed = timeit.timeit(test, number=10, globals=globals())
    print(test, "took", elapsed, "seconds", flush=True)

#InsertionSort2 con datos desordenados
print('\nInsertionSort2 con datos desordenados:')
arr.traverse()
arr.insertionSort2()
print('La matriz ordenada contiene:\n', arr)

#InsertionSort2 con una matriz inversamente ordenada
maxSize2 = 10 # Tamaño máximo de la matriz
arr2 = Array(maxSize2) # Crear un objeto de matriz
arr2.insert(10) #  Insertar 10 elementos
arr2.insert(10)
arr2.insert(9)
arr2.insert(8)
arr2.insert(8)
arr2.insert(5)
arr2.insert(4)
arr2.insert(4)
arr2.insert(2)
arr2.insert(1)
print('\nInsertionSort2 con datos ordenados inversamente:')
arr2.traverse()
arr2.insertionSort2()
print('La matriz ordenada contiene:\n', arr2)

#InsertionSort2 con una matriz casi ordenada
maxSize3 = 10 # Tamaño máximo de la matriz
arr3 = Array(maxSize3)
arr3.insert(1) #  Insertar 10 elementos
arr3.insert(2)
arr3.insert(4)
arr3.insert(5)
arr3.insert(4)
arr3.insert(8)
arr3.insert(8)
arr3.insert(9)
arr3.insert(10)
arr3.insert(10)
print('\nInsertionSort2 con datos casi ordenados:')
arr3.traverse()
arr3.insertionSort2()
print('La matriz ordenada contiene:\n', arr3)
print('\n***Este algoritmo es muy eficiente para los datos casi ordenados***\n')