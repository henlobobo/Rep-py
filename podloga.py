import math
a=float(input('liczba '))
b=float(input('liczba '))
x=float(input('pojemnosc paczki '))
print('ilosc kartonow ', math.ceil(a*b/x))