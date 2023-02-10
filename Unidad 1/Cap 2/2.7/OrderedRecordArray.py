# Implementar una estructura de matriz ordenada de registros
def identity(x): # La función identidad
    return x
class OrderedRecordArray(object):
    def __init__(self, initialSize, key=identity): # Constructor
        self.__a = [None] * initialSize #  La matriz almacenada como una lista
        self.__nItems = 0 # No hay elementos en la matriz inicialmente
        self.__key = key # La función de tecla obtiene la clave de registro
    
    def __len__(self):  # Definición especial para la función len()
        return self.__nItems  # Número de devolución de artículos

    def get(self, n): # Devuelve el valor en el índice n
        if n >= 0 and n < self.__nItems:  # Comprobar si n está dentro de los límites, y
            return self.__a[n] # solo devolver el elemento si está dentro de los límites
        raise IndexError("Index " + str(n) + " is out of range")
    
    def traverse(self, function=print): # Recorrer todos los elementos
        for j in range(self.__nItems):  # y aplicar una función 
           function(self.__a[j])
            
    def __str__(self): # Definición especial para str() func 
        ans = "["  # Rodeado por corchetes
        for i in range(self.__nItems): # Pasar por los elementos
            if len(ans) > 1:# Excepto al lado del corchete izquierdo,
                ans += ", " # elementos separados con coma
            ans += str(self.__a[i]) # Agregar forma de cadena del elemento
        ans += "]" # Cerrar con corchete derecho
        return ans
