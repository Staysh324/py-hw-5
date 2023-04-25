# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.


a = float(input("введите число = "))
b = float(input("введите степень = "))
c = a
def stepen(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    if b < 0:
        return 1/(a * stepen(a, -b - 1))
    if b > 1:
        return (a * stepen(a, b - 1))

a = stepen(a, b)  
b = int(b)
c = int(c)
print (f"число {c} в степени {b} = {a}")





