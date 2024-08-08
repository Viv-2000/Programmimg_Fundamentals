#NAME        :  VIVEK AGGARWAL
#STUDENT ID  :  S4015465

#PROGRAMING FUNDAMENTAL ASSIGNMENT 2

#CURRENTLY I HAVE JUST DESIGNED THE CLASSES, AND HAVENT LINKED THEM YET TO ANY OBJECT YET.



#####################################################################################


def get_string(prompt):
    print(promt)
    input_string = sys.stdin.readline().strip().title()
    return input_string

def get_integer(prompt):
    print(prompt)
    while True:
        input_integer = sys.stdin.readline().strip()
        if not isnum(input_integer) and input_integer < 1 :
            print('Invalid input. Please try again')
            break
    return input_integer

class Customer:                                             #creating class Customer
    
    def __init__(self, ID, name):                           #initializing constructor method
        self.ID = ID                                        #initialising Customer.ID
        self.name = name                                    #initialising Customer.name

    def get_ID(self):                                       #get_ID() = getter method for Customer ID
        return self.ID

    def get_name(self):                                     #get_name() = getter method for Customer name
        return self.name

    def get_discount(self, cost):                           #get_discount() = method to store ticket cost and return 0
        self.ticket_cost = cost
        return 0

    def get_ticket_cost(self):                              #get_ticket_cost() = getter method for individual ticket cost
        return self.ticket_cost

    def get_booking_fee(self, ticket_quantity):             #get_booking_fee() = method to store ticket quantity and return booking fee
        self.ticket_quantity = ticket_quantity
        self.booking_fee = ticket_quantity * 2              #booking_fee = instance variable storing the cost of booking
        return self.booking_fee

    def get_ticket_quantity(self):                          #get_ticket_quantity = getter method for ticket quantity
        return self.ticket_quantity

    def display_info(self):                                 #display_info() = method to display Customer ID and name
        print('{:<15}{:>20}'.format("Customer ID :", self.ID))
        print('{:<15}{:>20}'.format("Customer name :", self.name))
        print('{:<15}{:>20}'.format("Ticket cost :", self.ticket_cost))
        print('{:<15}{:>20}'.format("Ticket quantity :", self.ticket_quantity))
       
        

#######################################################################################


class RewardFlatCustomer(Customer):                         #creating new class RewardFlatCustomer that inherits from Customer class defined above

    discount_rate = 0.2                                     #static variable dicount_rate set to 20%


    def get_discount(self, cost):                           #get_discount = getter to get discount value
        super().get_discount(cost)                          #super() takes the code for get_discount() defined in parent class and adds further attributes
        self.discount = cost * RewardFlatCustomer.discount_rate
        return self.discount
    
    def display_info(self):                                 #method to display information of all attributes
        super().display_info()                              #super() copies code from above, and adding more print statements
        print('{:<15}{:>20}'.format("Discount rate :",self.discount_rate ))
            
        
    
    @staticmethod                                           #static method set_discount_rate to update value of discount_rate
    def set_discount_rate(discount_rate):
        RewardFlatCustomer.discount_rate = discount_rate

    @staticmethod                                           #staticc method get_discount_rate to get the value of discount rate
    def get_discount_rate():
        return RewardFlatCustomer.discount_rate


####################################################################################

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
        super().display_info()
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

#################################################################################
################################################################################



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


#####################################################
####################################################################################


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

    

##################################################################################
################################################################


    
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


################################################################
    ################################################################


class Records:

    customers = []
    movies = []
    ticket_types = []

    @staticmethod                 #as of now we are storing all lists as static variables
    def read_customers(file_name):
        with open(file_name+'.txt','r') as f:
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
                Records.customers.append(customer)


    @staticmethod
    def read_movies(file_name):
        with open(file_name+'.txt','r') as f1:
            for line in f1:
                row=line.strip().split(",")
                [y.strip() for y in line]
                movie_ID = row[0]
                movie_name = row[1].title()
                seats_available = row[2]

                if (row[0][0].upper() !='M'):
                    continue

                movie = Movie(movie_ID, movie_name, seats_available)

                Records.movies.append(movie)


    @staticmethod
    def read_tickets(file_name):
        with open(file_name+'.txt','r') as f2:
            for line in f2:
                row=line.strip().split(",")
                [z.strip() for z in line]
                ticket_ID = row[0]
                ticket_name = row[1].lower()
                ticket_unit_price = row[2]

                if (row[0][0].upper() !='T'):
                    continue

                ticket = Ticket(ticket_ID, ticket_name, ticket_unit_price)

                Records.tickets.append(ticket)


    @staticmethod
    def find_customer():
##      column_format = "{:<" + str(dates_width) + "} {:<" + str(names_width) + "} {:>" + str(amounts_width) + "}\n"
        user_inp = get_string("Please enter customer name__")
        i = 0
        for customer in Records.customers:
            if customer.get_name() == user_inp:
                print('{:<15}{:>15}'.format("Customer ID :",customer.get_ID()))
                print('{:<15}{:>15}'.format("Customer name :",customer.get_name()))
                i+=1
            if i == 0:
                print("Apologies, customer doesn't exist in the system.")
            else:
                pass

            
    @staticmethod
    def find_movie():
        user_inp = get_string("Please enter movie name__")
        i = 0
        for movie in Records.movies:
            if movie.get_name() == user_inp:
                print('{:<15}{:>15}'.format("Movie ID :",movie.get_ID()))
                print('{:<15}{:>15}'.format("Movie name :",movie.get_name()))
                print('{:<15}{:>15}'.format("Seats available :",movie.get_seat_available()))
                i+=1
            if i == 0:
                print("Apologies, we are unable find any movie with the given name.")
            else:
                pass
        

    @staticmethod
    def find_ticket():
        user_inp = get_string("Please enter the name of the ticket you are searching for__").lower()
        i = 0
        for ticket in Records.ticket_types:
            if ticket.get_name() == user_inp:
                print('{:<15}{:>15}'.format("Ticket ID :",ticket.get_ID()))
                print('{:<15}{:>15}'.format("Ticket name :",ticket.get_name()))
                print('{:<15}{:>15}'.format("Ticket price :",ticket.get_price()))
                i+=1
            if i == 0:
                print("Apologies, we were unable to find the required ticket type")
            else:
                pass
                
        
        





    @staticmethod
    def display_customers():
        pass

    @staticmethod
    def display_movies():
        pass

    @staticmethod
    def display_tickets():
        pass



    




                


                
            




##    def __init__(self, customers=[], movies=[], ticket_types=[]):
##        self.customers = customers
##        self.movies = movies
##        self.ticket_types = ticket_types
        
        















        


        
