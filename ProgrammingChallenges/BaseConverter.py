class Number:


    def __init__(self, number, base):
        self.number = number
        self.base = base

    def changeBase(self, base):
        if self.number == 0:
            self.base = base

        if base > 10 or base <2:
            raise ValueError
        
        if self.base> base:
            self.decomposition(base)
        elif self.base <base:
            self.composition(base)
        else:
            return
    def decomposition(self, targetBase):
        number = self.number
        result = []
        
        while(number>0):
            result.append(number%targetBase)
            number //= targetBase
        result.reverse()

        self.base = targetBase
        self.number = int("".join(map(str,result)))

        
        

    def composition(self, targetBase):
        number = self.number
        listNumber = [int(x) for x in str(number)]
        listNumber.reverse()
        
        Base10 = sum([x * (self.base ** i) for i,x in enumerate(listNumber)])

        self.number = Base10
        self.base = 10

        self.decomposition(targetBase)


    def __str__(self):
        return str(self.number)



def test_number_class():
    # 1. Binary to Decimal
    n = Number(1011, 2)
    n.changeBase(10)
    assert n.number == 11 and n.base == 10

    # 2. Decimal to Binary
    n = Number(11, 10)
    n.changeBase(2)
    assert n.number == 1011 and n.base == 2

    # 3. Binary to Base-3
    n = Number(1011, 2)
    n.changeBase(3)
    assert n.number == 102 and n.base == 3

    # 4. Base-5 to Base-10
    n = Number(243, 5)
    n.changeBase(10)
    assert n.number == 73 and n.base == 10

    # 5. Base-10 to Base-5
    n = Number(73, 10)
    n.changeBase(5)
    assert n.number == 243 and n.base == 5

    # 6. No-op: Changing to same base
    n = Number(123, 4)
    n.changeBase(4)
    assert n.number == 123 and n.base == 4

    # 7. Edge case: zero input
    n = Number(0, 10)
    n.changeBase(2)
    assert n.number == 0 and n.base == 2

    # 9. Leading zeros in input base (e.g. 00101 base-2)
    n = Number(101, 2)
    n.changeBase(10)
    assert n.number == 5 and n.base == 10

    # 10. Chain conversion: Binary → Decimal → Base-4
    n = Number(1111, 2)
    n.changeBase(10)
    assert n.number == 15 and n.base == 10
    n.changeBase(4)
    assert n.number == 33 and n.base == 4

    # 8. Decimal to Hex-equivalent (base-16-like)
    n = Number(255, 10)

    worked = False
    try:
        n.changeBase(16)
    except ValueError:
        worked = True

    assert worked == True

    # 8. Decimal to Hex-equivalent (base-16-like)
    n = Number(255, 10)

    worked = False
    try:
        n.changeBase(1)
    except ValueError:
        worked = True


    print("tests complete")




test_number_class()
