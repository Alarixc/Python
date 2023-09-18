class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
        status=[]
        for x in range(self.seats):
            status.append(self.seats)
            self.seats-=1
            if(self.seats==0):
                break
        print(status)
    
    def status(self):
        print(f"The name of the train is {self.name}.")
        print(f"The seats available in the train are {self.seats}.")

    def fareInfo(self):
        print(f"The fare of a ticket in the train is {self.fare}.")

    @staticmethod
    def availableOrNot(self):
        if(self.seats==0):
            print("The booking is unavailable as there are no seats.")
        elif(self.seats>0):
            print(f"The booking of the train is available.\nYour seat has been booked.\nYour seat number is {self.seats}")
            self.seats=self.seats-1
            while(True):
                response=input("Do you wanna book another ticket?Y/N")
                if response.upper()=='Y':
                    break
                elif response.upper()=='N':
                    break
                else:
                    print("Invalid! Try again!")
            while(response.upper()=='Y'):
                    print(f"Your seat has been booked.\nYour train number is {self.seats}")
                    self.seats=self.seats-1
                    while(True):
                        response=input("Do you wanna book another ticket?Y/N")
                        if response.upper()=='Y':
                            break
                        elif response.upper()=='N':
                            break
                        else:
                            print("Invalid! Try again!")
            exit("Okay,thank you for your time! Have a great journey!")

name=input("Enter the name of the train:\n")
seats=int(input("Enter the number of seats available in the train:\n"))
fare=int(input("Enter the fare of a ticket for a seat in the train:\n"))
intercity=Train(name,fare,seats)
intercity.status()
intercity.fareInfo()
intercity.availableOrNot(intercity)


