# Learn Python <!-- omit in toc -->

## Tabla de contenido: <!-- omit in toc -->

- [Introducción al Pensamiento Computacional en Python](#introducción-al-pensamiento-computacional-en-python)
  - [Aproximación de Soluciones](#aproximación-de-soluciones)
  - [Búsqueda Binaria](#búsqueda-binaria)
  - [Recursividad](#recursividad)
  - [Argumentos de otras funciones](#argumentos-de-otras-funciones)
  - [Funciones en Expresiones](#funciones-en-expresiones)
  - [Funciones en Estructuras de Datos](#funciones-en-estructuras-de-datos)

## Introducción al Pensamiento Computacional en Python

```python
# <literales> = 1, 'abc', 2.0 True
# <operadores> = + / * % ** = ==
# <literal> <operador> <literal>

# <objeto> <operador> <objeto> # expresión
# >>> valor

>>> 1 + 2
>>> 1 3.0 # error sintáctico
>>> 5 / 'Platzi' # error semántico estático
>>> 5 * 'Platzi'

# statement o enunciado
>>> print('hello, Platzi!')
```

### Aproximación de Soluciones

- Similar a enumeración exhaustiva, pero no necesita una respuesta exacta
- Podemos aproximar soluciones con un margen de error que llamaremos epsilon

### Búsqueda Binaria

- Cuando la respuesta se encuentra en un conjunto ordenado, podemos utilizar búsqueda binaria
- Es altamente eficiente, pues corta el espacio de búsqueda en dos por cada iteración

### Recursividad

- Algorítmica: Una forma de crear soluciones utilizando el principio de "divide y vencerás"
- Programática: Una técnica programática mediante la cual una función se llama a sí misma

### Argumentos de otras funciones

Las funciones también pueden recibir funciones como argumentos para crear abstracciones más poderosas.

```python
def multiplicar_por_dos(n):
  return n * 2


def aplicar_operacion(f, numeros):
  resultados = []
  for numero in numeros:
    resultado = f(numero)
    resultado.append(resultado)

>>> nums = [1, 2, 3]
>>> aplicar_operaciones(multiplicar_por_dos, nums)
[2, 4, 6]
```

### Funciones en Expresiones

Una forma de definir una función en una expresión es utilizando el keyword `lambda`. lambda tiene la siguiente sintaxis: `lambda <vars>: <expresion>`.

Otro ejemplo interesante es que las funciones se pueden utilizar en una expresión directamente. Esto es posible ya que como lo hemos platicado con anterioridad, en Python las variables son simplemente nombres que apuntan a un objeto (en este caso a una función).

```python
sumar = lambda x, y: x + y

>>> sumar(2, 3)
5
```

### Funciones en Estructuras de Datos

Las funciones también se pueden incluir en diversas estructuras que las permiten almacenar. Por ejemplo, una lista puede guardar diversas funciones a aplicar o un diccionario las puede almacenar como valores.

```python
def aplicar_operaciones(num):
    operaciones = [abs, float]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))

    return resultado

>>> aplicar_operaciones(-2)
[2, -2.0]
```