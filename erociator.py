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
        print("UPI")
        print("7376549282@fam")
    
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
        The formula in the code is a simple calculation but may not be applicable in all situations as it doesn't take into account specific details of the negotiation.
        Negotiations are complex and require a thorough understanding of the market, item, and parties involved.
        It's important to use negotiation techniques and consider other factors to reach a mutually beneficial agreement.""")


Negotiator.intro()
nm = str(input("Enter the name of the article: \n"))
pre = int(input("Enter the price offered by the seller: \n"))
epx = int(input(f"Enter the price at what you expect the seller to give you {nm} at: \n"))
Negotiator.negotiation(pre, epx)


        
