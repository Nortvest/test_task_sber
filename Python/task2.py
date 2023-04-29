def get_optimal_distances_between_cash_machines(n: int, k: int, *args) -> list:
    """
    Расставляет k новых банкоматов.
    Там, где расстояние между ними самое большое

    :param n: Количество банкоматов на дороге.
    :param k: Количество банкоматов которые нужно поставить.
    :param args: Расстояния между соседними банкоматами.
    :return: Список с новыми расстояниями между соседними банкоматами
    """
    if len(args) >= n:  # Фильтр ненужных расстояний
        args = args[:n-1]

    new_distances = []

    # Максимальные k расстояний с их изначальными индексами и количеством разделений [[0, 100, 1], [1, 180, 1]]
    max_distances = sorted(zip(range(len(args)), args), reverse=True, key=lambda x: x[1])[:k]
    max_distances = {i: [distance, 1] for i, distance in max_distances}

    for i in range(k):
        # Выделяем наибольшее расстояние между банкоматами без сохранения в основной список
        distances = [[i, distance / div] for i, (distance, div) in max_distances.items()]
        index_max_distance = max(distances, key=lambda x: x[1])[0]  # Argmax
        max_distances[index_max_distance][1] += 1  # Увеличиваем счетчик разделений на 1

    for i in range(n-1):  # Формируем финальный список расстояний
        if i in max_distances.keys():
            distance, div = max_distances[i]
            new_distances.extend([distance / div] * div)
        else:
            new_distances.append(args[i])
    return new_distances


if __name__ == '__main__':
    print(get_optimal_distances_between_cash_machines(5, 3, 100, 180, 50, 150))  # [50.0, 50.0, 90.0, 90.0, 50, 75.0, 75.0]
    print(get_optimal_distances_between_cash_machines(4, 3, 1000, 180, 150))  # [250.0, 250.0, 250.0, 250.0, 180.0, 150.0]
    print(get_optimal_distances_between_cash_machines(5, 0, 1000, 180, 50, 150))  # [1000, 180, 50, 150]
    print(get_optimal_distances_between_cash_machines(5, 5, 1000, 1000, 1000, 1000))  # [333.3, 333.3, 333.3, 500.0, 500.0, 500.0, 500.0, 500.0, 500.0]
