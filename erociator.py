# negotiator program



import time




class Negotiator():

    
    
    
    @staticmethod
    def intro():
        print("Negotiator")
        print("----------")
        time.sleep(0.5)
        print("This is a prototype of how a program which negotiates with a price would work.")
        print("------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("❤️_donate here_❤️")
        print("a3ro.xyz.viz@idfcbank")
    
    @staticmethod
    def negotiation( price, expectation):
        price = price # 100
        expectation = expectation # 40

        s1 = price - expectation # 60
        s2 = s1 - expectation # 20
        s3 = s2/2 # 10
        s4 = s3 + expectation # 50
        s5 = s4/2 # 25
        s6 = expectation + s5 # 65
        print(f"Negotiated amount is {s6}")
        print("""
    Note:
        This amount is not final and you should further negotiate it if possible.""")


Negotiator.intro()
nm = str(input("Enter the name of the article: \n"))
pre = int(input("Enter the price offered by the seller: \n"))
epx = int(input(f"Enter the price at what you expect the seller to give you {nm} at: \n"))
Negotiator.negotiation(pre, epx)


        