from math import comb


def count_lucky_tickets(start_digit):
    # Количество счастливых билетов, если стартовая цифра 0
    total_lucky_tickets = 0

    # Перебираем все возможные суммы для первых трех цифр
    for sum_first_half in range(0, 28):
        # Количество способов получить сумму sum_first_half с тремя цифрами
        ways_to_get_sum = comb(sum_first_half + 2, 2)
        # Количество счастливых билетов для текущей суммы
        lucky_tickets_for_sum = ways_to_get_sum ** 2
        # Добавляем к общему количеству счастливых билетов
        total_lucky_tickets += lucky_tickets_for_sum

    # Вычитаем количество билетов, которые не могут быть сгенерированы, начиная с start_digit
    # Это билеты, у которых первая цифра меньше start_digit
    if start_digit != 0:
        for sum_first_half in range(0, start_digit):
            ways_to_get_sum = comb(sum_first_half + 2, 2)
            total_lucky_tickets -= ways_to_get_sum ** 2

    return total_lucky_tickets


# Ввод стартовой цифры от 0 до 9
start_digit = int(input("Введите стартовую цифру (от 0 до 9): "))

# Вычисление и вывод количества счастливых билетов
print("Количество счастливых билетов:", count_lucky_tickets(start_digit))