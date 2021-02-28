some_list = ['в', '5', 'часов', '17', 'минут', 'темппература', 'воздуха', 'была', '+5', 'градусов']
sign = ''
count, digit = 0, 0

for idx in range(len(some_list) - 1, 0, -1):
    digit = some_list[idx]
    count = some_list.index(digit)
    if some_list[idx][0] == '+' or some_list[idx][0] == '-':
        sign = some_list[idx][:1]
        some_list[idx] = some_list[idx][1:]
    if some_list[idx].isdigit():
        if len(some_list[idx]) == 1:
            some_list[idx] = f"{sign}0{some_list[idx]}"
        elif len(some_list[idx]) > 1:
            some_list[idx] = f"{sign}{some_list[idx]}"
        some_list.insert(count, '"')
        some_list.insert(count + 2, '"')
    sign = ''

print(' '.join(some_list))
