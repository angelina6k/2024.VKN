#Варіант 7.1

from array import array


number_array = input('Введіть числа, розділені пробілами: ')
list1 = []


for num in number_array.split():  
    list1.append(int(num))  


mas = array('i', list1)
print('Масив:', mas)


A = sum(mas) / len(mas)
print('Середнє арифметичне:', A)
