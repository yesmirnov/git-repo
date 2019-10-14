'''
Перестановка соседних элементов в списке, последний нечетный элемент остается на месте
'''
# Ввести список swapping_list; el - кол-во элементов; разделитель при вводе - пробел
swapping_list = [el for el in input('Введите произвольный список элементов через пробел: ').split()]

# собственно перестановка соседних элементов списка
for el in range(1, len(swapping_list), 2):
    swapping_list[el - 1], swapping_list[el] = swapping_list[el], swapping_list[el - 1]
# Создание и вывод нужной строки str
print("Результат перестановки: ", ' '.join([str(el) for el in swapping_list]))
