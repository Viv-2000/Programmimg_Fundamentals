#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Name : Vivek Aggarwal
#student ID: S4015465
#
#highest part attempted : hd
#errors or missing things: this code does not calculate the weighted grade point avergae(WGPA) in the students table
#                          this code does not print the students table in a sorted way
#                          this code does not print the courses table in a sorted way
#
#
##Most of the code is very well self explanatory, all the function and variable names are stored with names representing the exact meaning for which they are used for.
##I started by making basic 3 classes, that were students, courses and results. After doing the assignment 1 and 2, and reading the finance manager code, I had a small idea about
## what we were supposed to do in this assignment and how. The assignment, the pass level was achieved relatively easily with the read courses and display etc function. The first
##barrier was finding out how to store the results data, because there were 3 conditions, one where the score was blank, one where it is given, and one where student might not have 
## enrolledin all the courses. After solving this by using results dictionary, finding a way to find the average pass rate. I had to make another static variable in Results class for this.
##I stored the all the scores as a list for this level and calculated the pass rate with if conditon by comapring whether the score was above 49.5 or not.
##
##Coming to the credit level, I had to change the data type to store the score into a course-score dictionary rather than a list. now every course had a list that would store the
##scores of allstudents that have enrolled in the respective course. I defined the respective functions for courses and students to calculate the course stats and student stats.
##These functions return a tuple of all values that are needed to be printed in the display functions. We do not need to use any other library apart from sys, os and datetime,
##sys is mostly used for writing data, datetime is used for finding the current date and time everytime needed, and os is used to check whether the input file is present in the
##current working directory or not.
##
##All the display functions work and they print on screen and append the tables into the reports file as per the assignment specifications. I used the f.seek() to point the
##pointer to the beginning of the file everytime a display function is called and the timestamp is also printed in the reports everytime it is opened. Most of the function names
##used are used for them to be as self explanatory as possible. Also, there are no external references used in the program. All of the data used is from the modules provided by
##RMIT canvas.
##
##The rest explanantions are given in the comments with each line.
## the comments that need to be repeated or are redundant like in multilple display functions, are not there. The displaying students was also very challenging as i had to figure out
##that how to return all 4 values with the help of a single function. The majority of functions are present in the result class.
## Once the files are fed in the system throught the command lines, the data is automatically loaded if all the conditions are satisfied and data is in correct format.
## THen the user is given a menu to choose options from and the corresponding function is called (this idea from the orevious assignment). The code is tidy and easy to understand.
## The code is strictly object oriented apart from 2 lines that start the execution of the code.
##

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Importing all necessary libraries
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import sys
import os
from datetime import datetime

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#defining the custom exceptions that will be raised later in the code
class InvalidArgumentsError(Exception):
    pass

class InvalidChoiceError(Exception):
    pass

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Creating class student, all students will be passed through this class and an object will represent each student
class Student:  
    def __init__(self, student_ID, student_name, student_type, student_mode):    #constructor takes 4 parameters
        self.student_ID = student_ID                                             #this is student id
        self.student_name = student_name                                         #this is student name
        self.student_type = student_type                                         #this is student type, PG or UG
        self.student_mode = student_mode                                         #student mode is pt or ft


    #following are all the getters defined for the class student that will be used later, we did not need the setters.
    def get_student_ID(self):       
        return self.student_ID

    def get_student_name(self):
        return self.student_name

    def get_student_type(self):
        return self.student_type

    def get_student_mode(self):
        return self.student_mode

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# creating class course, all the courses found will go through here for formation of a course object for each course
class Course:
    def __init__(self, course_ID, course_type, course_name, credit_points, offered_semesters = 'All'):    #constructor takes 5 parameters
        self.course_ID = course_ID                      #stores course ID
        self.course_type = course_type                  #stores course type
        self.course_name = course_name                  #stores course name
        self.credit_points = int(credit_points)         #stores credit points for the respective course
        self.offered_semesters = offered_semesters      #stores the semesters in which the corresponding course is offered

    #following are all the getters defined for the class course that will be required in the code later
    def get_course_ID(self):
        return self.course_ID

    def get_course_type(self):
        return self.course_type

    def get_course_name(self):
        return self.course_name

    def get_credit_points(self):
        return self.credit_points

    def get_offered_semesters(self):
        return self.offered_semesters

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#class result, this class will store most of the functions and lists to store data and perform calculations
class Result:
    students = list()       #stores list off student objects
    courses = list()        #stores list of course objects
    results = dict()        #stores a nested dictionary for student, that stores a subjectionary for courses, and the respective score of the student for the respective course

    score_dict = dict()     #this dictionary stores lists as values and courses as its keys, used to compute course data and averages


#.........................................................................

#read data functions
    def read_students(self, file_name):                     #this function reads the student data, makes an object, appends it to the student list
        try:            
            with open(file_name,'r') as student_file:       #opens student file as student_file
                for line in student_file:                   #going through each line
                    row = [x.strip().upper() for x in line.strip().split(',')]      #list comprehension, the first splits strips spaces off of indiviual attributes, second for whole line 
                    student_ID = row[0]                     #assigning student id its value from row
                    if not student_ID.startswith('S'):      #checking whether the student id starts with s otherwise return false and exit the program
                        return False
                    student_name = row[1].title()           #assigning student name
                    student_type = row[2]                   #student type-UG or PG
                    if len(row) == 4:                       #if condition checks if another attribute is there, it must be for PT students.
                        student_mode = row[3]       
                    else:
                        student_mode = 'FT'
                    student = Student(student_ID, student_name, student_type, student_mode)     #making object of student
                    self.students.append(student)                                               #appending the student to the list
            return True
        except:
            return False


    def read_courses(self, file_name):                                          #read courses to read the course data, make objects and append it
        try:            
            with open(file_name,'r') as course_file:                            #open() to open course file as course_file
                for line in course_file:
                    row = [y.strip().title() for y in line.strip().split(',')]  #list comprehension, strips and splits all elements simultaneously in every line
                    course_ID = row[0].upper()
                    if course_ID[:4] not in ['COSC', 'ISYS', 'MATH']:           #checking if all subjects start wiht given conditions otherwise exit program
                        return False
                    course_type = row[1]                                        #assigning course type
                    course_name = row[2]                                        #assigning course name
                    credit_points = int(row[3])
                    if len(row) == 5:                                           #if condition to check if offered semesters is provided or not
                        offered_semesters = row[4]
                    elif len(row) == 4:                                         #default value of offered semesters is all
                        offered_semesters = 'All'
                        
                    course = Course(course_ID, course_type, course_name, credit_points, offered_semesters)      #creating object for every course
                    self.courses.append(course)                                                                 #appending course into course list
                    self.score_dict[course] = list()                                                            #appending course into score_dict, that will be used for calculations
            return True
        except:
            return False

    
    def read_results(self, file_name):                                          #read results will read the result file and append all info into score dict as well as results dictionary
        try:            
            with open(file_name, 'r') as result_file:                           #opening results file as result_file
                for line in result_file:    
                    row = [z.strip().upper() for z in line.strip().split(',')]  #list comprehension, splitting aqdn stripping data simultaneously 
                    student_ID, course_ID, score = row                          # assinging student id, courseid and score to variables
                    student = self.find_student(student_ID)                     #finding the student 
                    course = self.find_course(course_ID)                        #finding the course
                    if score:                                                   #if score is given, vale converted to float, if wrong datatype, the program will exit
                        score = float(score)
                    else:                                                       #blank value means result awaited, so score replaced with hyphens
                        score = '--'
                    self.score_dict[course].append(score)                       #appending the score to every corresponding course in the score dict
                    if student not in self.results:                             #if student doesnt exist in the result dict yet, then insert
                        self.results[student] = dict()  
                    self.results[student][course] = score                       #adding the score of respective course for respective student in the result dictionary
            if not self.results:                                                # if result file is empty, return false
                return False
            return True
        except:
            return False        

            
#.........................................................................

    #find data functions , these functions are referenced from the assignment 2, made easier to find data       
    def find_student(self, student_info):
        try:
            for student in self.students:
                if student.get_student_ID() == student_info:
                    return student
        except:
            return None
            
    def find_course(self, course_info):
        try:
            for course in self.courses:
                if course.get_course_ID() == course_info:
                    return course
        except:
            return None
 
#.........................................................................

    #update reports file to save timestamp 
    def get_timestamp(self):                            #function to get date and time for report file
        now = datetime.now()                            #now stores current data and time
        timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
        report = f"Report generated at {timestamp}"
        return report                                   #returning the timestamp



#.........................................................................

    def calculate_pass_rate(self, score_dict):          #this function calculates pass rate in the score dict
        i = 0
        j = 0
        for course in score_dict:                       #nested for loops to check all the scores for all subjects
            for score in score_dict[course]:
                if type(score) == float and score > 49.5:
                    i += 1
                j += 1
        pass_rate = (i / j) * 100
        return pass_rate


#.........................................................................

    def calculate_course_stats(self, course):           #a function to calculate all stats for a course
        total_score = 0
        n_finish = 0
        non_going = 0
        if course in self.score_dict:                   #if the course is in the score dict
            for score in self.score_dict[course]:       
                if type(score) is float:                    
                    total_score += score
                    n_finish += 1
                elif type(score) is str:
                    non_going += 1                    
        course_average = (total_score / n_finish)       #calculating the course average
        return course_average, n_finish, non_going      #returning the average, the nfinsh and nongoing

#.........................................................................

    def find_difficult_course(self, course_type):       #this function is to find the most difficult course,
        lowest_average = 1000000
        course_list = list()
        for course in self.courses:                     #checks all the courses, and uses calculate average function
            if course.get_course_type() == course_type: #if the course average is lower than previous course, appends it to course list
                course_average = self.calculate_course_stats(course)[0]
                if lowest_average > course_average:
                        lowest_average = course_average
                        course_list.append(course)

        return course_list[len(course_list)-1]          #returning the last element of the list as it will have the loweest average

#.........................................................................

    def calculate_student_average(self, student):       #calculating the stats for students
        total_score = 0
        mini_score = 0
        n_finish = 0
        non_going = 0
        for course in self.results[student]:            #iterating through all the courses for a student in the results dictionary
            if type(self.results[student][course]) == float:        
                score = self.results[student][course]
                total_score += score
                n_finish += 1
                if score >= 79.5:                               #assigning the grade points as given in the assignment
                    mini_score += 4
                elif score >= 69.5 and score < 79.5:
                    mini_score += 3
                elif score >= 59.5 and score < 69.5:
                    mini_score += 2
                elif score >= 49.5 and score < 59.5:
                    mini_score += 1    
            else:
                non_going += 1
                 
        GPA100 = total_score / n_finish                 #calculating the gpa out of 100
        GPA4 = mini_score / n_finish                    #calculating gpa out of 4
        return GPA100, GPA4, n_finish, non_going        #returning a tuple, having both gpas and nfinish and non going

#.........................................................................

    def find_best_student(self, student_type):          #finding the best student
        best_gpa = 0
        student_list = list()
        for student in self.students:                   #checking through all the students
            if student.get_student_type() == student_type:
                new_gpa = self.calculate_student_average(student)[1]  
                if new_gpa > best_gpa:      
                    best_gpa = new_gpa                  #assigning new gpa if the new one is higher than the last one, and using the calcualte student stat function
                    student_list.append(student)        #appending the new student if the condition satisfies

        return student_list[len(student_list)-1]        #returning the last object in the list

#.......................................................................................................................................................................

    
    #this function displays the required result and writes all the ouptut into the reports file as well
    #after every print function for output, there is a corresponding file.write function to update report file
    def display_results(self, reports_file_name):        
        report_file = open(reports_file_name, 'a')      #opening the reports file, in append mode
        report_file.seek(0, 0)                          #shifting the pointer to the begininng of the file
        
        print('\n\n')
        report_file.write('\n \n')              

        report_file.write(str(self.get_timestamp()) + '\n') #to put the timestamp in the report

        print('-' * 90)
        report_file.write('-' * 90 + '\n')
        
        sys.stdout.write('{:<15}'.format('Student IDs'))
        report_file.write('{:<15}'.format('Student IDs'))

        for course in self.courses:
            sys.stdout.write('{:>15}'.format(course.get_course_ID()))
            report_file.write('{:>15}'.format(course.get_course_ID()))
        print()
        report_file.write('\n')

        print('-' * 90)
        report_file.write('-' * 90 + '\n')
        
        # Print the table rows
        for student in self.students:
            student_ID = student.get_student_ID()
            sys.stdout.write('{:<15}'.format(student_ID))
            report_file.write('{:<15}'.format(student_ID))

            for course in self.courses:
                course_ID = course.get_course_ID()
                if (student in self.results) and (course in self.results[student]):
                    sys.stdout.write('{:>15}'.format(self.results[student][course]))
                    report_file.write('{:>15}'.format(self.results[student][course]))
                else:
                    sys.stdout.write('{:>15}'.format(''))
                    report_file.write('{:>15}'.format(''))
            print()
            report_file.write('\n')
        
        #Results summary
        no_of_students = len(self.students)
        no_of_courses = len(self.courses)
        pass_rate = self.calculate_pass_rate(self.score_dict)
        print('\n RESULTS SUMMARY')
        print(f"There are {no_of_students} students and {no_of_courses} courses.")                
        print(f"The average pass rate is {pass_rate:.2f}%.")

        report_file.write('\n RESULTS SUMMARY \n')
        report_file.write(f"There are {no_of_students} students and {no_of_courses} courses. \n")                
        report_file.write(f"The average pass rate is {pass_rate:.2f}%. \n")
        report_file.close()     #closing the file

#.......................................................................................................................................................................
    #this function displays the courses and writes all the ouptut into the reports file as well
    #after every print function for output, there is a corresponding file.write function to update report file

    def display_courses(self, reports_file_name):
        report_file = open(reports_file_name, 'a')    #opening report file in append mode
        report_file.seek(0, 0)                          #shifting pointer to starting of file
        
        print('\n\n')
        report_file.write('\n \n')

        report_file.write(str(self.get_timestamp()) + '\n')
        
        print('COURSE INFORMATION')
        report_file.write('COURSE INFORMATION \n')
        
        print('-' * 111)
        report_file.write('-' * 111 + '\n')
        sys.stdout.write('{:<15}{:<15}{:>6}{:>15}{:>15}{:>15}{:>15}{:>15}'.format('CourseID', 'Name', 'Type', 'Credit', 'Semester', 'Average', 'Nfinish', 'Nongoing'))
        report_file.write('{:<15}{:<15}{:>6}{:>15}{:>15}{:>15}{:>15}{:>15}'.format('CourseID', 'Name', 'Type', 'Credit', 'Semester', 'Average', 'Nfinish', 'Nongoing'))
        print()
        report_file.write('\n')
        print('-' * 111)
        report_file.write('-' * 111 + '\n')
        
        for course in self.courses:
            if course.get_course_type() == 'C':
                course_stats = self.calculate_course_stats(course)
                course_average = course_stats[0]
                n_finish = course_stats[1]
                non_going = course_stats[2]           
                sys.stdout.write('{:<15}{:<15}{:>6}{:>15}{:>15}{:>15.2f}{:>15}{:>15}'.format(course.get_course_ID(), course.get_course_name(), course.get_course_type(), course.get_credit_points(), course.get_offered_semesters(), course_average, n_finish, non_going))
                report_file.write('{:<15}{:<15}{:>6}{:>15}{:>15}{:>15.2f}{:>15}{:>15}'.format(course.get_course_ID(), course.get_course_name(), course.get_course_type(), course.get_credit_points(), course.get_offered_semesters(), course_average, n_finish, non_going))
                print()
                report_file.write('\n')
        print('-' * 111)
        report_file.write('-' * 111 + '\n')
        
        sys.stdout.write('{:<15}{:<15}{:>6}{:>15}{:>15}{:>15}{:>15}{:>15}'.format('CourseID', 'Name', 'Type', 'Credit', 'Semester', 'Average', 'Nfinish', 'Nongoing'))
        report_file.write('{:<15}{:<15}{:>6}{:>15}{:>15}{:>15}{:>15}{:>15}'.format('CourseID', 'Name', 'Type', 'Credit', 'Semester', 'Average', 'Nfinish', 'Nongoing'))
    
        print()
        report_file.write('\n')
        
        print('-' * 111)
        report_file.write('-' * 111 + '\n')
        for course in self.courses:
            if course.get_course_type() == 'E':
                course_stats = self.calculate_course_stats(course)
                course_average = course_stats[0]
                n_finish = course_stats[1]
                non_going = course_stats[2]
                sys.stdout.write('{:<15}{:<15}{:>6}{:>15}{:>15}{:>15.2f}{:>15}{:>15}'.format(course.get_course_ID(), course.get_course_name(), course.get_course_type(), course.get_credit_points(), course.get_offered_semesters(), course_average, n_finish, non_going))
                report_file.write('{:<15}{:<15}{:>6}{:>15}{:>15}{:>15.2f}{:>15}{:>15}'.format(course.get_course_ID(), course.get_course_name(), course.get_course_type(), course.get_credit_points(), course.get_offered_semesters(), course_average, n_finish, non_going))
                print()
                report_file.write('\n')

        print('\n COURSE SUMMARY')
        report_file.write('\n COURSE SUMMARY \n')
    
        course = self.find_difficult_course('C')        
        print(f"The most difficult core course is {course.get_course_ID()} with an average score of {self.calculate_course_stats(course)[0]:.2f}.")
        report_file.write(f"The most difficult core course is {course.get_course_ID()} with an average score of {self.calculate_course_stats(course)[0]:.2f}. \n")
        course = self.find_difficult_course('E')
        print(f"The most difficult elective course is {course.get_course_ID()} with an average score of {self.calculate_course_stats(course)[0]:.2f}.")
        report_file.write(f"The most difficult core course is {course.get_course_ID()} with an average score of {self.calculate_course_stats(course)[0]:.2f}. \n")

        report_file.close()
        
#.......................................................................................................................................................................

#this function displays the students and writes all the ouptut into the reports file as well
    #after every print function for output, there is a corresponding file.write function to update report file


    def display_students(self, reports_file_name):

        report_file = open(reports_file_name, 'a')
        report_file.seek(0, 0)
        
        print('\n\n')
        report_file.write('\n \n')

        report_file.write(str(self.get_timestamp()) + '\n')
        
        print('STUDENT INFORMATION')
        report_file.write('STUDENT INFORMATION \n')
        
        print('-' * 94)
        report_file.write('-' * 94 + '\n')
        
        sys.stdout.write('{:<15}{:<10}{:>10}{:>10}{:>15}{:>10}{:>12}{:>12}'.format('StudentID', 'Name', 'Type', 'Mode', 'GPA(100)', 'GPA(4)', 'Nfinish', 'Nongoing'))
        report_file.write('{:<15}{:<10}{:>10}{:>10}{:>15}{:>10}{:>12}{:>12}'.format('StudentID', 'Name', 'Type', 'Mode', 'GPA(100)', 'GPA(4)', 'Nfinish', 'Nongoing'))
        
        print()
        report_file.write('\n')
        print('-' * 94)
        report_file.write('-' * 94 + '\n')
        
        for student in self.students:
            if student.get_student_type() == 'PG':
                student_stats = self.calculate_student_average(student)
                GPA100 = student_stats[0]
                GPA4 = student_stats[1]
                n_finish = student_stats[2]
                non_going = student_stats[3]
                if (student.get_student_mode() == 'FT') and (n_finish + non_going < 4):
                    s_name = str(student.get_student_name()) + '(!)'
                elif (student.get_student_mode() == 'PT') and (n_finish + non_going < 2):
                    s_name = str(student.get_student_name()) + '(!)'
                else:
                    s_name = student.get_student_name()
                                            
                sys.stdout.write('{:<15}{:<10}{:>10}{:>10}{:>15.2f}{:>10.2f}{:>12}{:>12}'.format(student.get_student_ID(), s_name, student.get_student_type(), student.get_student_mode(), GPA100, GPA4, n_finish, non_going))
                report_file.write('{:<15}{:<10}{:>10}{:>10}{:>15.2f}{:>10.2f}{:>12}{:>12}'.format(student.get_student_ID(), s_name, student.get_student_type(), student.get_student_mode(), GPA100, GPA4, n_finish, non_going))
                print()
                report_file.write('\n')            
                
        print('-' * 94)
        report_file.write('-' * 94 + '\n')
        
        sys.stdout.write('{:<15}{:<10}{:>10}{:>10}{:>15}{:>10}{:>12}{:>12}'.format('StudentID', 'Name', 'Type', 'Mode', 'GPA(100)', 'GPA(4)', 'Nfinish', 'Nongoing'))
        report_file.write('{:<15}{:<10}{:>10}{:>10}{:>15}{:>10}{:>12}{:>12}'.format('StudentID', 'Name', 'Type', 'Mode', 'GPA(100)', 'GPA(4)', 'Nfinish', 'Nongoing'))
        
        print()
        report_file.write('\n')
        print('-' * 94)
        report_file.write('-' * 94 + '\n')
        
        for student in self.students:
            if student.get_student_type() == 'UG':
                student_stats = self.calculate_student_average(student)
                GPA100 = student_stats[0]
                GPA4 = student_stats[1]
                n_finish = student_stats[2]
                non_going = student_stats[3]
                if (n_finish + non_going < 4):
                    s_name = student.get_student_name() + '(!)'
                else:
                    s_name = student.get_student_name()
                    
                sys.stdout.write('{:<15}{:<10}{:>10}{:>10}{:>15.2f}{:>10.2f}{:>12}{:>12}'.format(student.get_student_ID(), s_name, student.get_student_type(), student.get_student_mode(), GPA100, GPA4, n_finish, non_going))            
                report_file.write('{:<15}{:<10}{:>10}{:>10}{:>15.2f}{:>10.2f}{:>12}{:>12}'.format(student.get_student_ID(), s_name, student.get_student_type(), student.get_student_mode(), GPA100, GPA4, n_finish, non_going))
                print()
                report_file.write('\n')

        print('\n STUDENT SUMMARY')
        report_file.write('\n STUDENT SUMMARY \n')
        
        student = self.find_best_student('PG')
        print(f"The best PG student is {student.get_student_ID()} with a GPA score of {self.calculate_student_average(student)[1]:.2f}.")
        report_file.write(f"The best PG student is {student.get_student_ID()} with a GPA score of {self.calculate_student_average(student)[1]:.2f}. \n")
        
        student = self.find_best_student('UG')        
        print(f"The best UG student is {student.get_student_ID()} with a GPA score of {self.calculate_student_average(student)[1]:.2f}.")
        report_file.write(f"The best UG student is {student.get_student_ID()} with a GPA score of {self.calculate_student_average(student)[1]:.2f}. \n")
        
        report_file.close()


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class Operations:

    result = Result()

#.........................................................................
    def load_data(self, s_file, c_file, r_file):   #this function checks whether all the files are correctly loaded or not

        if not self.result.read_students(s_file):
            print('There was some error loading the student data.')
            return False
        
        if not self.result.read_courses(c_file):
            print('There was some error loading the course data.')
            return False
                    
        if not self.result.read_results(r_file):
            print('There was some error loading the result data.')
            return False

        return True
#.........................................................................
            
    def menu(self):                                             #This function is to give the user all the options to choose from 
        print('\n\n')
        print("Welcome to RMIT academics database") 
        print('*'*60)
        print('''You can choose from the following options:
1. Display the results 
2. Display the course info
3. Display the student info
0. Exit the program''')
        print('*'*60)                                    


        user_choice = input("Please choose any one of the options given above__").strip()

        return user_choice                                      #returns the choice user makes


#.........................................................................

    def run_operations(self, s_file, c_file, r_file):           #runs the respctive operation, or function according to user choice
        if not self.load_data(s_file, c_file, r_file):
            return
        else:
            reports_file_name = 'reports.txt'

        user_choice = self.menu()
        while True:
            match user_choice:
                case '1':
                    self.result.display_results(reports_file_name)
                case '2':
                    self.result.display_courses(reports_file_name)
                case '3':
                    self.result.display_students(reports_file_name)
                case '0':
                    print('Thank you for using RMIT academics results system. Have a good day.')
                    return
                case _:
                    print('Invalid input. Please select one of the given options.')
            user_choice = self.menu()    

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Main:
    def check_files_exist(self, files):
        missing_files = []
        for file in files:
            if not os.path.isfile(file):
                missing_files.append(file)
        return missing_files

    def run(self):
        sys_arguments = sys.argv

        if len(sys_arguments) == 4:  # Check for 4 arguments (including script name)
            r_file = sys_arguments[1]
            c_file = sys_arguments[2]
            s_file = sys_arguments[3]

            missing_files = self.check_files_exist([r_file, c_file, s_file])

            # Print error message and exit if any files are missing
            if missing_files:
                print("The following files could not be found:")
                for file in missing_files:
                    print(file)
                sys.exit(1)
        else:
            print('[Usage:] python my_school.py <result_file> <course_file> <student_file>')
            sys.exit(0)

        operation1 = Operations()
        operation1.run_operations(s_file, c_file, r_file)

if __name__ == "__main__":
    main_obj = Main()
    main_obj.run()






#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


