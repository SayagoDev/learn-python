def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]

    return divisors


def run():
    num = input('Ingrese un número: ')
    assert num.isnumeric(), "Debes ingresar un número entero positivo"
    print(divisors(int(num)))
    print("Terminó mi programa")


if __name__ == '__main__':
    run()