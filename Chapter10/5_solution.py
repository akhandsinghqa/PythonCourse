# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.
from random import randint


class Train:

    def __init__(self, trainNo, source, destination):
        self.trainNo = trainNo
        self.source = source
        self.destination = destination

    def book(self):
        print("*********************************")
        print(
            f"Your ticket is booked successfully.\nFrom: {self.source} to {self.destination} in train no {self.trainNo}")
        print("*********************************")

    def getstatus(self):
        print(f"{self.trainNo} is running on time.")

    def ticket(self):
        fare = randint(250, 2500)
        print(f"Your fare from {self.source} to {self.destination} is Rs.{fare}.")


ticketbooking = Train(12490, "Meerut", "Delhi")

ticketbooking.book()
ticketbooking.getstatus()
ticketbooking.ticket()
