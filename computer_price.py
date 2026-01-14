class Computer:
    def __init__(self):
        self.__maxprice = 900
       
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))   

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price directly (this will NOT work)
c.__maxprice = 1000
c.sell()

# using setter function (this WILL work)
c.setMaxPrice(1000)
c.sell()