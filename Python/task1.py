import re


def special_number_to_good_number(special_number: str) -> str:
    """
    Принимает Особенную строки и делает из нее Хорошую

    Example:
        :param special_number: 405\549
        :return: 0405\00549
    """
    first_num, second_num = special_number.split('\\', maxsplit=1)
    return rf'{first_num.zfill(4)}\{second_num.zfill(5)}'


def find_good_number(input_text: str) -> str:
    """
    Принимает на вход строку и для каждого особенного номера,
    встречающегося в строке, выводит соответствующий хороший номер.

    Example:
        :param input_text: Адрес 5467\456. Номер 405\549
        :return: 5467\00456
                 0405\00549
    """
    special_numbers = re.findall(r'\b\d{2,4}\\\d{2,5}\b', input_text)

    # В задании написано Вывести результат, поэтому оставляю эту строчку
    # print('\n'.join(map(special_number_to_good_number, special_number)))
    return '\n'.join(map(special_number_to_good_number, special_numbers))


if __name__ == '__main__':
    print(find_good_number(r'Адрес 5467\456. Номер 405\549'), end='\n\n')
    print(find_good_number(r'Адрес 5467\456. Номер 1405\54. Для теста 89765\234'), end='\n\n')
    print(find_good_number(r'Адрес 5467\456. можно так 10\10'), end='\n\n')
    print(find_good_number(r'мой адрес 1\234567'), end='\n\n')
