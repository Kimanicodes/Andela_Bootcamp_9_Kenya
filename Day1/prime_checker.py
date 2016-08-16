class PrimeChecker(object):
    def __init__(self, number=""):
        self.number = number

    def is_prime(self):
        if self.number == "":
            return False
        for i in range(2, int((int(self.number)**0.5) + 1)):
            if int(self.number) % i == 0:
                return False
        return True

x = PrimeChecker('')
print(x.is_prime())