EURO_BITCOIN_RATE:float = 44471.78

def sumar_numeros(num1, num2):
    '''Suma los dos numeros proporcionados.'''
    suma = num1 + num2
    return suma

def euros_a_bitcoins(euros: int | float)->float:
  '''Convierte una cantidad de euros a bitcoins. 1 bitcoin = 44570.17 €'''
  bitcoin = euros / EURO_BITCOIN_RATE
  bitcoin = round(bitcoin, 2)
  return bitcoin

def bitcoins_a_euros(usd: int | float) -> float:
  '''Convierte una cantidad de bitcoins a euros. 1 bitcoin = 44570.17 €'''
  euros = usd * EURO_BITCOIN_RATE
  euros = round(euros, 2)
  return euros

def contar_vocales(texto: str)->int:
  '''Devuelve el número de vocales que tiene el texto dado.'''
  vocales = 0
  texto = "".join(texto)
  for x in texto.lower():
    if x in ("a", "e", "i", "o", "u"):
      vocales = vocales + 1
  return vocales

def es_palindromo(texto: str) -> bool:
  '''Detecta si un texto es palíndromo o no'''
  if isinstance(texto,list):
    texto = "".join(texto).lower()
  else:
    texto = texto.replace(" ", "").lower()
  return texto == texto [::-1]

def max_temperaturas (temperaturas: list[float], umbral: float) -> list[float]:
  '''Detecta qué mediciones de temperatura han superado el umbral dado'''
  maximos = []
  for x in temperaturas:
    if x > umbral:
      maximos.append(x)
  return (maximos)


productos: list[str] = []

def insertar(producto: str) -> None:   
  '''Añade un producto a la lista'''
  productos.append(producto)

def borrar(numero: int) -> None:      
  '''Borra el producto en el índice dado de lista de productos.'''
  del productos [numero]

def mostrar_productos() -> None:    
  '''Muestra la lista de productos con sus índices.'''
  indice = -1
  for x in productos:
    indice = productos.index(x)
    print (f"{indice}: {x}")
  if indice == -1:
    print ("No hay productos")

def cantidad() -> int:   
  '''Devuelve el número de productos.'''
  longitud = len(productos)
  if longitud == 0:
    ("No hay productos")
  else:
    return (longitud)


def mostrar_menu():
    print("Menú Interactivo")
    print("-"*30)
    print("convertir euros bitcoins <cantidad>")
    print("convertir bitcoins euros <cantidad>")
    print("contar <texto>")
    print("palindromo <texto>")
    print("temperaturas <varios números separados por comas> <umbral>")
    print("cifrar <texto> <desplazamiento>")
    print("descifrar <texto> <desplazamiento>")
    print("productos")
    print("productos nuevo <nombre>")
    print("productos borrar <índice>")
    print("salir")

def Menu_interactivo():
  while True:
    opcion = input()
    elementos = opcion.split()
    if opcion.startswith("convertir euros bitcoins"):
      print (euros_a_bitcoins(elementos[-1]))

    elif opcion.startswith("convertir bitcoins euros"):
      print(bitcoins_a_euros(elementos [-1]))
    
    elif opcion.startswith("contar"):
      print (contar_vocales(elementos [1:]))
    
    elif opcion.startswith("palindromo"):
      print (es_palindromo(elementos[1:]))
    
    elif opcion.startswith("temperaturas"):
      print (max_temperaturas(elementos[1:-2], elementos [-1]))
    
    elif opcion.startswith("productos"):
      print (mostrar_productos)
    
    elif opcion.startswith("productos nuevo"):
      print (insertar(elementos[-1]))
    
    elif opcion.startswith("productos borrar"):
      print (borrar(elementos[-1]))
    
    elif opcion == "salir":
      print("¡Adiós!")
    
    else:
      print("Comando no reconocido")
