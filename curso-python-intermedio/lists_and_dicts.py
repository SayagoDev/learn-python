def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Saúl", "lastname": "Sáyago"}

    super_list = [
        {"firstname": "Saúl", "lastname": "Sáyago"},
        {"firstname": "Carlos", "lastname": "Torres"},
        {"firstname": "Pepe", "lastname": "Rodelo"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "José", "lastname": "García"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.73]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for i in super_list:
        print(i)


if __name__ == '__main__':
    run()