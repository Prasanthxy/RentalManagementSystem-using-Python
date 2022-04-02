class RentalManagement:

    def __init__(self, rt='', s=0, p=0, r=0, t=0, a=1800, name='', address='',
                 cindate='', coutdate='', rno=101):

        print("\n\n*****WELLCOME TO THE HOTEL HEAVEN*****\n")

        self.rt = rt

        self.r = r

        self.t = t

        self.p = p

        self.s = s
        self.a = a
        self.name = name
        self.address = address
        self.cindate = cindate
        self.coutdate = coutdate
        self.rno = rno

    def inputdata(self):
        self.name = input("\nEnter the name:")
        self.address = input("\nEnter the address:")
        self.cindate = input("\nEnter the room booking date:")
        self.coutdate = input("\nEnter the room leaving date:")
        print("Your room no.:", self.rno, "\n")

    def roomrent(self):

        print("The rooms available for you:-")

        print("1.  Luxurious room -->7000")

        print("2.  Triple bed room -->5000")

        print("3.  Double bed room -->3000")

        print("4.  Single bed room -->1500")

        x = int(input("Enter the selected room")) 

        n = int(input("How many days would like to stay:")) 

        if x == 1:

            print("You have chosen the Luxurious room")

            self.s = 7000 * n

        if x == 2:

            print("You have chosen the Triple bed room")

            self.s = 5000 * n

        if x == 3:

            print("You have chosen the Double bed room")

            self.s = 3000 * n

        if x == 4:
            print("You have chosen the Single bed room")

            self.s = 1500 * n

        else:

            print("What type of room would like to stay")

        print("Your choosen room price is=", self.s, "\n")

    def restaurantbill(self):

        print("*****Your Menu For The Food Order*****")

        print("1.Desserts--->150", "2.Drinks and Refreshments--->300", "3.Morning Breakfast--->125",
              "4.Lunch--->200",
              "5.Dinner--->175", "6.Exit")

        while 1:

            c = int(input("Enter the food you want to tatse:")) 

            if c == 1:
                d = int(input("Enter the quantity:")) 
                self.r = self.r + 150 * d

            if c == 2:
                d = int(input("Enter the quantity:")) 
                self.r = self.r + 300 * d

            if c == 3:
                d = int(input("Enter the quantity:")) 
                self.r = self.r + 125 * d

            if c == 4:
                d = int(input("Enter the quantity:")) 
                self.r = self.r + 200 * d

            if c == 5:
                d = int(input("Enter the quantity:")) 
                self.r = self.r + 175 * d

            if c == 6:
                break
            else:
                print("You entered the unknown choice")

        print("Order total cost=Rs", self.r, "\n")

    def laundrybill(self):
        print("***LAUNDRY SERVICES***")

        print("1.T-Shirts and Shorts--->25", "2.Pants--->15", "3.Shirts--->10",
              "4.Jeans--->15", "5.Girlwear--->20",
              "6.Exit")

        while 1:

            e = int(input("Enter your choice:")) 

            if e == 1:
                f = int(input("Enter the quantity:")) 
                self.t = self.t + 25 * f

            if e == 2:
                f = int(input("Enter the quantity:")) 
                self.t = self.t + 15 * f

            if e == 3:
                f = int(input("Enter the quantity:")) 
                self.t = self.t + 10 * f

            if e == 4:
                f = int(input("Enter the quantity:")) 
                self.t = self.t + 15 * f

            if e == 5:
                f = int(input("Enter the quantity:")) 
                self.t = self.t + 20 * f
            if e == 6:
                break
            else:

                print("Invalid option")

        print("Total Laundary Cost=Rs", self.t, "\n")

    def entertainment(self):
        print("******Entertainments and Games*******")

        print("1.Swimming Pool--->100", "2.Bowling--->80", "3.Golf--->150",
              "4.Video games--->50", "5.Gym--->70",
              "6.Exit")

        while 1:

            g = int(input("Enter your choice:")) 

            if g == 1:
                h = int(input("No. of hours:")) 
                self.p = self.p + 100 * h

            if g == 2:
                h = int(input("No. of hours:")) 
                self.p = self.p + 80 * h

            if g == 3:
                h = int(input("No. of hours:")) 
                self.p = self.p + 150 * h

            if g == 4:
                h = int(input("No. of hours:")) 
                self.p = self.p + 50 * h

            if g == 5:
                h = int(input("No. of hours:")) 
                self.p = self.p + 70 * h
            if g == 6:
                break

            else:

                print("Invalid option")

        print("Total Entertainment and Game Charges=Rs", self.p, "\n")

    def display(self):
        print("******YOUR BILL******")
        print("Customer details:")
        print("Name of the customer:", self.name)
        print("Address of the customer:", self.address)
        print("Room booking date of the customer:", self.cindate)
        print("Room leaving date of the customer:", self.coutdate)
        print("Room no.", self.rno)
        print("Room rent:", self.s)
        print("Food bill:", self.r)
        print("Laundary bill:", self.t)
        print("Entertainment and Game Charges:", self.p)

        self.rt = self.s + self.t + self.p + self.r

        print("Your sub total Purchased is:", self.rt)
        print("Additional Service Charges is", self.a)
        print("Your final total Purchased is:", self.rt + self.a, "\n")
        self.rno += 1


def main():
    a = RentalManagement() 

    while 1:
        print("1.Enter Customer Data:")

        print("2.Calculate Room rent:")

        print("3.Calculate Food bill:")

        print("4.Calculate Laundry bill:")

        print("5.Calculate Entertainment and Game Charges:")

        print("6.Total cost:")

        print("7.EXIT")

        b = int(input("\nEnter the number of your choice:")) 
        if b == 1:
            a.inputdata()

        if b == 2:
            a.roomrent()

        if b == 3:
            a.restaurantbill()

        if b == 4:
            a.laundrybill()

        if b == 5:
            a.entertainment()

        if b == 6:
            a.display()

        if b == 7:
            quit()


main()
