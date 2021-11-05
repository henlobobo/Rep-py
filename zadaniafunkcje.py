#1
for i in range(2,10, 2):
    print(i)

#2
for i in range(50, 150, 3):
    print(i)

#3  hejka sloneczko <3

lista = [1, 4, 7, 345, 671, 445, 3, -5]
najmniejszaliczba = lista[0]
for i in lista:
    if i < najmniejszaliczba:
        najmniejszaliczba = i
print(najmniejszaliczba)

#4
for i in range(0,10):
    print(i)
    print(i+i-1)

#5

for i in range(1, 8):
    if i == 5:
        print("znalazlem 5!!!")
    else:
        print(i)

#6
for i in range(1,4):
    for j in ["a","b","c"]:
        print(str(i)+" "+j)

#7
for i in range(10, -1, -1):
    if i !=0:
        print(i)
    else:
        print("Rakieta startuje XDDD")


#8
lista1 = ["KKKK", "GGGG", "HHHH"]
lista2 = ["563-12", "363-AB"]

for i in lista1:
    for j in lista2:
        print(i+" "+j)
    print("-----------")


#1
def funkcjezadanie1():
    i = 2
    while i < 9:
        print(i)
        i+=1
funkcjezadanie1()

#2

def funkcjezadanie2(lista):
    for i in lista:
        print(i)
funkcjezadanie2([6,12,2,3,8])

#3

def funkcjezadanie3(znak, lista):
    for i in lista:
        if i == znak:
            print("Znalazlem znak rakiety "+ znak)
            break;
        else:
            print(i)
funkcjezadanie3('t',"Rakieta")