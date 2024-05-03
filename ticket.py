from math import comb
def count_lucky_tickets():
    total_lucky_tickets = 0
    # Перебираем все возможные суммы для первых трех цифр
    for sum_first_half in range(0, 28):
        # Количество способов получить сумму sum_first_half с тремя цифрами
        ways_to_get_sum = comb(sum_first_half + 2, 2)
        # Количество счастливых билетов для текущей суммы
        lucky_tickets_for_sum = ways_to_get_sum ** 2
        # Добавляем к общему количеству счастливых билетов
        total_lucky_tickets += lucky_tickets_for_sum
    return total_lucky_tickets

# Вычисление и вывод количества счастливых билетов
print("Количество счастливых билетов:", count_lucky_tickets())