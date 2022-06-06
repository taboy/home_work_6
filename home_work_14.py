#14.	Подсчитать сумму цифр в вещественном числе.
num=(input("write a number"))
a=num.split(".")
sum=sum(map(int,a))
print(sum)