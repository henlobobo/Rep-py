class Test:
    def __init__(self):
        self.publiczne, self._chronione, self.prywatne = 5, 8, 9
def main() :
    test = Test()
    print(test.publiczne)
    print (test._chronione)
    print(test._Test__prywatne)

    if __name__ == "__main__":
        main()

