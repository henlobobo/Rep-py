class Licznik:
    ile = 0
    def __init__(self):
        Licznik.ile +=1
        self.ktory = Licznik.ile
        print(f"To jest obiekt {Licznik.ile}")

    def __del__(self):
        Licznik.ile-=1
        print(f"Niszczę obiekt nr {self.ktory}, pozostało jeszcze {Licznik.ile}.")

    def policz():
        return Licznik.ile

def main():
    a=Licznik()
    b=Licznik()
    c=Licznik()
    print(f"a to obiekt nr {a.ktory}")
    print(f"b to obiekt nr {b.ktory}")
    print(f"c to obiekt nr {c.ktory}")
    print(f"Liczba obiektow to: {Licznik.policz()}")
    a = None
    b = None
    print(f"Liczba obiektow to: {Licznik.policz()}")

if __name__ == "__main__":
    main()