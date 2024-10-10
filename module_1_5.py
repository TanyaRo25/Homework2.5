immutable_var=25,300,"avocado",True,"honey"
print(immutable_var)
#immutable_var[1] = 7.5 TypeError: 'tuple' object does not support item assignment
#Кортеж - неизменяемый тип данных в Python.
#После создания кортежа в него нельзя добавлять элементы, а также изменять и удалять их.
mutable_list = [25,300,"avocado",True,"honey"]
mutable_list[0] = 25**2
mutable_list[2] = 'soft juicy kiwi'
mutable_list.remove(300)
mutable_list.append('strawberry')
print(mutable_list)

