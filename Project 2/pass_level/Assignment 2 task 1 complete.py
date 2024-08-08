#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#NAME        :  VIVEK AGGARWAL
#STUDENT ID  :  S4015465

#HIGHEST PART ATTEMPTED -> 1

#PROGRAMING FUNDAMENTAL ASSIGNMENT 2

#I Started by just defining the classes as mentioned in the assingment specifications which was relatively easy as the assignment mentions the exact specifications of the classes
#and their attributes. At first I didn't understand as to why we needed a get_ID or get_name function for every class but later on in the assigment I realised it makes the
#attribute easier and cleaner to access. I also declared a lot of other getter methods but removed them as i realised attributes like booking fee in a customer weren't really
#attributes, they were just being used to return a value to be used in other classes for calculations. It took me a over 2 weeks to accomplish part 1. The expense manager code
#was really helpful to make me understand the use of classes. It makes it easy to call control the program and store more data for each instance. As compared to assignment 1 where
#I used lists and dictionaries to store data, classes helped me store attributes for every individual element of those lists. As of now, the program reads data when initiated,
#from the file names given in the assignment. I have designed functions to input string and integer and float values from the user, and I got the idea from the expense manager
#code week 8. Using validations there and the code take input whereever needed, without having to put validation conditions everytime. 


#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Importing all the libraries we are allowed to use

import sys
import os

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

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

#......................................................................................................................

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

#......................................................................................................................

def get_float(prompt):

    input_float = get_string(prompt)
    while True:
        
        if not input_float.isdigit():
            print('Invalid input. Input must contain digits only. Please try again.')
            continue
        else:
            input_float = float(input_float)

            if input_float <= 0:
                print('Invalid input. Input value has to be a number greater than 0. Please try again.')
                continue
            else:
                return input_float
                       
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Customer:                                             #creating class Customer
    
    def __init__(self, ID, name):                           #initializing constructor method
        self.ID = ID                                        #initialising Customer.ID
        self.name = name                                    #initialising Customer.name

    def get_ID(self):                                       #getter method for Customer ID
        return self.ID

    def get_name(self):                                     #getter method for Customer name
        return self.name

    def get_discount(self, cost):                           #getter method to store ticket cost and return 0
        return 0

    def get_booking_fee(self, ticket_quantity):             #method to return booking fee
        booking_fee = ticket_quantity * 2                   #booking_fee = instance variable storing the cost of booking
        return booking_fee

    def display_info(self):                                 #method to display Customer ID and name
        print(f"Customer ID : {self.ID}, Customer name : {self.name}")
       
        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------


class RewardFlatCustomer(Customer):                         #creating new class RewardFlatCustomer that inherits from Customer class defined above

    discount_rate = 0.2                                     #static variable dicount_rate set to 20%

    def get_discount(self, cost):                           #get_discount = getter to get discount value                          \
        discount = cost * RewardFlatCustomer.discount_rate
        return discount
    
    def display_info(self):                                 #method to display information of all attributes
        print(f"Customer ID : {self.ID}, Customer name : {self.name}, Discount rate : {self.discount_rate}")

    @staticmethod                                           #static method set_discount_rate to update value of discount_rate
    def set_discount_rate(discount_rate):
        RewardFlatCustomer.discount_rate = discount_rate

    @staticmethod                                           #static method get_discount_rate to get the value of discount rate
    def get_discount_rate():
        return RewardFlatCustomer.discount_rate

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

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
        print(f"Customer ID : {self.ID}, Customer name : {self.name}, Discount rate : {self.discount_rate}, Threshold : {self.threshold}")
        
    def get_discount_rate(self):
        return self.discount_rate
    
    @staticmethod 
    def set_threshold(new_threshold):
        RewardStepCustomer.threshold = new_threshold

    @staticmethod 
    def get_threshold():
        return RewardStepCustomer.threshold
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Movie:            #creating class Movie

    def __init__(self, ID, name, seat_available):
        self.ID = ID
        self.name = name
        self.seat_available = seat_available

    def display_info(self):
        print(f"Movie ID : {self.ID}, Movie name : {self.name}, Seats available : {self.seat_available}")

    def get_ID(self):
        return self.ID  

    def get_name(self):
        return self.name

    def get_seat_available(self):
        return self.seat_available

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Ticket:
    
    def __init__(self, ID, name, price):
        self.ID = ID
        self.name = name
        self.price = float(price)
        
    def display_info(self):
        print(f"Ticket ID : {self.ID}, Ticket name : {self.name}, Ticket price : {self.price}")

    def get_ID(self):
        return self.ID

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
##
##class GroupTicket(Ticket):
##
##    def
##    
##

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

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
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------


class Records:

    customers = []
    movies = []
    tickets = []
    
##as of now we are storing all lists as static variables, but will fill the lists as instance variables
    
    
    def read_customers(self, file_name):

        try:
            with open(file_name,'r') as f:
                for line in f:
                    row = line.strip().split(",")
                    row = [x.strip() for x in row]
                    customer_ID = row[0].title()
                    customer_name = row[1].title()        #to save customer name with first letter in uppercase
            
                    if (row[0][0].upper() == 'C'):
                        customer = Customer(customer_ID, customer_name)

                    elif (row[0][0].upper() == 'F'):                        
                        customer = RewardFlatCustomer(customer_ID, customer_name)

                    elif (row[0][0].upper() == 'S'):
                        discount_rate = float(row[2])                                            
                        customer = RewardStepCustomer(customer_ID, customer_name, discount_rate)

                    else:
                        continue
                    
                    self.customers.append(customer)
            return True
        except:
            return False
                    


    def read_movies(self, file_name):

        try:
            
            with open(file_name,'r') as f1:
                for line in f1:
                    row = line.strip().split(",")
                    row = [y.strip() for y in row]

                    if (row[0][0].upper() !='M'):
                        continue
                    
                    movie_ID = row[0].title()
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
                    row = line.strip().split(",")
                    row = [z.strip() for z in row]

                    if (row[0][0].upper() !='T'):
                        continue
                    
                    ticket_ID = row[0].title()
                    ticket_name = row[1].title()
                    ticket_unit_price = row[2]

                    ticket = Ticket(ticket_ID, ticket_name, ticket_unit_price)

                    self.tickets.append(ticket)
            return True
        except:
            return False     #or pass

#..........................................................................................................

    def find_customer(self, customer_name):
##      column_format = "{:<" + str(dates_width) + "} {:<" + str(names_width) + "} {:>" + str(amounts_width) + "}\n"

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
       
        if self.tickets == []:
            print('There are no tickets to find. Try adding a few first. ')
            return None

        i = 0
        for ticket in self.tickets:
            if ticket.get_name() == ticket_name:
                return ticket

        if i == 0:
            return None
#....................................................................................


    def save_customers_data(self, file_name):
        try:
            file_object = open(file_name, "w")
            num_customers = len(self.customers)        
            i = 0
            while (i < num_customers):
                if isinstance(self.customer, Customer):
                    file_object.write(self.customer[i].get_ID() + "," + self.customer[i].get_name() + '\n')
                elif isinstance(self.customer, RewardFlatCustomer):
                    file_object.write(self.customer[i].get_ID() + "," + self.customer[i].get_name() + "," + self.customer[i].get_discount_rate()+ '\n')
                elif isinstance(self.customer, RewardStepCustomer):
                    file_object.write(self.customer[i].get_ID() + "," + self.customer[i].get_name() + "," + self.customer[i].get_discount_rate() + ',' + self.customer[i].get_threshold()+ '\n')
                i += 1
            file_object.close()
            return i
        except:
            pass
        
    def save_movies_data(self, file_name):
        try:
            file_object = open(file_name, "w")
            num_movies = len(self.movies)        
            i = 0
            while (i < num_movies):
                file_object.write(self.movies[i].get_ID() + "," + self.movies[i].get_name() + "," + str(self.movies[i].get_seat_available()) + "\n")
                i += 1
            file_object.close()
            return i
        except:
            pass

    def save_tickets_data(self, file_name):
        try:
            file_object = open(file_name, "w")
            num_tickets = len(self.tickets)        
            i = 0
            while (i < num_tickets):
                file_object.write(self.tickets[i].get_ID() + "," + self.tickets[i].get_name() + "," + str(self.tickets[i].get_price()) + "\n")
                i += 1
            file_object.close()
            return i
        except:
            pass        
                
#....................................................................................#
                                                                                     #
    def display_customers(self):                                                     #
        print("\n The details of all the existing customers are as follows:")        #
        for customer in self.customers:                                              #
            customer.display_info()                                                  #
                                                                                     #
    def display_movies(self):                                                        #
        print("\n The details of all the existing movies are as follows:")           #
        for movie in self.movies:                                                    #
            movie.display_info()                                                     #
                                                                                     #
    def display_tickets(self):                                                       #
        print("\n The details of all the existing ticket types are as follows:")     #
        for ticket in self.tickets:                                                  #   
            ticket.display_info()                                                    #       
                                                                                     #       
#....................................................................................#                                                              
                                                                                     #
    def generate_ID(self, type_of_list, type_of_ID):                                 #
                                                                                     #
        x = type_of_list.lower().strip()                                             #
        y = type_of_ID.title().strip()                                               #
                                                                                     #
        object_list = []                                                             #
        refined_list = []                                                            #
                                                                                     #
        if x == 'customers':                                                         #
            object_list =  self.customers                                            #
        elif x == 'movies':                                                          #
            object_list =  self.movies                                               #
        elif x == 'tickets':                                                         #
            object_list =  self.ticekts                                              #
        else:                                                                        #
            print(f"There is no attribute '{x}' in records.")                        #
                                                                                     #
        for object in object_list:                                                   #
            if object.get_ID().startswith(y):                                        #
                refined_list.append(object.get_ID())                                 #
                                                                                     #
        max_ID = max(refined_list)                                                   #
        new_ID_num = int(max_ID[1:]) + 1                                             #
        new_ID = y + str(new_ID_num)                                                 #
                                                                                     #
        return new_ID                                                                #
                                                                                     #
#....................................................................................#




#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

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
5. Add new movies
6. Adjust the discount rate of all RewardFlat Customers
7. Adjust the discount rate of a RewardStep Customer
8. Display all bookings
9. Display the most popular movie
10. Display all movie records
0. Exit the program''')
        print('*'*60)                                    #given user all information regarding choosing an option


        user_choice = input("Please choose any one of the options given above__").strip()

        return user_choice

#......................................................................

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

#........................................................................
    
    def purchase_ticket(self):
        
        user_name = get_string('Please enter your name__')
        customer = self.record.find_customer(user_name)


        if customer == None:
            input_invalid = True

            while input_invalid:
                choice_1 = input("Do you wish to join any rewards program? Enter 'y' for yes or 'n' for no__")

                if (choice_1 == 'y' or choice_1 == 'Y'):
                    print('You have chosen to become a part of our rewards program.')

                    while input_invalid:
                        choice_2 = input("Enter 's' to become a Reward Step Customer, or 'f' to become a Reward Flat Customer__")
                        if (choice_2 == 's' or choice_2 == 'S'):
                            user_ID = self.record.generate_ID('customers', 'S')
                            customer = RewardStepCustomer(user_ID, user_name)
                            self.record.customers.append(customer)
                            input_invalid = False

                        elif (choice_2 == 'f' or choice_2 == 'F'):
                            user_ID = self.record.generate_ID('customers', 'F')
                            customer = RewardFlatCustomer(user_ID, user_name)
                            self.record.customers.append(customer)
                            input_invalid = False

                        else:
                            print('Sorry, invalid input. Please enter one of the given options.')
                            
                elif (choice_1 == 'n' or choice_1 == 'N'):
                    print('You have chosen not to become a part of our rewards program.')
                    user_ID = self.record.generate_ID('customers', 'C')
                    customer = Customer(user_ID, user_name)
                    self.record.customers.append(customer)
                    input_invalid = False

                else:
                    print('Sorry, invalid input. Please enter one of the given options.')
           
        
        movie_name = get_string('Please enter movie name__')
        movie = self.record.find_movie(movie_name)
                
        ticket_name = get_string('Please enter the ticket type__')
        ticket = self.record.find_ticket(ticket_name)

        ticket_quantity = get_integer('Please enter the number of tickets you wish to purchase__')

        
        booking = Booking(customer, movie, ticket, ticket_quantity)
        booking_details = booking.compute_cost()

        total_cost = booking_details[0]
        booking_fee = booking_details[1]
        total_discount = booking_details[2]
        final_cost = total_cost - total_discount
        
        print('\n\n')
        print('-' * 45)
        print(f"Receipt of {customer.get_name()}")
        print('-' * 45)
        print("{:<25}{:>20}".format("Movie",movie.get_name()))
        print("{:<25}{:>20}".format("Ticket type",ticket.get_name()))
        print("{:<25}{:>20}".format("Ticket unit price",ticket.get_price()))
        print("{:<25}{:>20}".format("Ticket quantity",ticket_quantity))
        print('-' * 45)
        print("{:<25}{:>20.2f}".format("Discount",total_discount))
        print("{:<25}{:>20}".format("Booking fee",booking_fee))
        print("{:<25}{:>20}".format("Total cost",final_cost))
        print('-' * 45)
        
        
        

        
#..................................................................

    def adjust_discount_rate_for_RewardFlatCustomer(self):
        new_discount_rate = get_float("Please enter the new discount rate you wish to set for all RewardFlat Customers")
        converted_discount_rate = new_discount_rate / 100
        RewardFlatCustomer.set_discount_rate(converted_discount_rate)
        print(f"New discount rate '{new_discount_rate}%' of RewardFlat Customers has been set successfully")
               
#...................................................................

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
                case '5':
                    pass
                case '6':
                    self.adjust_discount_rate_for_RewardFlatCustomer()                    
                case '0':
                    print('Thank you for using RMIT ticketing system. Have a good day.')
                    return
                case _:
                    print('Invalid input. Please select one of the given options.')
            user_choice = self.menu()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------


operation_1 = Operations()
operation_1.run_operations()

        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

##
##def read_bookings(self, file_name):
##
##        try:            
##            with open(file_name,'r') as f3:
##                for line in f3:
##                    row = line.strip().split(",")
##                    row = [w.strip() for w in row]
##
##                    customer_ID = row[0]
##                    movie_ID = row[1]
##
##                    if (row[0][1].isdigit()):
##                        
##                    else:
##                        
##                        
##                        
##                    
##                    ticket_ID = row[0]
##                    ticket_name = row[1].title()
##                    ticket_unit_price = row[2]
##
##                    ticket = Ticket(ticket_ID, ticket_name, ticket_unit_price)
##
##                    self.tickets.append(ticket)
##            return True
##        except:
##            return False     #or pass




                
            





        















        


        
