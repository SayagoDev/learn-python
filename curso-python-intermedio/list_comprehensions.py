def run():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    challenge = [i for i in range(1, 10000) if i % 36 == 0]  # 36 múltiplo de 4, 6 y 9

    print(squares)
    print(challenge)


if __name__ == '__main__':
    run()