def get_max_number_from_numbers(numbers: list[str]) -> str:
    """
    Составляет наибольшее число из переданных

    :param numbers: Список строк-чисел.
    :return: Число составленное из numbers.
    """
    return ''.join(sorted(numbers, reverse=True))


if __name__ == '__main__':
    print(get_max_number_from_numbers(['11', '234', '005', '89']))
    print(get_max_number_from_numbers(['119', '2', '0500', '89']))
    print(get_max_number_from_numbers(['1', '12', '1', '1']))
    print(get_max_number_from_numbers(['0', '02', '0', '0']))
    print(get_max_number_from_numbers(['1', '02', '1', '1']))
    print(get_max_number_from_numbers(['', '3', '', '']))
