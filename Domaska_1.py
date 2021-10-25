#1) Создать переменную типа String
name = 'Olya'
print(type(name))

#2) Создать переменную типа Integer
age= 18
print(type(age))

#3) Создать переменную типа Float
temp_october= float(3.5)
print(type(temp_october))

#4) Создать переменную типа Bytes
bytes_data = bytes(128)
new_bytes_data= type(bytes_data)
print(new_bytes_data)

#5) Создать переменную типа List
my_list = [1,3,7,11,15,89,178]
print(type(my_list))

#6) Создать переменную типа Tuple
my_tuple = ('Olya', 'Masha', 'Yulia', 'Lilia', 'Nadya', 'Anastasia')
print(type(my_tuple))

#7) Создать переменную типа Set
Days=set({"Mon","Tue","Wed","Thu","Fri","Sat","Sun"})
print(type(Days))

#8. Создать переменную типа Frozen set
Days=frozenset({"Mon","Tue","Wed","Thu","Fri","Sat","Sun","Mon","Tue","Wed","Thu","Fri","Sat","Sun"})
print(type(Days))

#9) Создать переменную типа Dict
my_animals_dict = {'cat': 'Alisa', 'dog': 'Bobik', 'bird': 'Kesha'}
print(type(my_animals_dict))

#10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.

print(name, type(name))
print(age, type(age))
print(temp_october, type(temp_october))
print(new_bytes_data, bytes_data)
print(my_list, type(my_list))
print(my_tuple, type(my_tuple))
print(Days, type(Days))
print(Days, type(Days))
print(my_animals_dict, type(my_animals_dict))

#11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
name = 'Volha'
second_name= 'Viarenich'
me=name+' '+second_name
print(me)

#12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
name = 'Volha'
age= 18
print(name , str(age))

#13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
name = 'Volha'
age= 18
print(name+' '+str(age))

#Ключевые зарезервированные слова в Питоне - true, false, none, and, or, not, assert, def, class, continue, break, if, else, elif, del, for, while, import, from, as, path, with.
