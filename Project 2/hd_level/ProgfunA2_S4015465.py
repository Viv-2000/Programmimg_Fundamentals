#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#NAME        :  VIVEK AGGARWAL
#STUDENT ID  :  S4015465

#HIGHEST PART ATTEMPTED -> HD

#PROGRAMING FUNDAMENTAL ASSIGNMENT 2

'''I started by defining the classes as mentioned in the assignment specifications, which was relatively easy since the assignment provided the exact specifications
for the classes and their attributes. Initially, I didn't understand why we needed get_ID or get_name functions for every class, but later on, I realized that these
functions make it easier and cleaner to access the attributes. I also declared several other getter methods but removed them when I realized that attributes like
booking fee in a customer weren't really attributes; they were just being used to return a value for calculations in other classes. It took me over 2 weeks to complete
part 1. The expense manager code from week 8 was really helpful in understanding the use of classes. It makes it easier to control the program flow and store more data
for each instance. Compared to assignment 1, where I used lists and dictionaries to store data, using classes helped me store attributes for each individual element more
efficiently. Currently, the program reads data from the files specified in the assignment when initiated. I have designed functions to input string, integer, and float
values from the user, taking inspiration from the expense manager code from week 8. By using validations in those functions, I can take input wherever needed without
having to add validation conditions every time.

After defining all the classes, I started to see everything falling into place as I implemented the class operations and records. Handling errors was relatively
simple, as we had already done it in the first assignment. I have included error messages for all possible issues the user might face. Task 1 was completed quite
easily. For task 2, we were asked to integrate group tickets into our system, which was done by creating a GroupTicket class. I also had to modify the read_tickets
function to handle group tickets.

The Generate_ID function is designed to take two parameters: the list of respective objects and the ID types. This was the most challenging part of the task.

Finally, for task 3, we needed to allow the user to buy multiple tickets in a single booking. This was accomplished by using lists for ticket types and ticket
quantities, similar to assignment 1. The Booking class was modified to accept a list of ticket types, respective quantities, and return the effective total cost
of the entire booking, including the booking fee and discount. This information was then used to print the receipt for the booking, with a for loop used to display
all the ticket types and their respective quantities, and so on.

I have tried to keep the code as clean as possible by creating functions for specific tasks. The most challenging part was modifying
the Booking class to accept bookings from both predefined bookings in the booking file and new bookings made by customers. Saving data
was relatively easy, as we simply wrote the data back into the files in the desired format.

I only used one online site apart from the RMIT material available in th ecanvas. Its link is shared below. 
 References used:
https://www.w3schools.com/python/ref_func_all.asp '''

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------





#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<     Importing all the libraries we are allowed to use      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

import sys
import os

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------





#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<     Defining some custom exceptions that will be raised later in the code     >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

class BlankInputError(Exception):
    pass

class InvalidInputError(Exception):
    pass

class InvalidChoiceError(Exception):
    pass

class InvalidDataTypeError(Exception):
    pass

class MatchNotFoundError(Exception):
    pass

class DataListEmpty(Exception):
    pass

class DataNotSavedError(Exception):
    pass

class UnknownComputationalError(Exception):
    pass

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------





#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<     Defining some global functions that will  be used in the code later     >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

def get_string(prompt):                                          #get_string is a function with a few validation rules to get an input string from the user
    
    while True:
        try:
            sys.stdout.write(prompt)
            sys.stdout.flush()
            input_string = sys.stdin.readline().strip().title()      #str.strip() to strip spaces, str.title() to capitalize first letter

            if (len(input_string) == 0):                             #if condition to make sure input is not blank
                raise BlankInputError("Sorry, input cannot be blank.")

            elif not input_string.isalnum():                         #if condition to make sure input contains only alphanumerical characters
                raise InvalidInputError("Invalid input. Input must contain alphabets or digits only.")

            else:
                return input_string                                  #returns the input string if it is valid
        except BlankInputError as e:
            print(str(e))
            continue
        except  InvalidInputError as e:
            print(str(e))
            continue
            

#................................................................................................................................................................

def get_list(prompt):                                   #get_list is a function to let the user input a string of comma seperated elements

    while True:                                         #while loop to ensure user doesn't enter a blank list
        try:
            sys.stdout.write(prompt)
            sys.stdout.flush()
            input_string = sys.stdin.readline().strip() #readline() function to read the input line

            input_list = [x.strip().title() for x in input_string.split(",")]     #string comprehension, title() and str.split() ,split the string and strip spaces
            if any(len(x) == 0 for x in input_list):
                raise BlankInputError('Invalid input, elements of the input list cannot be blank.')
            else:
                return input_list                       #returns the input list
            
        except BlankInputError as e:                                         #except statement to continue the while loop if any error
            print(str(e))

#................................................................................................................................................................

def get_integer(prompt):                                #get_integer is a function with a few validation rules to get an input integer from the user
    
    while True:
        try:                                            #try statement to try converting input into int
            input_integer = input(prompt)
            input_integer = int(input_integer)

            if input_integer <= 0:                      #if condition for checking input being a positive integer
                raise InvalidInputError('Invalid input. Input value has to be a number greater than 0. Please try again.')
            else:
                return input_integer                    #returns the inout integer if it is valid

        except ValueError:                                         #except statement to continue while loop if there is any type of error during try statement
            print('Invalid input. Input must contain digits only. Please try again.')
            continue
        except InvalidInputError as e:
            print(str(e))

#................................................................................................................................................................

def get_float(prompt):                          #get_float is a function with a few validation rules to get an input float from the user

    while True:                                 #while loop runs till user inputs a valid float
        try:                                    #try statement to try converting input into float
            input_float = input(prompt)    
            input_float = float(input_float)

            if input_float <= 0 or input_float > 1:
                print('Invalid input. Input value has to be a number greater than 0, and less than 1. Please try again.')
            else:
                return input_float              #returns the input float if it is valid
            
        except:                                 #except statement to continue while loop if there is any type of error during try statement
            print('Invalid input. Please enter a float value.')

#................................................................................................................................................................
                                                                                     
def generate_ID(target_list, ID_type):          #generate_ID() takes 2 parameters, one is a list and second is the type of ID, to generate and return a new_ID

    try:                                                                                                                                
        ID_type = ID_type.title().strip()       #str.strip() and str.title() to make sure the first letter is capital and no spaces are passed                                      
                                                             
        refined_list = []                       #refined list is an empty list that will store all the existing IDs of the ID_type entered                                                                                                                                            
        for obj in target_list:                 #for loop to iterate through the target list and filter all the ojects with same ID type                                     
            if obj.get_ID().startswith(ID_type):                                           
                refined_list.append(int(obj.get_ID()[1:]))  #list.append() to append the integer part of the ID in the refined list                        
                                                                                     
        max_ID = max(refined_list)              #max() funciton to find the maximum value that exists in the list                                        
        new_ID_num = int(max_ID) + 1            #the new_ID_num stores the integer part of the new ID that is being created                                      
        new_ID = ID_type + str(new_ID_num)      #new_ID stores the complete new ID, by concatinating the ID_type with the integer we just generated in line above                                             
                                                                                     
        return new_ID                           #returns the generated new ID
    except:
        pass

                                                                                                          
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<     End of creating global functions        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#----------------------------------------------------------------------------------------------------------------------------------------------------------------






#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<     Creating and defining the required classes mentioned in the assignment     >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
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

    def display_info(self):                                 #method to display Customer ID and name in the desired format
        print(f"Customer ID : {self.ID}, Customer name : {self.name}")
       
        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------





#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------


class RewardFlatCustomer(Customer):                         #creating new class RewardFlatCustomer that inherits from Customer class defined above

    discount_rate = 0.2                                     #static variable dicount_rate set to 20%, for all rewardflat customers

    def get_discount(self, cost):                           #get_discount = getter to get discount value                          \
        discount = cost * RewardFlatCustomer.discount_rate
        return discount
    
    def display_info(self):                                 #method to display information of all attributes as per desired format
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

class RewardStepCustomer(Customer):                         #creating new class RewardStepCustomer that inherits from Customer class defined above
    
    threshold = 50                                          #default threshold is set to 50
    
    def __init__(self, ID, name, discount_rate=.3):         #default discount_rate is 30%, unless corresponding argument passed during object creation
        super().__init__(ID, name)                          #super() function to use the same constructor in customer class, ans also adding modifications
        self.discount_rate = discount_rate
    
    def get_discount(self, cost):                           #get_discount returns the corresponding discount
        if cost >= RewardStepCustomer.threshold:            #if coundition to check whether cost satisfies threshold criteria
            self.discount = cost * self.discount_rate
            return self.discount
        else:                                               #else returns 0 discount if cost is less than threshold
            self.discount = 0
            return self.discount
    
    def display_info(self):                                 #display function to display all attributes of rewardstep customers in desired format
        print(f"Customer ID : {self.ID}, Customer name : {self.name}, Discount rate : {self.discount_rate}, Threshold : {self.threshold}")
        
    def get_discount_rate(self):                            #getter method to return self discount rate of the customer
        return self.discount_rate
    
    @staticmethod                                           #static function to set the update the threshold when needed
    def set_threshold(new_threshold):
        RewardStepCustomer.threshold = new_threshold

    @staticmethod                                           #static function to get the static threshold for all rewardstep customers
    def get_threshold():
        return RewardStepCustomer.threshold
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------





#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Movie:            #creating class Movie

    def __init__(self, ID, name, seat_available, ticket_dict = dict()):
        self.ID = ID
        self.name = name
        self.seat_available = seat_available
        self.revenue = 0
        self.ticket_dict = ticket_dict

    def display_info(self):
        print(f"Movie ID : {self.ID}, Movie name : {self.name}, Seats available : {self.seat_available}")

    def update_revenue(self, new_sale_revenue):
        self.revenue += new_sale_revenue
    
    def get_ID(self):
        return self.ID  

    def get_name(self):
        return self.name

    def get_seat_available(self):
        return self.seat_available

    def get_revenue(self):
        return self.revenue

    def update_seats(self, tickets_info):
        for i in range(0, len(tickets_info), 2):
            self.ticket_dict[tickets_info[i]] += tickets_info[i+1]

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------





#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Ticket:
    
    def __init__(self, ID, name, price):
        self.ID = ID
        self.name = name
        self.price = float(price)
        self.no_of_seat = 1
        
    def display_info(self):
        print(f"Ticket ID : {self.ID}, Ticket name : {self.name}, Ticket price : {self.price}")

    def get_ID(self):
        return self.ID

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price

    def get_no_of_seat(self):
        return self.no_of_seat
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------





#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

class GroupTicket(Ticket):

    def __init__(self, ID, name, ticket_components, ticket_list):
        self.ID = ID
        self.name = name
        self.ticket_components = ticket_components
        self.no_of_seat = 0

        ticket_price = 0
        for i in range(0,len(ticket_components),2):
            t_comp = self.ticket_components[i].title()
            t_quant = int(self.ticket_components[i+1])
            
            for ticket in ticket_list:
                if ticket.get_name() == t_comp or ticket.get_ID == t_comp:
                    ticket_price += (ticket.get_price() * t_quant)

        final_price = ticket_price * 0.8
        self.price = final_price

        for i in range(1,len(self.ticket_components),2):
            self.no_of_seat += int(self.ticket_components[i])

    def get_no_of_seat(self):                       
        return self.no_of_seat
                
             
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#<<<<<<<<<<<<<<<<<<     All the basic classes for all types of customers, movies and tickets have been created and defined    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#----------------------------------------------------------------------------------------------------------------------------------------------------------------





#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#<<<<<<<<<<<<<<   This booking class is for storing every booking and its attributes, makes code efficient and useful for further applications    >>>>>>>>>>>>>>>
#----------------------------------------------------------------------------------------------------------------------------------------------------------------


class Booking:

    def __init__(self, customer, movie, tickets_info, discount = 0, booking_fee = 0, final_cost = 0):
        self.customer = customer
        self.movie = movie
        self.tickets_info = tickets_info
        self.discount = discount
        self.booking_fee = booking_fee
        self.final_cost = final_cost
        
    def compute_cost(self):
        ticket_list = self.tickets_info[::2]
        quantity_list = self.tickets_info[1::2]
        total_quantity = sum(quantity_list)
        total_cost = 0        

        empty_list = []
        for ticket, t_quan in zip(ticket_list, quantity_list):        
            total_cost += ticket.get_price() * t_quan
            empty_list.append(ticket.get_name())
            empty_list.append(str(t_quan))

        self.tickets_info = empty_list

        self.discount = self.customer.get_discount(total_cost)
        self.booking_fee = self.customer.get_booking_fee(total_quantity)
        self.final_cost = total_cost - self.discount + self.booking_fee
        
        return total_cost, self.booking_fee, self.discount

    def display_info(self):
        print(f"{self.customer.get_name()}, {self.movie.get_name()}, {', '.join(self.tickets_info)}, {self.discount}, {self.booking_fee}, {self.final_cost}")

    def get_customer(self):
        return self.customer

    def get_movie(self):
        return self.movie

    def get_tickets_info(self):
        return self.tickets_info

    def get_final_cost(self):
        return self.cost

    def get_booking_fee(self):
        return self.booking_fee

    def get_discount(self):
        return self.discount
    

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------





#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#<<<<<<<<<<<<<<<<<<<<<<<<     Class records, keeps all the records for customers, movies etc as list of objects, as static variables    >>>>>>>>>>>>>>>>>>>>>>>>>
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Records:

    customers = []
    tickets = []
    movies = []
    bookings = []

    all_ticket_names = dict()
    
##as of now we are storing all lists as static variables, but will fill the lists as instance variables
    
#................................................................................................................................................................
##### All the read_data functions, that read the data in the given files
#................................................................................................................................................................
    
    def read_customers(self, file_name):
        try:
            with open(file_name,'r') as f:
                for line in f:
                    row = [x.strip().title() for x in line.split(",")]
                    customer_ID = row[0]
                    customer_name = row[1]        #to save customer name with first letter in uppercase
            
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

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def read_movies(self, file_name):
        try:            
            with open(file_name,'r') as f1:
                for line in f1:
                    row = [y.strip().title() for y in line.split(",")]

                    if (row[0][0].upper() !='M'):
                        continue
                    
                    movie_ID = row[0]
                    movie_name = row[1]
                    seats_available = int(row[2])

                    movie = Movie(movie_ID, movie_name, seats_available) #, self.all_ticket_names
                    self.movies.append(movie)
                    
            return True
        except:
            return False  

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def read_tickets(self, file_name):
        try:            
            with open(file_name,'r') as f2:
                for line in f2:
                    row = [z.strip().title() for z in line.split(",")]
                    ticket_ID = row[0]
                    ticket_name = row[1]

                    if (ticket_ID.startswith('T')):                        
                        ticket_unit_price = float(row[2])
                        ticket = Ticket(ticket_ID, ticket_name, ticket_unit_price)
                        self.tickets.append(ticket)
                        self.all_ticket_names[ticket.get_name()] = 0

                    elif (ticket_ID.startswith('G')):
                        ticket_list = self.tickets
                        ticket_components = row[2:]
                        ticket = GroupTicket(ticket_ID, ticket_name, ticket_components, ticket_list)
                        if ticket.get_price() < 50:
                            print(f'Sorry, this ticket {ticket_ID} does not satisfy GroupTicket criteria.')
                        else:
                            self.tickets.append(ticket)
                            self.all_ticket_names[ticket.get_name()] = 0
                    else:
                        continue
    
            return True
        except:
            return False            

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def read_bookings(self, file_name):
        try:            
            with open(file_name,'r') as f3:
                for line in f3:                    
                    row = [w.strip().title() for w in line.strip().split(",")]

                    customer = self.find_customer(row[0])
                    movie = self.find_movie(row[1])
                    tickets_info = row[2:-3]            #a list with alternate ticket type at even indices and quantity at odd indices
                    discount = float(row[-3])
                    booking_fee = float(row[-2])
                    final_cost = float(row[-1])

                    movie.update_revenue(final_cost)
                    #movie.update_seats(tickets_info)

                    booking = Booking(customer, movie, tickets_info, discount, booking_fee, final_cost)
                    self.bookings.append(booking)
            return True
        except:
            return False     



#................................................................................................................................................................
##### All the find_data functions, that find the respective data in the system lists
#................................................................................................................................................................

    def find_customer(self, customer_info):
##      column_format = "{:<" + str(dates_width) + "} {:<" + str(names_width) + "} {:>" + str(amounts_width) + "}\n"

        if self.customers == []:
            print('There are no customers to find. Try adding a few first. ')
            return None
        
        i = 0
        for customer in self.customers:
            if customer.get_name() == customer_info or customer.get_ID() == customer_info:
                return customer

        if i == 0:
            return None

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def find_movie(self, movie_info):

        if self.movies == []:
            print('There are no movies to find. Try adding a few first. ')
            return None
        
        i = 0
        for movie in self.movies:
            if movie.get_name() == movie_info or movie.get_ID() == movie_info:
                return movie

        if i == 0:
            return None

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def find_ticket(self, ticket_info):
       
        if self.tickets == []:
            print('There are no tickets to find. Try adding a few first. ')
            return None

        i = 0
        for ticket in self.tickets:
            if ticket.get_name() == ticket_info or ticket.get_ID() == ticket_info:
                return ticket

        if i == 0:
            return None


        
#................................................................................................................................................................
##### All the save_data functions, that save the correspoding data into respective files
#................................................................................................................................................................

    def save_customers_data(self, file_name):
        try:
            file_object = open(file_name, "w")
            num_customers = len(self.customers)        
            i = 0
            while (i < num_customers):
                if isinstance(self.customer, Customer):
                    file_object.write(self.customer[i].get_ID() + "," + self.customer[i].get_name() + '\n')
                elif isinstance(self.customer, RewardFlatCustomer):
                    file_object.write(self.customer[i].get_ID() + "," + self.customer[i].get_name() + "," + RewardFlatCustomer.get_discount_rate()+ '\n')
                elif isinstance(self.customer, RewardStepCustomer):
                    file_object.write(self.customer[i].get_ID() + "," + self.customer[i].get_name() + "," + self.customer[i].get_discount_rate() + ',' + RewardStepCustomer.get_threshold()+ '\n')
                i += 1
            file_object.close()
            return i
        except:
            pass

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -        

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

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def save_bookings_data(self, file_name):
        try:
            file_object = open(file_name, "w")
            num_bookings = len(self.bookings)        
            i = 0
            while (i < num_bookings):
                file_object.write(self.bookings[i].get_name() + "," + self.bookings[i].get_name() + "," + str(self.bookings[i].get_discount())+"," + str(self.bookings[i].get_booking_fee())+"," + str(self.bookings[i].get_final_cost()) + "\n")
                
                i += 1
            file_object.close()
            return i
        except:
            pass


                
#................................................................................................................................................................
##### All the display_data functions, that print the respective data present in the system 
#................................................................................................................................................................                                                                                     #
                                                                                     #
    def display_customers(self):                                                     #
        print("\n The details of all the existing customers are as follows :")       #
        for customer in self.customers:                                              #
            customer.display_info()                                                  #
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   #
    def display_movies(self):                                                        #
        print("\n The details of all the existing movies are as follows :")          #
        for movie in self.movies:                                                    #
            movie.display_info()                                                     #
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   #
    def display_tickets(self):                                                       #
        print("\n The details of all the existing ticket types are as follows :")    #
        for ticket in self.tickets:                                                  #   
            ticket.display_info()                                                    #                                                                                                                                                                                                                                                                 
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   #
    def display_bookings(self):                                                      #
        print("\n The details of all the existing bookings are as follows :")        #
        for booking in self.bookings:                                                #   
            booking.display_info()                                                   #       
                                                                                     #                                                                                                                                                                             
#................................................................................................................................................................

    def add_movies(self):                   #this function asks user to enter a list of new movies, and adds the new movie if they do not already exist    
        new_movie_list = get_list('Please enter a list of new movie names, seperated by commas__')          #calling get_list() to let the user enter a list

        for new_movie_name in new_movie_list:               #for loop iterates through the entered movie list
                                  
            if any(new_movie_name == movie.get_name() for movie in self.movies):      #if condition checks whether new movie exists already or not, and conveys corresponding message
                print(f"The movie '{new_movie_name}' already exists in the system.")
                                                            #if  movie exists, next item in enetered movie list is processed
            else:                                           #if there is no match, then this else statement is executed                  
                new_movie_ID = generate_ID(self.movies, 'M')               #generating new movie ID
                new_movie = Movie(new_movie_ID , new_movie_name, 50)       #creating class for the new movie
                self.movies.append(new_movie)                              #appending the new movie into the movie list
                print(f"New movie {new_movie_name} with a new movie ID '{new_movie.get_ID()}' has been added to the system with 50 seats.")

#................................................................................................................................................................

    def display_most_pop(self):
        revenue_list = [movie.get_revenue() for movie in self.movies]
        max_revenue = max(revenue_list)
        index_most_pop = revenue_list.index(max_revenue)
        print(f"The most popular movie up till now is '{self.movies[index_most_pop].get_name()}' with an astonishing revenue of $'{self.movies[index_most_pop].get_revenue()}'.")

                            
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------





#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Operations:

    record = Records()

    def menu(self):                                             #This function is to give the user all the options to choose from 
        print('\n\n')
        print("Welcome to RMIT movie ticketing system.") 
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
        print('*'*60)                                    

        user_choice = input("Please choose any one of the options given above__").strip()

        return user_choice                                      #returns the choice user makes

#................................................................................................................................................................
   
    def load_data(self, c_file, m_file, t_file, b_file):                                        #This function calls all the reading functions to read the data from all given files
        if not self.record.read_customers(c_file):              #reading customer data from customer file 
            print(f"Sorry, the file '{c_file}' is missing.")
            return False

        if not self.record.read_tickets(t_file):                #reading ticekts data from tickets file
            print(f"Sorry, the file '{t_file}' is missing.")
            return False
                       
        if not self.record.read_movies(m_file):                 #reading movies data from movies file
            print(f"Sorry, the file '{m_file}' is missing.")
            return False

        if b_file:
            if not self.record.read_bookings(b_file):
                print(f"Sorry, the file '{b_file}' is missing.")
                return False

        return True

#................................................................................................................................................................
    
    def purchase_ticket(self):
        
        user_name = get_string('Please enter your name__')
        customer = self.record.find_customer(user_name)

        ################# This part of code checks whether customer is an existing one or new #######################
        if customer is None:
            user_choice = input("Do you wish to join any rewards program? Enter 'y' for yes or 'n' for no__")

            while user_choice not in ['y', 'Y', 'n', 'N']:
                print('Sorry, invalid input. Please enter one of the given options.')
                user_choice = input("Do you wish to join any rewards program? Enter 'y' for yes or 'n' for no__")

            if user_choice in ['y', 'Y']:
                print('You have chosen to become a part of our rewards program.')
                program_type = input("Enter 's' to become a Reward Step Customer, or 'f' to become a Reward Flat Customer__")

                while program_type not in ['s', 'S', 'f', 'F']:
                    print('Sorry, invalid input. Please enter one of the given options.')
                    program_type = input("Enter 's' to become a Reward Step Customer, or 'f' to become a Reward Flat Customer__")

                if program_type in ['s', 'S']:
                    new_user_ID = generate_ID(self.record.customers, 'S')
                    customer = RewardStepCustomer(new_user_ID, user_name)
                else:
                    new_user_ID = generate_ID(self.record.customers, 'F')
                    customer = RewardFlatCustomer(new_user_ID, user_name)

            else:
                print('You have chosen not to become a part of our rewards program.')
                user_ID = generate_ID(self.record.customers, 'C')
                customer = Customer(user_ID, user_name)

            self.record.customers.append(customer)


        ############## This block of code is to get a valid movie input from the user, using while loop #############           
        movie_invalid = True  
        while movie_invalid:                
            movie_name = get_string('Please enter movie name or movie ID__')
            movie = self.record.find_movie(movie_name)
            if movie is None:
                print('Sorry, this movie does not exist yet. Either add the movie or please select another one.')
                continue            
            if movie.get_seat_available() == 0:
                print('Sorry, this movie currently has no available seats. Please select another movie.')
            else:
                movie_invalid = False



        ######## This block of code is to get valid lists input for ticket types and ticket quantities from the user, using while loops and if conditions #######
        lists_invalid = True
        while lists_invalid:                           

            ticket_list = get_list('Please enter a list of ticket names or ticket IDs, seperated by commas__')

            if any(self.record.find_ticket(ticket_name) == None for ticket_name in ticket_list):
                print('Sorry, not every ticket in the input ticket list is valid. Please try again.')
                continue
            else:
                ticket_list = [self.record.find_ticket(ticket) for ticket in ticket_list]
                 
            quantity_list = get_list('Please enter the number of tickets you wish to purchase for the respective ticket type, seperated by commas__')

            try:
                quantity_list = [int(h) for h in quantity_list]
            except:
                print('Sorry, not all elements entered were valid integers. Please try again. ')
                continue
            
            if any(t_quan <1 for t_quan in quantity_list) or (len(ticket_list) != len(quantity_list)):
                print('Sorry, please try again. Either a quanitity was less than 1, or the number of elements in the input lists are not equal.')
                continue            
                
            total_quantity = sum(quantity_list)
            actual_seat_quantity = 0
            for ticket, t_quan in zip(ticket_list, quantity_list):                
                actual_seat_quantity += t_quan * ticket.get_no_of_seat()

            if actual_seat_quantity > int(movie.get_seat_available()):
                print('Sorry, this number exceeds the number of seats available for this movie. Please select a smaller quantity or another movie.')
                continue

            lists_invalid = False

        movie.seat_available -= actual_seat_quantity

        tickets_info = []
        tickets_info_with_names = []
        for ticket, t_quan in zip(ticket_list, quantity_list):
            tickets_info.append(ticket)
            tickets_info_with_names.append(ticket.get_name())
            tickets_info.append(t_quan)
            tickets_info_with_names.append(t_quan)

        #movie.update_seats(tickets_info_with_names)
       
        booking = Booking(customer, movie, tickets_info)
        self.record.bookings.append(booking)
        booking_details = booking.compute_cost()

        total_cost = booking_details[0]
        booking_fee = booking_details[1]
        total_discount = booking_details[2]
            
        final_cost = total_cost - total_discount + booking_fee
            

        ################## The following code is to print the receipt of the booking for the user ##############
        print('\n\n')
        print('-' * 45)
        print(f"Receipt of {customer.get_name()}")
        print('-' * 45)
        print("{:<25}{:>20}".format("Movie",movie.get_name()))

        for ticket, t_quan in zip(ticket_list, quantity_list):
            print(".........".center(45))
            print("{:<25}{:>20}".format("Ticket type",ticket.get_name()))
            print("{:<25}{:>20}".format("Ticket unit price",ticket.get_price()))
            print("{:<25}{:>20}".format("Ticket quantity",t_quan))

        print('-' * 45)
        print("{:<25}{:>20.2f}".format("Discount",total_discount))
        print("{:<25}{:>20}".format("Booking fee",booking_fee))
        print("{:<25}{:>20}".format("Total cost",final_cost))
        print('-' * 45)

        
#................................................................................................................................................................
    
    def adjust_disc_rate_Flat(self):            #This function adjusts the discount rate for all reward flat customers
        new_discount_rate = get_float("Please enter the new discount rate you wish to set for all RewardFlat Customers__")
        RewardFlatCustomer.set_discount_rate(new_discount_rate)
        print(f"New discount rate '{new_discount_rate * 100}%' of RewardFlat Customers has been set successfully.")
              
#................................................................................................................................................................
    def save_data(self):
        self.record.save_customers_data(c_file)
        self.record.save_movies_data(m_file)
        self.record.save_bookings_data(b_file)


    
    def adjust_disc_rate_Step(self):
        while True:
            try:
                customer_info = get_string('Please enter the customer ID or customer name__')
                customer = self.record.find_customer(customer_info)
                if customer == None:
                    print('Sorry, customer not found. Please try again.')
                elif not isinstance(customer,RewardStepCustomer):
                    print('Sorry, this customer is not a part of RewardStep Program. Please try again.')
                else:
                    new_discount_rate = get_float(f"Please enter the new discount rate you wish to set for {customer.get_name()}__")
                    customer.discount_rate = new_discount_rate
                    print(f"The discount rate for {customer.get_name()} has been successfully updated to '{new_discount_rate * 100}%'.")
                    return
            except:
                pass
        
#................................................................................................................................................................

    def run_operations(self, c_file, m_file, t_file, b_file):

        if not self.load_data(c_file, m_file, t_file, b_file):
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
                    self.record.add_movies()
                case '6':
                    self.adjust_disc_rate_Flat()
                case '7':
                    self.adjust_disc_rate_Step()
                case '8':
                    self.record.display_bookings()
                case '9':
                    self.record.display_most_pop()
                case '0':
                    self.save_data()
                    print('Thank you for using RMIT ticketing system. Have a good day.')
                    return
                case _:
                    print('Invalid input. Please select one of the given options.')
            user_choice = self.menu()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------





#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
sys_arguments = sys.argv

if len(sys_arguments) == 3:            
    c_file = sys_arguments[0]
    m_file = sys_arguments[1]
    t_file = sys_arguments[2]
    b_file = None

elif len(sys_arguments) == 4:
    c_file = sys_arguments[0]
    m_file = sys_arguments[1]
    t_file = sys_arguments[2]
    b_file = sys_arguments[3]

else:
    c_file = 'customers.txt'
    m_file = 'movies.txt'
    t_file = 'tickets.txt'
    b_file = None


operation_1 = Operations()
operation_1.run_operations(c_file, m_file, t_file, b_file)

        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------





    






                
            





        















        


        
