import sys
import os
from datetime import datetime
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------


class Student:
    def __init__(self, student_ID, student_name, student_type, student_mode):
        self.student_ID = student_ID
        self.student_name = student_name
        self.student_type = student_type
        self.student_mode = student_mode

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
                    row = [x.strip().upper() for x in line.strip().split(',')]      #list comprehension, the first splits strips spaces off of indiviual attributes, second for whole line 
                    student_ID = row[0]
                    if not student_ID.startswith('S'):
                        return False
                    student_name = row[1].title()
                    student_type = row[2]
                    if len(row) == 4:
                        student_mode = row[3]
                    else:
                        student_mode = 'FT'
                    student = Student(student_ID, student_name, student_type, student_mode)
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
                    if course_ID[:4] not in ['COSC', 'ISYS', 'MATH']:
                        return False
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
            if not self.results:
                return False
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

    #update reports file to save timestamp 
    def get_timestamp(self):
        now = datetime.now()
        timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
        report = f"Report generated at {timestamp}"
        return report



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

    def find_difficult_course(self, course_type):
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

    def calculate_student_average(self, student):
        total_score = 0
        mini_score = 0
        n_finish = 0
        non_going = 0
        for course in self.results[student]:
            if type(self.results[student][course]) == float:
                score = self.results[student][course]
                total_score += score
                n_finish += 1
                if score >= 79.5:
                    mini_score += 4
                elif score >= 69.5 and score < 79.5:
                    mini_score += 3
                elif score >= 59.5 and score < 69.5:
                    mini_score += 2
                elif score >= 49.5 and score < 59.5:
                    mini_score += 1    
            else:
                non_going += 1
                 
        GPA100 = total_score / n_finish
        GPA4 = mini_score / n_finish
        return GPA100, GPA4, n_finish, non_going

#.........................................................................

    def find_best_student(self, student_type):
        best_gpa = 0
        student_list = list()
        for student in self.students:
            if student.get_student_type() == student_type:
                new_gpa = self.calculate_student_average(student)[1]
                if new_gpa > best_gpa:
                    best_gpa = new_gpa
                    student_list.append(student)

        return student_list[len(student_list)-1]

#.........................................................................

    
    #this function displays the required result and writes all the ouptut into the reports file as well
    def display_results(self, reports_file_name):        
        report_file = open(reports_file_name, 'a')
        report_file.seek(0, 0)
        
        print('\n\n')
        report_file.write('\n \n')

        report_file.write(str(self.get_timestamp()) + '\n')

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
        report_file.close()
#.........................................................................


    def display_courses(self, reports_file_name):
        report_file = open(reports_file_name, 'a')
        report_file.seek(0, 0)
        
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
        
#.........................................................................

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
3. Display the student info
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
                case '3':
                    self.result.display_students(reports_file_name)
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
    print('[Usage:] python my_school.py <result_file> <course_file> <student_file>')
    s_file = 'students.txt'
    c_file = 'courses.txt'
    r_file = 'results.txt'
    operation1 = Operations()
    operation1.run_operations(s_file, c_file, r_file)





