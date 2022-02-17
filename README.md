# Learn Python <!-- omit in toc -->

## Tabla de contenido: <!-- omit in toc -->

- [Introducción al Pensamiento Computacional en Python](#introducción-al-pensamiento-computacional-en-python)
  - [Aproximación de Soluciones](#aproximación-de-soluciones)
  - [Búsqueda Binaria](#búsqueda-binaria)
  - [Recursividad](#recursividad)
  - [Argumentos de otras funciones](#argumentos-de-otras-funciones)
  - [Funciones en Expresiones](#funciones-en-expresiones)
  - [Funciones en Estructuras de Datos](#funciones-en-estructuras-de-datos)
  - [Clonación](#clonación)
  - [List Comprehension](#list-comprehension)
  - [Pruebas de Caja Negra](#pruebas-de-caja-negra)
  - [Pruebas de Caja de Cristal](#pruebas-de-caja-de-cristal)
  - [Debugging](#debugging)
    - [Reglas Generales](#reglas-generales)
    - [Diseño de Experimentos](#diseño-de-experimentos)
    - [Errores Comunes](#errores-comunes)
  - [Manejo de Excepciones](#manejo-de-excepciones)
    - [Excepciones Como Control de Flujo](#excepciones-como-control-de-flujo)
  - [Afirmaciones](#afirmaciones)
- [POO](#poo)
  - [Tipos de Datos Abstractos](#tipos-de-datos-abstractos)
  - [Instancias](#instancias)
  - [Decomposición](#decomposición)
  - [Abstracción](#abstracción)

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

### Clonación

- Casi siempre es mejor clonar una lista en vez de mutarla
- Para clonar una lista podemos utilizar rebanadas (slices) o la función `list`

### List Comprehension

- Es una forma concisa de aplicar operaciones a los valores de una secuencia
- También se pueden aplicar condiciones para filtrar

### Pruebas de Caja Negra

- Se basan en la especificación de la función o el programa
- Prueba inputs y valida outputs
- _Unit testing_ o _integration testing_

### Pruebas de Caja de Cristal

- Se basan en el flujo del programa
- Prueba todos los caminos posibles de una función. Ramificaciones, bucles for y while, recursión.
- _Regression testing_ o _mocks_

### Debugging

#### Reglas Generales

- No te molestes con el debugger. Aprende a utilizar el _`print` statement_
- Estudia los datos disponibles
- Utiliza los datos para crear hipótesis y experimentos. Método científico
- Ten una mente abierta. Si entendieras el programa, probablemente no habrían bugs
- Lleva un registro de lo que has tratado, preferentemente en la forma de tests

#### Diseño de Experimentos

- Debugear es un proceso de búsqueda. CAda prueba debe acotar el espacio de búsqueda
- Búsqueda binaria con _`print` statements_

#### Errores Comunes

- Encuentra a los sospechosos comunes
- En lugar de preguntarte por qué un programa no funciona, pregúntate por qué está funcionando de esta manera
- Es posible que el bug no se encuentre donde crees que está
- Explícale el problema a otra persona. De preferencia que no tenga contexto
- Lleva un registro de lo que has tratado, preferentemente en la forma de tests
- Vete a dormir

### Manejo de Excepciones

- Son muy comunes en la programación. No tienen nada de excepcional
- Las excepciones de Python normalmente se relacionan con errores de semántica
- Se pueden crear excepciones propias
- Cuando una excepción no se maneja (unhandled exception), el programa termina en error
- Las excepciones se manejan con los keywords: `try`, `except`, `finally`
- Se pueden utilizar también para ramificar programas
- No deben manejarse de manera silenciosa (por ejemplo, con _`print` statements_)
- Para aventar tu propia excepción utiliza el keyword `raise`

#### Excepciones Como Control de Flujo

**EAFP** (_easier to ask for forgiveness than permission_, _es más fácil pedir perdón que permiso_)

El principio EAFP es un estilo de programación común en Python en el cual se asumen llaves, índices o atributos válidos y se captura la excepción si la suposición resulta ser falsa. Es importante resaltar que otros lenguajes de programación favorecen el principio:

**LBYL** (_look before you leap_, _revisa antes de saltar_)

En el cual el código verifica de manera explícita las precondiciones antes de realizar llamadas.

**Ejemplo:**

```python
# Python

def busca_pais(paises, pais):
    """
    Países es un diccionario. País es la llave.
    Código con el principio EAFP.
    """

    try:
        return paises[pais]
    except KeyError:
        return None
```

```javascript
# Javascript

/**
 * Países es un objeto. País es la llave.
 * Código con el principio LBYL.
 */

function buscaPais(paises, pais) {
  if(!Object.keys(paises).includes(pais)) {
    return null;
  }

  return paises[pais];
}
```

Como puedes ver, el código de Python accede directamente a la llave y únicamente si dicho acceso falla, entonces se captura la excepción y se provee el código necesario. En el caso de JavaScript, se verifica primero que la llave exista en el objeto y únicamente con posterioridad se accede.

Es importante resaltar que ambos estilos pueden utilizarse en Python, pero el estilo EAFP es mucho más "pythonico".

### Afirmaciones

- Programación defensiva
- Pueden utilizarse para verificar que los tipos sean correctos en una función
- También sirven para debuguear

```python
# assert <expresion booleana>, <mensaje de error>

def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'No se permiten str vacíos'

        primeras_letras.append(palabra[0])

    return primeras_letras
```

## POO

### Tipos de Datos Abstractos

- En Python todo es un objeto y tiene un tipo
  - Representación de datos y formas de interactuar con ellos
- Formas de interactuar con un objeto:
  - Creación
  - Manipulación
  - Destrucción
- Ventajas:
  - Decomposición
  - Abstracción
  - Encapsulación

**Ejemplo:**

```python
# Definición de clase

class <nombre_de_la_clase>(<super_clase>):

    def __init__(self, <params>):
        <expresion>

    def <nombre_del_metodo>(self, <params>):
        <expresion>
```

```python
# Definición
class Persona:

    def __init__(self, nombre, edad):
      self.nombre = nombre
      self.edad = edad

    def saluda(self, otra_persona):
      return f'Hola {otra_persona.nombre}, me llamo {self.nombre}.'

# Uso
>>> david = Persona('David', 35)
>>> erika = Persona('Erika', 32)

>>> david.saluda(erika)
'Hola Erika, me llamo David'
```

### Instancias

- Mientras que la clase es un molde, a los objetos creados se les conoce como instancias
- Cuando se crea una instancia, se ejecuta el método `__init__`
- Todos los métodos de una clase reciben implícitamente como primer parámetro `self`
- Los atributos de clase nos permite:
  - Representar datos
  - Procedimientos para interactuar con los mismos (métodos)
  - Mecanismos para esconder la representación interna
- Se accede a los atributos con la notación de punto
- Puede tener atributos privados. Por convención comienzan con _

### Decomposición

- Partir un problema en problemas más pequeños
- Las clases permiten crear mayores abstracciones en forma de componentes
- Cada clase se encarga de una parte del programa se vuelve más fácil de mantener

### Abstracción

- Enfocarnos en la información relevante
- Separar la información central de los secundarios
- Podemos utilizar variables y métodos (privados o públicos)
