#11.	Сформировать список из  N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.

count = int(input("write a number"))
num=1
list=[(-3)**num for num in range(count)]
print(list)