from SortArray import *
from google.oauth2.credentials import Credentials
#importa la clase Credentials del módulo oauth2, que se utiliza para proporcionar 
# las credenciales necesarias para acceder a la API de Google.
from googleapiclient.discovery import build
#importa la función build del módulo discovery, que se utiliza para crear una instancia 
# de una API de Google. Esto se hace pasando el nombre de la API y la versión que se desea 
# utilizar, así como las credenciales que se utilizarán para acceder a la API.
from google.oauth2 import service_account
#importa la clase service_account del módulo oauth2, que se utiliza para crear una instancia 
# de las credenciales de la cuenta de servicio de Google. Las cuentas de servicio son una forma 
# de proporcionar autenticación a una aplicación de manera programática, sin tener que utilizar 
# las credenciales de un usuario real.
import random
import timeit

#Para sincronizar con Google sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
#La variable SCOPES define el nivel de acceso que se otorga a 
# la aplicación para acceder a la hoja de cálculo de Google. 
# Leer y escribir en este caso
KEY = 'key.json'
#La variable KEY hace referencia al archivo JSON que contiene las 
# credenciales de la cuenta de servicio de Google necesarias para 
# acceder a la hoja de cálculo de Google.
SPREADSHEET_ID = '1viP68Q68jmTvwV5GjjhmzZRUSUKksUx1LsG78AiImaQ'
#La variable SPREADSHEET_ID hace referencia al ID de la hoja de cálculo 
# de Google con la que se quiere sincronizar.

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

def initArray(size=4, maxValue=100, seed=3.14159):
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
    elapsed = timeit.timeit(test, number=4, globals=globals())
    print(test, "took", elapsed, "seconds", flush=True)


#LISTA NORMAL
arr.traverse()
print('La matriz desordenada contiene:\n', arr)

# Convertir el arreglo a una lista de listas con un elemento por sublista
values = [[arr.get(i)] for i in range(len(arr))]

# Especificar la dirección de la celda para cada valor
range_ ='A2:A'

# Borrar los datos previos en el rango especificado
sheet.values().clear(spreadsheetId=SPREADSHEET_ID, range=range_).execute()

# Llamamos a la api para insertar los valores
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range=range_,
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente.\n{(result.get('updates').get('updatedCells'))}")



#BUBBLE
arr.bubbleSort()
print('La matriz ordenada por bubbleSort contiene:\n', arr)

# Convertir el arreglo a una lista de listas con un elemento por sublista
values = [[arr.get(i)] for i in range(len(arr))]

# Especificar la dirección de la celda para cada valor
range2_ ='B2:B'

# Borrar los datos previos en el rango especificado
sheet.values().clear(spreadsheetId=SPREADSHEET_ID, range=range2_).execute()

# Llamamos a la api para insertar los valores
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range=range2_,
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente.\n{(result.get('updates').get('updatedCells'))}")



#SELECTION
arr.selectionSort()
print('La matriz ordenada por selectionSort contiene:\n', arr)

# Convertir el arreglo a una lista de listas con un elemento por sublista
values = [[arr.get(i)] for i in range(len(arr))]

# Especificar la dirección de la celda para cada valor
range3_ ='C2:C'

# Borrar los datos previos en el rango especificado
sheet.values().clear(spreadsheetId=SPREADSHEET_ID, range=range3_).execute()

# Llamamos a la api para insertar los valores
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range=range3_,
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente.\n{(result.get('updates').get('updatedCells'))}")



#INSERTION
arr.insertionSort()
print('La matriz ordenada por nsertionSort contiene:\n', arr)

# Convertir el arreglo a una lista de listas con un elemento por sublista
values = [[arr.get(i)] for i in range(len(arr))]

# Especificar la dirección de la celda para cada valor
range4_ ='D2:D'

# Borrar los datos previos en el rango especificado
sheet.values().clear(spreadsheetId=SPREADSHEET_ID, range=range4_).execute()

# Llamamos a la api para insertar los valores
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range=range4_,
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente.\n{(result.get('updates').get('updatedCells'))}")


