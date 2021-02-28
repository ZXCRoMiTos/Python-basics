some_list, new_list = [57.8, 46.51, 97, 67.3, 78.3, 37, 84.3], [57.8, 46.51, 97, 67.3, 78.3, 37, 84.3]
some_str, fractional, new_str = '', '', ''
integer = 0

for el in some_list:
    some_str = str(el)
    integer = int(el)
    if some_str.count('.') != 0:
        fractional = some_str[some_str.index('.') + 1:]
    if len(fractional) == 1:
        fractional += '0'
    print(f'{integer} руб {fractional} копеек')
    fractional = '00'

print(sorted(some_list))
new_list.sort(reverse=True)
print(new_list)
print(sorted(some_list, reverse=True)[:5])
