# z51. ДЗ
# Напишите ф-ю same_by(characteristic, objects),
# к-я проверяет все ли объекты имеют одинаковое значение
# некоторой хар-ки и возвращают True, если это так.
# Если значение хар-ки для разных объетов отличается - 
# то False. Для пустого набора объектов ф-я должна 
# возвращать True. Аргумент characteristic - это ф-я,
# к-я принимает объект и вычисляет его хар-ку.

values = [0, 3, 12, 21]
def same_by(func, collection):
    return sum(filter(func, collection)) == 0
if same_by(lambda x: x % 3, values):
    print('same')
else:
    print('different')