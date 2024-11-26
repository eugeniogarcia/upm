### 2. Ordenación de la lista de la compra
Para ello, vamos a utilizar un algoritmo de ordenación conocido como Insertion Sort<sup>[2](#insertion_sort)</sup>, que comparará la prioridad de cada artículo y los colocará en el orden adecuado.
El criterio de ordenación será el siguiente: un producto ha de aparecer antes que otro si su prioridad es **mayor**, o si el primer producto no ha sido comprado y el segundo sí.


### 4. Refactorización del código
``listadelacompra_clases.py`` en el que crearemos dos clases (``ListaCompra`` y ``Producto``) que agruparán las funciones desarrolladas anteriormente. 

La clase ``Producto`` ha de tener un constructor que reciba todos los parámetros necesarios para la creación de un producto (``nombre``, ``precio``, ``categorias``, ``etiquetas``, ``prioridad``), y los inicialice como atributos. Considere qué puede haber parámetros opcionales, decida cuáles podrían ser y qué valor por defecto deberían tener. Además, debe inicializar el atributo ``comprado`` a False.

La clase ``ListaCompra`` debe contener un constructor que inicialice su único atributo: ``productos`` (una lista de objetos de la clase ``Producto``). Además, debe contener todos los métodos necesarios para realizar las operaciones: ``insertar``, ``borrar``, ``actualizar_precio``, ``ordenar``,  ``cambiar_estado`` y ``mostrar_productos``, con sus respectivos parámetros.

Por último, el menú deberá operar con ambas clases en lugar de llamar directamente a las funciones desarrolladas en los puntos anteriores.

Este último punto del proyecto 2 es **obligatorio** para considerar terminado el proyecto 2. Es decir, que es necesario para su evaluación en el examen práctico. En otras palabras, aunque se realice la primera parte (sin clases) en el fichero ``listadelacompra.py``; se debe completar este úlitmo punto y desarrollar también la versión usando las clases ``ListaCompra`` y ``Producto`` en el fichero ``listadelacompra_clases.py``.

### 5. Tareas opcionales

Como hemos dicho, hemos realizado una gestión muy básica de la lista de la compra. Por ello, se propone realizar
libremente las siguientes tareas para mejorar en el manejo de Python y obtener una gestión de lista de la compra más
útil:

- Permitir varias listas de la compra.
  Con la clase ``ListaCompra`` puede crear tantos objetos como listas de la compra necesite (para diferentes supermercados o diferentes temáticas). Por lo que puede hacer que el menú permita la creación y el uso de diferentes listas.
- Modificar el menú para que los argumentos se pidan uno a uno de manera interactiva, en lugar de escribirlos con separadores en la misma lı́nea.
 - Mostrar el ı́ndice de cada producto. Borrar o cambiar un producto requiere saber el ı́ndice del producto en la lista.
 Serı́a útil que se mostrara el ı́ndice de cada producto junto con el resto de información.
 Existen varios enfoques para lograrlo.
 Una opción es incluir el ı́ndice en el producto, igual que hemos hecho con el resto de información, pero eso requiere modificar muchas partes del código.
 Una opción más elegante es usar la función `enumerate`, que además permite recorrer una lista (cualquier iterable) y devuelve uno a uno los elementos y su ı́ndice.
- Añadir una función que permita borrar o modificar productos por nombre en vez de por índice.
