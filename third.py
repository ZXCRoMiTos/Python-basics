some_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
string, name = '', ''

for el in some_list:
    string = el.split()
    name = string[-1].title()
    print(f"Привет, {name}")

