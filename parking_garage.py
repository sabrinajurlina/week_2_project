class Garage():
    ticket_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    current_tickets = {}
    def __init__(self, tickets_avail=10, spaces_avail=10):
        self.tickets_avail = tickets_avail
        self.spaces_avail = spaces_avail

    def take_ticket(self):
        if self.spaces_avail == 0:
            print("We're sorry, there are no spaces available")
        else:
            self.tickets_avail -= 1
            self.spaces_avail -= 1
            self.current_tickets[ self.ticket_numbers[0] ] = ""
            del self.ticket_numbers[0]
            print(self.current_tickets)
       
    def pay_for_parking(self):
        ticket_number = int(input("Please enter your ticket number "))
        status = self.current_tickets.get(ticket_number)
        if status == 'paid':
            print('Your ticket has already been paid. You have 15 mins to exit the garage.')
        elif status == '':
            press_to_pay = input('Press any key to pay ')
            self.current_tickets[ ticket_number ] = "paid"
        else:
            if ticket_number not in self.current_tickets:
                print('Invalid Input')

    def leave_garage(self):
        ticket_number = int(input("Please enter your ticket number "))
        status = self.current_tickets.get(ticket_number)
        if status == 'paid':
            print('Thank you, have a nice day')
            del self.current_tickets[ticket_number]
            self.ticket_numbers.append(ticket_number)
            self.tickets_avail += 1
            self.spaces_avail += 1
        else:
            print('You must pay before you leave') 

#UI
class UI():
    def __init__(self):
        self.my_garage = Garage()
#to run the code...
    def run(self):
        while True:
            response = input("What would you like to do? Choose only one; Park, Pay, Leave, or Quit")
            if response.lower().strip() == 'quit':
                print("We're sorry, the parking garage is now closed")
                break
            elif response.lower().strip() == 'park':
                print("Please take a ticket ")
                self.my_garage.take_ticket()
            elif response.lower().strip() == 'pay':
                self.my_garage.pay_for_parking()
            elif response.lower().strip() == 'leave':
                self.my_garage.leave_garage()
            else:
                print("Invalid answer. Please choose either to Park, Pay, Leave, or Quit")
#driver code
my_ui = UI()
my_ui.run()
