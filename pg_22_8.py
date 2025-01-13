# user-defined exceptions

class InsufficientBalanceError(Exception):
    def __init__(self, accno, cb):
        # print('self_init: ', self)
        self.__accno = accno
        self.__curbal = cb
        print('inside IBE')

    def get_details(self):
        # print('self_gt: ', self)
        return {'Acc No': self.__accno, 
                'Current Balance': self.__curbal}

class Customers:
    def __init__(self):
        self.__dct = {}

    def append(self, accno, nm, bal):
        self.__dct[accno] = {'Name': nm, 'Balance': bal}

    def deposit(self, accno, amt):
        d = self.__dct[accno]
        d['Balance'] = d['Balance'] + amt
        self.__dct[accno] = d

    def display(self):
        for k, v in self.__dct.items():
            print(k, v)
        print()

    def withdraw(self, accno, amt):
        d = self.__dct[accno]
        curbal = d['Balance']
        if curbal - amt < 5000:
            raise InsufficientBalanceError(accno, curbal)
        else:
            d['Balance'] = d['Balance'] - amt
            self.__dct[accno] = d

c = Customers()
print(c)
c.append(123, 'Bhavesh', 35000)
c.append(456, 'Nitin', 45000)
c.append(789, 'Sunny', 20000)
c.append(101, 'Krutika', 53000)
c.display()
c.deposit(789, 10000)
c.deposit(123, 5000)
c.display()

try:
    c.withdraw(101, 48000)
    print('amount withdrawn successfully')
    c.display()
    c.withdraw(101, 100)
    print('amount withdrawn successfully')
    c.display()

except InsufficientBalanceError as ibe:
    print('withdrawal denied')
    print('insufficient balance')
    print(ibe.get_details())
    print('ibe: ', ibe)
