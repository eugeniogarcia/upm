EURO_BITCOIN_RATE = 44471.78

def sumar_numeros(num1, num2):
    '''Suma los dos numeros proporcionados.'''
    suma = num1 + num2
    return suma

def euros_a_bitcoins(euros: int | float):
  '''Convierte una cantidad de euros a bitcoins. 1 bitcoin = 44570.17 €'''
  bitcoin = euros / 44471.78
  bitcoin = round(bitcoin, 2)
  return bitcoin

def bitcoins_a_euros(usd: int | float) -> int | float:
  '''Convierte una cantidad de bitcoins a euros. 1 bitcoin = 44570.17 €'''
  euros = usd * 44471.78
  euros = round(euros, 2)
  return euros

def contar_vocales(texto: str):
  '''Devuelve el número de vocales que tiene el texto dado.'''
  vocales = 0
  texto.lower()
  for x in texto:
    if x in ("a", "e", "i", "o", "U"):
      vocales = vocales + 1
  return vocales

def es_palindromo(texto: str):
  '''Detecta si un texto es palíndromo o no'''
  texto.replace (" ", "")
  texto.lower()
  texto = texto [::-1]

  print (texto)

def max_temperaturas (temperaturas: list[float], umbral: float) -> list[float]:
  '''Detecta qué mediciones de temperatura han superado el umbral dado'''
  maximos = []
  for x in temperaturas:
    if x > umbral:
      maximos = maximos.append(x)
  print (maximos)


productos: list[str] = []

def insertar(producto: str) -> None:   
  '''Añade un producto a la lista'''
  productos.append(producto)

def borrar(numero: int) -> None:      
  '''Borra el producto en el índice dado de lista de productos.'''
  del productos [numero]

def mostrar_productos() -> None:    
  '''Muestra la lista de productos con sus índices.'''
  for x in productos:
    indice = productos.index(x)
    print("{indice}: {x}")

def cantidad() -> int:   
  '''Devuelve el número de productos.'''
  longitud = len(productos)
  print (longitud)