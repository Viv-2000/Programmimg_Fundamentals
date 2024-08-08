#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#NAME        :  VIVEK AGGARWAL
#STUDENT ID  :  S4015465

#PROGRAMING FUNDAMENTAL ASSIGNMENT 2

#CURRENTLY I HAVE JUST DESIGNED THE CLASSES, AND HAVENT LINKED THEM YET TO ANY OBJECT YET.


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Importing all the libraries we are allowed to use

import sys
import os

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def get_string(prompt):
    
    input_invalid = True
    while (input_invalid):

        sys.stdout.write(prompt)
        sys.stdout.flush()
        input_string = sys.stdin.readline().strip().title()

        if (len(input_string) == 0):
            print("Sorry, input cannot be blank.")
            continue

        if not input_string.isalnum():
            print("Invalid input. Input must contain alphabets or digits only.")
            continue

        input_invalid = False
             
    return input_string

#....................................................................................................................................................................................

def get_integer(prompt):
    
    while True:
        input_integer = get_string(prompt)
        if not input_integer.isdigit():
            print('Invalid input. Input must contain digits only. Please try again.')
            continue
        else:
            input_integer = int(input_integer)

        if input_integer <= 0:
            print('Invalid input. Input value has to be a number greater than 0. Please try again.')
            continue
        else:
            return input_integer
                       
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Customer:                                             #creating class Customer
    
    def __init__(self, ID, name):                           #initializing constructor method
        self.ID = ID                                        #initialising Customer.ID
        self.name = name                                    #initialising Customer.name

    def get_ID(self):                                       #get_ID() = getter method for Customer ID
        return self.ID

    def get_name(self):                                     #get_name() = getter method for Customer name
        return self.name

    def get_discount(self, cost):                           #get_discount() = method to store ticket cost and return 0
##      self.ticket_cost = cost
        return 0

##  def get_ticket_cost(self):                              #get_ticket_cost() = getter method for individual ticket cost
##      return self.ticket_cost

    def get_booking_fee(self, ticket_quantity):             #get_booking_fee() = method to store ticket quantity and return booking fee
##      self.ticket_quantity = ticket_quantity
        self.booking_fee = ticket_quantity * 2              #booking_fee = instance variable storing the cost of booking
        return self.booking_fee

##  def get_ticket_quantity(self):                          #get_ticket_quantity = getter method for ticket quantity
##      return self.ticket_quantity

    def display_info(self):                                 #display_info() = method to display Customer ID and name
        print('{:<15}{:>20}'.format("Customer ID :", self.ID))
        print('{:<15}{:>20}'.format("Customer name :", self.name))
##      print('{:<15}{:>20}'.format("Ticket cost :", self.ticket_cost))
##      print('{:<15}{:>20}'.format("Ticket quantity :", self.ticket_quantity))
       
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class RewardFlatCustomer(Customer):                         #creating new class RewardFlatCustomer that inherits from Customer class defined above

    discount_rate = 0.2                                     #static variable dicount_rate set to 20%


    def get_discount(self, cost):                           #get_discount = getter to get discount value                          \
        self.discount = cost * RewardFlatCustomer.discount_rate
        return self.discount
    
    def display_info(self):                                 #method to display information of all attributes
        super().display_info()                              #super() copies code from above, and adding more print statements
        print('{:<15}{:>20}'.format("Discount rate :",self.discount_rate ))
            
        
    
    @staticmethod                                           #static method set_discount_rate to update value of discount_rate
    def set_discount_rate(discount_rate):
        RewardFlatCustomer.discount_rate = discount_rate

    @staticmethod                                           #static method get_discount_rate to get the value of discount rate
    def get_discount_rate():
        return RewardFlatCustomer.discount_rate

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class RewardStepCustomer(Customer):
    
    threshold = 50               #default threshold is set to 50
    
    def __init__(self, ID, name, discount_rate=.3):      #default discount_rate is 30%
        super().__init__(ID, name)
        self.discount_rate = discount_rate
    
    def get_discount(self, cost):
        if cost >= RewardStepCustomer.threshold:
            self.discount = cost * self.discount_rate
            return self.discount
        else:
            self.discount = 0
            return self.discount
    
    def display_info(self):
        super().display_info()  #super() takes the code for display_info from parent and lets us add more
        print('{:<15}{:>20}'.format("Threshold is :", self.threshold))
        print('{:<15}{:>20}'.format("Discount Rate :", self.discount_rate))


    def get_discount_rate(self):
        return self.discount_rate
    
    @staticmethod 
    def set_threshold(new_threshold):
        RewardStepCustomer.threshold = new_threshold


    @staticmethod 
    def get_threshold():
        return RewardStepCustomer.threshold
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Movie:            #creating class Movie
    def __init__(self, ID, name, seat_available):
        self.ID = ID
        self.name = name
        self.seat_available = seat_available

    def display_info(self):
        print('{:<15}{:>20}'.format("Movie ID :", self.ID))
        print('{:<15}{:>20}'.format("Movie name :", self.name))
        print('{:<15}{:>20}'.format("Seats available :", self.seat_available))




    def get_ID(self):
        return self.ID
    

    def get_name(self):
        return self.name

       
    def get_seat_available(self):
        return self.seat_available

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Ticket:
    
    def __init__(self, ID, name, price):
        self.ID = ID
        self.name = name
        self.price = price
        
    def display_info(self):
        print('{:<15}{:>20}'.format("Ticket ID :", self.ID))
        print('{:<15}{:>20}'.format("Ticket name :", self.name))
        print('{:<15}{:>20}'.format("Ticket price :", self.price))

   
    def get_ID(self):
        return self.ID


    def get_name(self):
        return self.name
    

    def get_price(self):
        return self.price
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
class Booking:
    def __init__(self, customer, movie, ticket, ticket_quantity):
        self.customer = customer
        self.movie = movie
        self.ticket = ticket
        self.quantity = ticket_quantity
        
    def compute_cost(self):
        self.cost = self.ticket.get_price() * self.quantity
        self.booking_fee = self.customer.get_booking_fee(self.quantity)
        self.discount = self.customer.get_discount(self.cost)
       
        return self.cost, self.booking_fee, self.discount


    def get_cost(self):
        return self.cost

    def get_booking_fee(self):
        return self.booking_fee

    def get_discount(self):
        return self.discount
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Records:

    customers = []
    movies = []
    tickets = []
    
##as of now we are storing all lists as static variables, but will fill the lists as instance variables

    def read_customers(self, file_name):

        try:
            with open(file_name,'r') as f:
                for line in f:
                    row=line.strip().split(",")
                    [x.strip() for x in row]
                    customer_ID = row[0]
                    customer_name = row[1].title()        #to save customer name with first letter in uppercase
            
                    if (row[0][0].upper() == 'C'):
                        customer = Customer(customer_ID, customer_name)

                    elif (row[0][0].upper() == 'F'):
    ##                  discount_rate = row[2]
    ##                  if discount_rate != 2:
    ##                      RewardFlatCustomer.set_discount_rate(discount_rate)
                        
                        customer = RewardFlatCustomer(customer_ID, customer_name)

                    elif (row[0][0].upper() == 'S'):
                        discount_rate = row[2]                    
    ##                  threshold = row[3]
    ##                  if threshold != 50:
    ##                      RewardStepCustomer.set_threshold(threshold)
                        
                        customer = RewardStepCustomer(customer_ID, customer_name, discount_rate)

                    else:
                        continue
                    
                    self.customers.append(customer)
            return True
        except:
            return False   #or pass
                    



    def read_movies(self, file_name):

        try:
            
            with open(file_name,'r') as f1:
                for line in f1:
                    row=line.strip().split(",")
                    [y.strip() for y in line]

                    if (row[0][0].upper() !='M'):
                        continue
                    
                    movie_ID = row[0]
                    movie_name = row[1].title()
                    seats_available = row[2]

                    movie = Movie(movie_ID, movie_name, seats_available)

                    self.movies.append(movie)
            return True
        except:
            return False  #or pass



    def read_tickets(self, file_name):

        try:            
            with open(file_name,'r') as f2:
                for line in f2:
                    row=line.strip().split(",")
                    [z.strip() for z in line]

                    if (row[0][0].upper() !='T'):
                        continue
                    
                    ticket_ID = row[0]
                    ticket_name = row[1].title()
                    ticket_unit_price = row[2]

                    ticket = Ticket(ticket_ID, ticket_name, ticket_unit_price)

                    self.tickets.append(ticket)
            return True
        except:
            return False     #or pass



    def find_customer(self, customer_name):
##      column_format = "{:<" + str(dates_width) + "} {:<" + str(names_width) + "} {:>" + str(amounts_width) + "}\n"
#        user_inp = get_string("Please enter customer name__")

        if self.customers == []:
            print('There are no customers to find. Try adding a few first. ')
            return None
        
        i = 0
        for customer in self.customers:
            if customer.get_name() == customer_name:
                return customer

        if i == 0:
            return None


            
    def find_movie(self, movie_name):
#        user_inp = get_string("Please enter movie name__")

        if self.movies == []:
            print('There are no movies to find. Try adding a few first. ')
            return None
        
        i = 0
        for movie in self.movies:
            if movie.get_name() == movie_name:
                return movie

        if i == 0:
            return None
        


    def find_ticket(self, ticket_name):
#        user_inp = get_string("Please enter the name of the ticket you are searching for__").lower()
       
        if self.tickets == []:
            print('There are no tickets to find. Try adding a few first. ')
            return None

        i = 0
        for ticket in self.tickets:
            if ticket.get_name() == ticket_name:
                return ticket

        if i == 0:
            return None
                
        
        


    def display_customers(self):
        print("\n The details of all the existing customers are as follows:")
        for customer in self.customers:
            if isinstance(customer, Customer):
                print(customer.get_ID() + ',' + customer.get_name())
            elif isinstance(customer, RewardFlatCustomer):
                print(customer.get_ID() + ',' + customer.get_name() + ',' + customer.get_discount_rate())
            elif isinstance(customer, RewardStepCustomer):
                print(customer.get_ID() + ',' + customer.get_name() + ',' + customer.get_discount_rate() + ',' + customer.get_threshold())
            else:
                pass



    def display_movies(self):
        print("\n The details of all the existing movies are as follows:")
        for movie in self.movies:
            print(movie.get_ID() + ',' + movie.get_name() + ',' + movie.get_seat_available())

    
    def display_tickets(self):
        print("\n The details of all the existing ticket types are as follows:")
        for ticket in self.tickets:
            print(ticket.get_ID() + ',' + ticket.get_name() + ',' + ticket.get_price())

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Operations:

    record = Records()

    
    def menu(self):
        print('\n\n')
        print("Welcome to RMIT movie ticketing system.")
        print("Please note that some inputs can be case-sensitive.") 
        print('*'*60)
        print('''You can choose from the following options:
1. Purchase a ticket 
2. Display existing customers' information
3. Display existing movies' information
4. Display existing ticket types' information
0. Exit the program''')
        print('*'*60)                                    #given user all information regarding choosing an option


        user_choice = input("Please choose any one of the options given above__").strip()

        return user_choice


    def load_data(self):
        c_file = 'customers.txt'
        if not self.record.read_customers(c_file):
            print(f"Sorry, the file '{c_file}' is missing")
            return False

        m_file = 'movies.txt'
        if not self.record.read_movies(m_file):
            print(f"Sorry, the file '{m_file}' is missing")
            return False
        
        t_file = 'tickets.txt'
        if not self.record.read_tickets(t_file):
            print(f"Sorry, the file '{t_file}' is missing")
            return False

        return True



    def purchase_ticket(self):
        
        user_name = get_string('Please enter your name__')
        customer = self.record.find_customer(user_name)
        
        movie_name = get_string('Please enter movie name__')
        movie = self.record.find_movie(movie_name)
                
        ticket_name = get_string('Please enter the ticket type__')
        ticket = self.record.find_ticket(ticket_name)

        ticket_quantity = get_integer('Please enter the number of tickets you wish to purchase__')

        booking = Booking(customer, movie, ticket, ticket_quantity)
        print(booking.compute_cost())
        
        
        



    def run_operations(self):

        if not self.load_data():
            return

        user_choice = self.menu()
        while True:
            match user_choice:
                case '1':
                    self.purchase_ticket()
                case '2':
                    self.record.display_customers()
                case '3':
                    self.record.display_movies()
                case '4':
                    self.record.display_tickets()
                case '0':
                    print('Thank you for using RMIT ticketing system. Have a good day.')
                    return
                case _:
                    print('Invalid input. Please select one of the given options.')
            user_choice = self.menu()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



operation_1 = Operations()
operation_1.run_operations()

        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




       


                
            





        















        


        
