def czy_parzysta(nrPESEL):
    if int(nrPESEL[9]) % 2 != 0:
        return True
    else:
        return False


def kto(nrPESEL):
    if czy_parzysta(nrPESEL):
        print('1(K)')
    else:
        print('2(M)')

dlugosc = 0

dlugosc = 0
while dlugosc != 11:
    nrPESEL = int(input("podaj pesel: "))
    nrPESEL = str(nrPESEL)
    dlugosc = len(nrPESEL)
else:
    kto(nrPESEL)
