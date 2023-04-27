def get_optimal_distances_between_cash_machines(n: int, k: int, *args) -> list:
    """
    Расставляет k новых банкоматов.
    Там, где расстояние между ними самое большое

    :param n: Количество банкоматов на дороге.
    :param k: Количество банкоматов которые нужно поставить.
    :param args: Расстояния между соседними банкоматами.
    :return: Список с новыми расстояниями между соседними банкоматами
    """
    assert len(args) == n-1, ValueError('Количество расстояний должно быть равно количеству банкоматами')

    distances = list(args)

    for cash_machine in range(k):
        max_distance = max(distances)
        half_max_distance = max_distance / 2  # Новое расстояние до следующего банкомата
        index_max_distance = distances.index(max_distance)
        distances[index_max_distance] = half_max_distance  # Заменяет расстояние до следующего банкомата
        distances.insert(index_max_distance + 1, half_max_distance)  # Расстояние от нового банкомата до следующего
    return distances


if __name__ == '__main__':
    print(get_optimal_distances_between_cash_machines(5, 3, 100, 180, 50, 150))
    print(get_optimal_distances_between_cash_machines(4, 3, 1000, 180, 150))
    print(get_optimal_distances_between_cash_machines(5, 0, 1000, 180, 50, 150))
    print(get_optimal_distances_between_cash_machines(5, 4, 1000, 1000, 1000, 1000))
