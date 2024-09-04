#########################################################################################################################################################################################
#NAME         : VIVEK AGGARWAL
#STUDENT_ID   :S4015465
#ALL PARTS ATTEMPTED

## THIS PROGRAM CANNOT RECOGNIZE WORDS OR NAMES THAT HAVE 2 WORDS WRITTEN TOGETHER WITHOUT SPACES

#The following code currently does not give any errors.
#The following code will give the last movie entered as most popular movie with revenue of $0 if no mive has sold any ticket.


#Only one web source used for this program apart from canvas modules and python documentation provided to us. The citation as per IEEE format is as follows:
#“Python all(),” Programiz. [Online]. Available: https://www.programiz.com/python-programming/methods/built-in/all. [Accessed: 31-Mar-2023].

#########################################################################################################################################################################################
#########################################################################################################################################################################################
'''
I started assignment part one near the end of the 3rd week of current semester. Part one was relatively easy as it didnt require any complex conditions or logic to code.
Still, formatting the output was something that wasn not taught by then. By the next week, formatting the output by using format() was taught. Coming to part 2, I read the
remaining parts together and figured that making a function for every specific option would be the most convenient thing to do. So I made a menu function, that would display
the menu and all the options available to the user. The strip() function was the most important to learn as it is used with every input, to strip off the spaces from before
and after the input string.

The nemu function by itself was not very complex. Second part of the assignment needed us to sanitize the inputs given by the user like showing an error if input was not of
the required type. This was achieved with while loops, as this was what we were taught in class and in the pre lecture materials. The python documentation also helped in
understanding how to declare functions. Since I studied C++ in high school, I was used to declaring the main() whereever convenient, but I learnt in python we have to define
every function above before calling it. When going through the assignment, I noticed much of the queries could be solved by using lists. So I used multipple lists to store
a corresponding list for movie names, seat per movie, revenue etc. I would find the index of the movie entered by user with the index() and used that index to update the values
in seats and revenue. The part one of assignment became the entire first function for the second part. And the list method was used, since it was easiest method I was aware of.
I declared all the functions required in part 3 as well but ofcourse they were incomplete as i didnt know how to display most popular movie and how to show ticket types sold for
every movie. Luckily, I didnt have to change any variable names and just had to add while loops so that user could enter multiple promts until he entered the right one.
List comprehension was also one of the most important things as it made the code relatively smaller. I no longer had to use a for loop every time with strip().
In short, string functions(especially strip() and split()), list functions(especially append()) and list comprehension were the most important things I learnt while doing part 2.
Formatting was important as well.

For the part 3, I used dictionris. They were taught earlier this week. As soon as we were given the knowledge, in the preclass material and the practical class, I knew this
would be the way to store all the values of ticket types individually and display them. The format() function had already been taught so I used it whereever necessary in
outputs. The major challenge of this part was to store individual values of all ticekt types for all movies. At first I tried using multiple nested lists and failed.
Then we were taught about dictionaries. They were not very hard to use, and they are mutable as well, like lists. zip() function was also taught this week, that allowed us to
iterate throguh multiple lists and dictionaries simultaneuosly. I completed my program using these functions and data structures, where initially, I used a nested function
to sanitize the input for the list of ticket types and quantity of ticket type respectively. The conditions to check the ticket types was getting very messy. Then I defined
the sanitizing function outside, and the code became better. But taking the function outside the purchase ticket function gave one problem, ie scope of local variables.
Ofcourse it gave many errors in starting like I had forgotten to declare local vairbales for the function. The code was ready but it was not very readable due to the use of nested
functions. The nested function served just one purpose, ie to check if the input lists are valid or not. Then I came accross the all() function, that gives boolean output,
which is perfect for conditonal statements, and can be combined with if/else very efficiently. It's citation is mentioned above. I went through the list comprehension documentation
again and it helped me fit all the conditions into the while loop itself. The dictionaries allowed me to access and update values of keys its, that were later needed for
displaying mvie records. So I feel from part 3 helped me learn 3 more important things, ie, zip(), all() and dictionaries. These built in functions and data structures
helped conclude the code. *touchwood, the code runs successfully*

Today I finally cleaned and reformed my code, and used dictionaries to declare and store values of seats available and revenue for each movie. I did not have to change my
entire code. Just had to use movie name as a call from dictionary instead of the movie index. Also had to edit a almost all functions where the seat availability and revenue
were involded.

Today I have finally added string functions like str.title() and str.casefold() functions to allow the user to input without worrying about the capital cases in input.

'''
#########################################################################################################################################################################################
#########################################################################################################################################################################################


################## the assignment mentions that we can assume all movie types and other inputs will be valid ############################################################################ 


#########################################################################################################################################################################################
#########################################################################################################################################################################################
#importing sys and declaring all the global variables that will be used in the local functions


import sys


cust_list=['Mary','James']                                                                         #cust_list stores the customer list in the system


rc_list=['Mary']                                                                                   #rc_list stores the customer list that are a part of the rewards program


ticket_types={'adult':25.0,'child':19.5,'senior':17.0,'student':20.5,'concession':20.5}            #dictionary for ticket types and indiviual prices of tickets
         

movie_names=['Avatar','Titanic','StarWars']                                                        #movie_names stores a list of all movies in the system


total_seats={'Avatar':50,'Titanic':50,'StarWars':50}                                               #total_seats stores a dictionary of total seats available for all movies


revenue_movie={'Avatar':0,'Titanic':0,'StarWars':0}                                                #revenue_movie stores the revenue generated by all movies


type_layout={'adult':0,'child':0,'senior':0,'student':0,'concession':0}                            #this dictionary will only be used to create nested dictionaires for movies


movie_dict={'Avatar':dict(type_layout),'Titanic':dict(type_layout),'StarWars':dict(type_layout)}   #creating nested dictionary to store individual values of types of seats sold 



#########################################################################################################################################################################################
#########################################################################################################################################################################################
#a function to allow user to purchase multiple ticket types for a movie
def purchase_ticket():
    sys.stdout.write("Please enter your name_")       #customer name info
    c_name=sys.stdin.readline().strip().title()       #c_name=customer name


    if c_name not in cust_list:                       #checks whether the entered name is in the system, and adds it if it isn't
        cust_list.append(c_name)
    else:
        pass
            
    
    print(movie_names)
    while True:       #this loop takes input for movie name, until a valid movie name is entered
        m_name=input("Please enter the movie name from the above movies list_").strip().title()                       #m_name=movie name input
        if m_name not in movie_names:
            print('Invalid input, please try again')
        else:
            break
        
    
    sys.stdout.write("Avialable types of ticket are:\n"+str(ticket_types)+'\n')


    input_invalid = True

    while input_invalid:          #this loop takes input for ticket types and respective quantities, untill all inputs are valid

            sys.stdout.write("Please enter a list of ticket types you want to purchase seperated by commas_")
            type_list=sys.stdin.readline().strip()              #type_list=string of ticket types selected
            
            t_types=type_list.split(',')
            t_types=[c.strip().casefold() for c in t_types]     #t_types=final list of ticket type list entered, list comprehension for strip and casefold()
            
            print('Total tickets available for this movie are',total_seats[m_name])
            sys.stdout.write('Please enter a list of number of tickets you wish to purchase respective to the list of ticket types entered_')
            num_tickets=sys.stdin.readline().strip()            #num_tickets=string of number of tickets per type entered
            
            num_t=num_tickets.split(',')                          
            num_t=[d.strip() for d in num_t]                    #num_t=final list of number of tickets per type entered


            if len(t_types)!=len(num_t):                        #to check whether the number of inputs for both t_types and num_t are same
                print('Sorry, the length of inputs for ticket types and number of tickets did not match.\n')
                continue
            
            if not all(n.isdigit() for n in num_t):             #condition to check whether all input elements in the list are numbers
                print('Sorry, invalid input. Ticket quantity has to be a positive integer.\n')
                continue
            else:
                num_t=[int(h) for h in num_t]    #list comprehension for turning all values into int 

      
            if not all(e in ticket_types for e in t_types):     #condition to check whether all input ticket types are valid or not
                print('Sorry, input for types of tickets types entered is invalid.\n')
                continue

            if not all(f>0 for f in num_t):                     #condtion to check the entered numbers are positive integers
                print('Sorry, invalid input. Number of tickets cannot be less than 1.\n')
                continue
            
            t_num=0                                             #variable to store total number of tickets selected for the movie by user

            t_num = sum(num_t)                                  #calculating total number of tickets user wishes to buy

            if t_num>total_seats[m_name]:                       #checking if total number of seats required are available or not
                print('Sorry, this amount is greater than the number of tickets currently available.\n')
                continue

            input_invalid=False
            
    #######end of the big while loop
                

    #now calculating the money
    costing=[]                                           #list for storing all the individual costing of all ticket types entered   
    for p,q in zip(t_types,num_t):
        costing.append(ticket_types[p]*q)                #adding values in costing
        movie_dict[m_name][p]+=q                         #updating values of seats sold in movie dict
      
        
    

    total_seats[m_name]-=t_num                           #updating number of seats in the total seats dictionary


    t_cost=0                                             #t_cost=cost of all types of ticket combined
    t_cost=sum(costing)                                  #sum() to add all the individual ticekt costs

        
        
    #asking the user whether he/she wants to be a part of the rewards program, and applying corresponding discount     
    discount=0
    if c_name in rc_list:        
        sys.stdout.write("You are a member of our rewards program. 20% discount will apply \n")
        discount=(0.2)*t_cost                            #discount is the money off
    else:
        sys.stdout.write("You are not currently in the rewards program. Do you wish to join? Enter 'y' for yes, 'n' for no_")
        
        rewards_input=False
        
        while rewards_input==False:                      #while loop to ensure user inputs a valid input to the given question
            r_mem=sys.stdin.readline().strip()
            match r_mem:
                case 'y' | 'Y':
                    rc_list.append(c_name)
                    print('You are now a member of the rewards program,20% discount will apply \n')
                    discount=(0.2)*t_cost                #discount is the money off
                    rewards_input=True
                case 'n' |'N':
                    print('You chose not to become a member of the rewards program. Sorry, no discount')
                    rewards_input=True
                case _:
                    print('Invalid input, please try again')


    
                            
    b_cost=2*t_num                              #b_cost=booking cost

    
    total_cost=t_cost-discount+b_cost           #total_cost= total cost for the customer

    
    revenue_movie[m_name]+=total_cost           #adding the money to the corresponding total movie revenue list item

    

    print('-'*75)
    print('Receipt of ',c_name)
    print('-'*75)
    print('{:<15}{:>40}'.format('Movie',m_name))
    print('-'*75)

    for v,w in zip(t_types,num_t):        
        print('{:<15}{:>40}'.format('Ticket type',v))
        print('{:<15}{:>40}'.format('Ticket unit price',ticket_types[v]))
        print('{:<15}{:>39}'.format('Ticket quantitiy',w))

    
    print('-'*75)
    print('{:<15}{:>40.2f}'.format('Discount',discount))
    print('{:<15}{:>40}'.format('Booking cost',b_cost))
    print('{:<15}{:>40}'.format('Total cost:',total_cost))
    
    
#end of purchase_ticket()
#########################################################################################################################################################################################
#########################################################################################################################################################################################



#########################################################################################################################################################################################
#########################################################################################################################################################################################
#a function to let user add more movies to the system
def add_new():
    
    print('Please enter a list of movie names you wish to add, seperated by commas.\n50 seats will be added for each new movie entered:')
    
    new_movies=input()                                                  #new_movies=inputs new movies as a string
    newmovie_list=new_movies.split(',')                                 #newmovie_list=splits the string seperated by commas in to a list
    newmovie_list=[str1.strip().title() for str1 in newmovie_list]      #list comprehension that strips all the spaces from the input movies
                                                                        #this also capitalizes the first letter in every movie name
    
    
    
    for i in range(0,len(newmovie_list)):                           #runs a loop to check if movie exists or not and add them if not existing
        if newmovie_list[i] in movie_names:
            print(newmovie_list[i]," already exists in the system\n")
        else:
            movie_names.append(newmovie_list[i])              #adding movie name to the movie anmes list
            total_seats[newmovie_list[i]]=50                  #adding 50 seats for the respective movie
            revenue_movie[newmovie_list[i]]=0                 #adding the revenue into the revenue dictionary for the respective movie
            movie_dict[newmovie_list[i]]=dict(type_layout)    #adding the seat type selection dictionary for the new movie
        
            print(newmovie_list[i]," has been added to the system with 50 available seats \n")
            
#end of add_new()
#########################################################################################################################################################################################
#########################################################################################################################################################################################



#########################################################################################################################################################################################
#########################################################################################################################################################################################
#a function to display the customer information
def display_customers():
    print("Existing customer list is as follows")             #prints all the customers and a seperate list of customers that exist in the rewards program
    print(cust_list)
    print('List of customers that are a part of the rewards program is given below')
    print(rc_list)

#end of display_customers()
#########################################################################################################################################################################################
#########################################################################################################################################################################################



#########################################################################################################################################################################################    
#########################################################################################################################################################################################
#a function to display the movies and respective seats available
def display_movies():
    print('S.No.','Movies'.center(40),'Available Seats'.center(35),'\n')                    #prints a table with the movies and seats info
    s_no=1
    for x in movie_names:
        print(s_no,x.center(48),str(total_seats[x]).center(30),'\n')                        #str.center() is used on int by printing the string value of the number
        s_no+=1

    

#end of display_movies()
#########################################################################################################################################################################################
#########################################################################################################################################################################################



#########################################################################################################################################################################################
#########################################################################################################################################################################################
#a function to display the movie with most earnings 
def most_popular():                                                                             

    money=0                                  #money is a variable to store the highest revenue in money
    for y in revenue_movie:                  #for loop to match value of money to the highest amount in revenue_movie list
        if revenue_movie[y]>=money:
            money=revenue_movie[y]           #storing highest amount of money in money
            most_pop=y                       #storing name of highest selling movie
        else:
            continue
    
    print("The most popular movie is",most_pop,"with an astonishing revenue of $",revenue_movie[most_pop])
        

#end of most_popular()
#########################################################################################################################################################################################
#########################################################################################################################################################################################
    


#########################################################################################################################################################################################
#########################################################################################################################################################################################
#a function to display all the movie records
def movie_records():    

    print('{0:>30}{1:>15}{2:>15}{3:>15}{4:>15}{5:>15}'.format('Adult','Child','Senior','Student','Concession','Revenue'))                 
    for z,k in zip(movie_dict,revenue_movie):    #zip() used as number of movies list and revenue dictionary for movies will always have same number of elements
                                                 #zip() is used to iterate through multiple lists or dictionaries simultaneously
        print('{0:<15}{1:>15}{2:>15}{3:>15}{4:>15}{5:>15}{6:>15}'.format(z,movie_dict[z]['adult'],movie_dict[z]['child'],movie_dict[z]['senior'],movie_dict[z]['student'],movie_dict[z]['concession'],revenue_movie[k]))
        

#end of movie_records()
#########################################################################################################################################################################################
#########################################################################################################################################################################################



#########################################################################################################################################################################################
#########################################################################################################################################################################################
#a function to display the menu and letting the user select the desired option, and to call the corresponding functions defined above
def menu():                                        
    print("Welcome to RMIT movie ticketing system.")
    print("Please note that all the inputs are case-sensitive. Kindly give inputs accordingly. Thank you <3")
    print('#'*80)
    print('''You can choose from the following options:
1. Purchase tickets
2. Add new movies
3. Display existing customers information
4. Display existing movies information
5. Display the most popular movie
6. Display all movie records
0. Exit the program''')
    print('#'*80)                                                    #given user all information regarding choosing an option


    user_input=input("Choose any one option_").strip()               #gives user info to choose a option,user_input= input given by the user, as per the option he/she chooses
                                                                     #str.strip() to igrnoe the spaces

    match user_input:                                                #matches and calls the function corresponding to the user input
        case '1':
            purchase_ticket()
        case '2':
            add_new()
        case '3':
            display_customers()
        case '4':
            display_movies()
        case '5':
            most_popular()
        case '6':
            movie_records()
        case '0':
            print('Thank you for using RMIT ticketing system, have a good day. Bubye')
            return            #exits the program function gracefully
                              #exit() or can use quit(), to exit the program
        case _:               #for any other invalid input
            print('Invalid input, please select one of the given options')
            
            


    print('The menu will be printed again below.\n\n')
    menu()                    #calls and displays the menu() again for choosing another option is the user wishes

#end of menu()
#########################################################################################################################################################################################
#########################################################################################################################################################################################
    



menu()                        #starts with the first menu
            
            
        
    

    



