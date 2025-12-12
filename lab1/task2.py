from math import sin,cos,log,exp
x = float(input('введите значение переменной x:'))
y = float(input('введите значение переменной y:'))
z = float(input('введите значение переменной z:'))

a = (((x**3)/2)/2)**(1/2)-sin(y)

b = (exp(2))/3-cos(y)+z+log(y)

print(f"Получено значение функции а={a}")

print(f"Получено значение функции а={b}")


