immutable_var = tuple = 1, 2, 3, 4, 5, 'вышел', 'зайчик', 'погулять'
print(tuple)
#кортеж не поддерживает обращение по элементам
mutable_list = list = [1, 2, 3, 4, 5, 'вышел', 'зайчик', 'погулять']
list[5] = 'выходи'
list[6] = 'гулять'
list[7] = 'опять'
list.append('Modified')
print(list)