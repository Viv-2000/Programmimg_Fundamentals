import sys
import os

#sys_arguments = sys.argv

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------


class Student:
    def __init__(self, student_ID):
        self.student_ID = student_ID

    def get_student_ID(self):
        return self.student_ID

    def display_info(self):
        print(f"Student ID : {self.student_ID}")

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------


class Course:
    def __init__(self, course_ID, course_type, course_name, credit_points, offered_semesters = 'All'):
        self.course_ID = course_ID
        self.course_type = course_type
        self.course_name = course_name
        self.credit_points = int(credit_points)
        self.offered_semesters = offered_semesters

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

    def display_info(self):
        print(f"Course ID : {self.course_ID}")

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------


class Result:
    students = list()
    courses = list()
    results = dict()

    score_dict = dict()


#.........................................................................

#read data functions
    def read_students(self, file_name):
        try:            
            with open(file_name,'r') as student_file:
                for line in student_file:
                    row = [x.strip().title() for x in line.strip().split(',')]      #list comprehension, the first splits strips spaces off of indiviual attributes, second for whole line 
                    student_ID = row[0].upper()
                    student = Student(student_ID)
                    self.students.append(student)
            return True
        except:
            return False


    def read_courses(self, file_name):
        try:            
            with open(file_name,'r') as course_file:
                for line in course_file:
                    row = [y.strip().title() for y in line.strip().split(',')]
                    course_ID = row[0].upper()
                    course_type = row[1]
                    course_name = row[2]
                    credit_points = int(row[3])
                    if len(row) == 5:
                        offered_semesters = row[4]
                    elif len(row) == 4:
                        offered_semesters = 'All'
                        
                    course = Course(course_ID, course_type, course_name, credit_points, offered_semesters)
                    self.courses.append(course)
                    self.score_dict[course] = list()
            return True
        except:
            return False

    
    def read_results(self, file_name):
        try:            
            with open(file_name, 'r') as result_file:
                for line in result_file:
                    row = [z.strip().upper() for z in line.strip().split(',')]
                    student_ID, course_ID, score = row
                    student = self.find_student(student_ID)
                    course = self.find_course(course_ID)
                    if score:
                        score = float(score)
                    else:
                        score = '--'
                    self.score_dict[course].append(score)
                    if student not in self.results:
                        self.results[student] = dict()
                    self.results[student][course] = score
            return True
        except:
            return False        

            
#.........................................................................

    #find data functions        
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

    #update reports file to save data function
    def update_report(self):
        pass



#.........................................................................

    def calculate_pass_rate(self, score_dict):
        i = 0
        j = 0
        for course in score_dict:
            for score in score_dict[course]:
                if type(score) == float and score > 49.5:
                    i += 1
                j += 1
        pass_rate = (i / j) * 100
        return pass_rate


#.........................................................................

    def calculate_course_stats(self, course):
        total_score = 0
        n_finish = 0
        non_going = 0
        if course in self.score_dict:
            for score in self.score_dict[course]:
                if type(score) is float:                    
                    total_score += score
                    n_finish += 1
                elif type(score) is str:
                    non_going += 1                    
        course_average = (total_score / n_finish) 
        return course_average, n_finish, non_going

#.........................................................................

    def calculate_difficult_course(self, course_type):
        lowest_average = 1000000
        course_list = list()
        for course in self.courses:
            if course.get_course_type() == course_type:
                course_average = self.calculate_course_stats(course)[0]
                if lowest_average > course_average:
                        lowest_average = course_average
                        course_list.append(course)

        return course_list[len(course_list)-1]
                




#.........................................................................
    
    #this function displays the required result and writes all the ouptut into the reports file as well
    def display_results(self, reports_file_name):        
        report_file = open(reports_file_name, 'w')

        print('\n\n')
        report_file.write('\n \n')
        
        sys.stdout.write('{:<15}'.format('Student IDs'))
        report_file.write('{:<15}'.format('Student IDs'))

        for course in self.courses:
            sys.stdout.write('{:>15}'.format(course.get_course_ID()))
            report_file.write('{:>15}'.format(course.get_course_ID()))
        print()
        report_file.write('\n')
        
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
        print('RESULTS SUMMARY')
        print(f"There are {no_of_students} students and {no_of_courses} courses.")                
        print(f"The average pass rate is {pass_rate:.2f}%.")

        report_file.write('RESULTS SUMMARY \n')
        report_file.write(f"There are {no_of_students} students and {no_of_courses} courses. \n")                
        report_file.write(f"The average pass rate is {pass_rate:.2f}%. \n")
        report_file.close()
#.........................................................................


    def display_courses(self, reports_file_name):
        report_file = open(reports_file_name, 'w')

        print('\n\n')
        report_file.write('\n \n')
        
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

        course = self.calculate_difficult_course('C')        
        print(f"The most difficult core course is {course.get_course_ID()} with an average score of {self.calculate_course_stats(course)[0]:.2f}.")
        report_file.write(f"The most difficult core course is {course.get_course_ID()} with an average score of {self.calculate_course_stats(course)[0]:.2f}. \n")
        course = self.calculate_difficult_course('E')
        print(f"The most difficult elective course is {course.get_course_ID()} with an average score of {self.calculate_course_stats(course)[0]:.2f}.")
        report_file.write(f"The most difficult core course is {course.get_course_ID()} with an average score of {self.calculate_course_stats(course)[0]:.2f}. \n")

        report_file.close()
        



#.........................................................................

            
            




#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------


class Operations:

    result = Result()

#.........................................................................
    def load_data(self, s_file, c_file, r_file):

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
0. Exit the program''')
        print('*'*60)                                    


        user_choice = input("Please choose any one of the options given above__").strip()

        return user_choice                                      #returns the choice user makes


#.........................................................................

    def run_operations(self, s_file, c_file, r_file):
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
                case '0':
                    self.save_data()
                    print('Thank you for using RMIT academics results system. Have a good day.')
                    return
                case _:
                    print('Invalid input. Please select one of the given options.')
            user_choice = self.menu()    

#------------------------------------------------------------------------------------------------------------------------

sys_arguments = sys.argv

if len(sys_arguments) == 3:            
    s_file = sys_arguments[2]
    c_file = sys_arguments[1]
    r_file = sys_arguments[0]
    
else:
    s_file = 'students.txt'
    c_file = 'courses.txt'
    r_file = 'results.txt'
operation1 = Operations()
operation1.run_operations(s_file, c_file, r_file)





