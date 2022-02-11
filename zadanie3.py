import math
class fx:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def wynik(self):
        delta = (self.b * self.b) - 4 * (self.a * self.c)
        if delta > 0:
            sqrt_delta = math.sqrt(delta)
            x1 = -self.b - sqrt_delta / 2 * self.a
            x2 = -self.b + sqrt_delta / 2 * self.a
            return f"mz: {x1} v {x2}"
        elif delta == 0:
            x = -self.b / 2 * self.a
            return f"mz: {x}"
        else:
            return "Brak miejsc zerowych"
def main():
    f1 = fx(3, 4, 5)
    print(f1.wynik())
if __name__ == "__main__":
    main()