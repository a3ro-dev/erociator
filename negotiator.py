# negotiator program



import time
import random

class Negotiator():

    @staticmethod
    def intro():
        print("Negotiator")
        print("----------")
        time.sleep(0.5)
        print("This is a prototype of how a program which negotiates with a price would work.")
        print("------------------------------------------------------------------------------")
        time.sleep(0.5)
        print(" ❤️ donate here ❤️ ")
        print("a3ro.xyz.viz@idfcbank")


    def negotiation(self, price, expectation):
        self.price = price
        self.expectation = expectation

        s1 = self.price - self.expectation
        
        
