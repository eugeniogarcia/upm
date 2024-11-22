EURO_BITCOIN_RATE:float = 44471.78

def sumar_numeros(num1, num2):
    '''Suma los dos numeros proporcionados.'''
    suma = num1 + num2
    return suma

def euros_a_bitcoins(euros: int | float)->float:
  '''Convierte una cantidad de euros a bitcoins. 1 bitcoin = 44570.17 €'''
  bitcoin = euros / EURO_BITCOIN_RATE
  bitcoin = round(bitcoin, 2) #posible error
  return bitcoin #simplificar

def bitcoins_a_euros(usd: int | float) -> float:
  '''Convierte una cantidad de bitcoins a euros. 1 bitcoin = 44570.17 €'''
  euros = usd * EURO_BITCOIN_RATE
  euros = round(euros, 2)
  return euros #simplificar

def contar_vocales(texto: str)->int:
  '''Devuelve el número de vocales que tiene el texto dado.'''
  vocales = 0
  texto.lower() #error 1
  for x in texto:
    if x in ("a", "e", "i", "o", "U"): #error 2
      vocales = vocales + 1
  return vocales

def es_palindromo(texto: str)->bool:
  '''Detecta si un texto es palíndromo o no'''
  texto.replace (" ", "") #error3
  texto.lower()
  return texto == texto [::-1]

def max_temperaturas (temperaturas: list[float], umbral: float) -> list[float]:
  '''Detecta qué mediciones de temperatura han superado el umbral dado'''
  maximos = []
  for x in temperaturas:
    if x > umbral:
      maximos = maximos.append(x) #error 4
  return maximos

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
    print("{indice}: {x}") #error4
  #error 5
  #posible optimizacion

def cantidad() -> int:   
  '''Devuelve el número de productos.'''
  return len(productos)

if __name__== "__main__":
  print(f"El resultado de convertir es: {bitcoins_a_euros(23)}")
