# TODO Напишите функцию find_common_participants
# TODO Провеьте работу функции с разделителем отличным от запятой

def find_common_participants(group1, group2, separator=','):

    group1_list1 = group1.split(separator)
    group2_list2 = group2.split(separator)
    common_participants = list(set(group1_list1).intersection(group2_list2))
    common_participants.sort()
    return common_participants

# Данные для первой и второй группы
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Поиск общих участников
common = find_common_participants(participants_first_group, participants_second_group, separator='|')
print("Общие участники:", common)