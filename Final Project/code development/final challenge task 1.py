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
    def __init__(self, course_ID):
        self.course_ID = course_ID

    def get_course_ID(self):
        return self.course_ID

    def display_info(self):
        print(f"Course ID : {self.course_ID}")

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------


class Result:
    students = list()
    courses = list()
    results = dict()

    score_list = list()


#.........................................................................

#read data functions
    def read_students(self, file_name):
        try:            
            with open(file_name,'r') as student_file:
                for line in student_file:
                    row = [x.strip().upper() for x in line.strip().split(',')]      #list comprehension, the first splits strips spaces off of indiviual attributes, second for whole line 
                    student_ID = row[0]
                    student = Student(student_ID)
                    self.students.append(student)
            return True
        except:
            return False


    def read_courses(self, file_name):
        try:            
            with open(file_name,'r') as course_file:
                for line in course_file:
                    row = [y.strip().upper() for y in line.strip().split(',')]
                    course_ID = row[0]
                    course = Course(course_ID)
                    self.courses.append(course)
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
                        self.score_list.append(score)
                    else:
                        score = '--'
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

    def calculate_pass_rate(self, score_list):
        i = 0
        j = len(score_list)
        for score in score_list:
            if score >= 49.5:
                i += 1
        pass_rate = (i / j) * 100
        return pass_rate

    


    def display_results(self):
        
        #Print the table header
        sys.stdout.write('{:<15}'.format('Student IDs'))
        for course in self.courses:
            sys.stdout.write('{:>15}'.format(course.get_course_ID()))
        print()
        
        # Print the table rows
        for student in self.students:
            student_ID = student.get_student_ID()
            sys.stdout.write('{:<15}'.format(student_ID))

            for course in self.courses:
                course_ID = course.get_course_ID()
                if (student in self.results) and (course in self.results[student]):
                    sys.stdout.write('{:>15}'.format(self.results[student][course]))       
                else:
                    sys.stdout.write('{:>15}'.format(''))
            print()
        
        #Results summary
        no_of_students = len(self.students)
        no_of_courses = len(self.courses)
        pass_rate = self.calculate_pass_rate(self.score_list)
        print('RESULTS SUMMARY')
        print(f"There are {no_of_students} students and {no_of_courses} courses.")                
        print(f"The average pass rate is {pass_rate:.2f}%.")
    


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
    def run_operations(self, s_file, c_file, r_file):
        if not self.load_data(s_file, c_file, r_file):
            return
        else:
            self.result.display_results()
           

    

#------------------------------------------------------------------------------------------------------------------------

s_file = 'students.txt'
c_file = 'courses.txt'
r_file = 'results.txt'


operation1 = Operations()
operation1.run_operations(s_file, c_file, r_file)





