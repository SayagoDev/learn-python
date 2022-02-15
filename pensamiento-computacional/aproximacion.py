objetivo = int(input('Escoge un número: '))

# Margen de error
epsilon = 0.01

# Valor que se irá sumando secuencialmente hasta encontrar la raíz cuadrada
paso = epsilon**2
respuesta = 0.0

# Mientras que respuesta al cuadrado no sea igual al objetivo (con un margen de error epsilon) el while se seguirá ejecutando
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')