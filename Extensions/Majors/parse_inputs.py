'''
This file contains functions that parse the inputs that are passed in as text
files.

ADAPTED FOR HAVERFORD DATA
Majors Version!
'''

def parse_constraints(constraints_name):
    with open(constraints_name,'r') as constraints_file:
        #last number of first line is number of time slots
        num_times = int(constraints_file.readline().split()[-1])
        times = {x:[] for x in range(1,num_times+1)}
        for i in range (0, num_times):
            constraints_file.readline()
        #set up rooms array
        num_rooms = int(constraints_file.readline().split()[-1])
        rooms = {}
        for i in range(0,num_rooms):
            line = constraints_file.readline().split()
            room_id = line[0]
            room_size = int(line[1])
            rooms[room_id] = room_size

        num_classes = int(constraints_file.readline().split()[-1])
        courses = [0] * num_classes

        num_teachers = int(constraints_file.readline().split()[-1])
        teacher_to_classes = {}
        for i in range(0,num_classes):
            line = constraints_file.readline().split()
            class_id = int(line[0])
            courses[i] = class_id
            try:
                teacher_id = int(line[1])
            except IndexError:
                teacher_id = '0'
            if not (teacher_id in teacher_to_classes):
                teacher_to_classes[teacher_id] = []
            teacher_to_classes[teacher_id].append(class_id)
        courses.sort()


        course_to_major = {}
        constraints_file.readline()
        for i in range(0,num_classes):
            line = constraints_file.readline().split()
            class_id = int(line[0])
            major = line[1]
            course_to_major[class_id] = major
        

        return (rooms, courses, teacher_to_classes, times, course_to_major)

def parse_prefs(prefs_name):
    with open(prefs_name, 'r') as prefs_file:
        num_students = int(prefs_file.readline().split()[-1])
        student_prefs = {}
        student_to_major = {}
        for i in range(0, num_students):
            line = prefs_file.readline().split()
            student_id = int(line.pop(0))
            student_prefs[student_id] = []
            for e in line:
                    try:
                        if (not int(e) in student_prefs[student_id]):
                            student_prefs[student_id].append(int(e))
                    except ValueError:
                        student_to_major[student_id] = e
            #line = [int(num) for num in line]
            #line = [num for num in line if line.count(num) < 2] #not fast
            #student_prefs[student_id] = line
        return (student_prefs, student_to_major)

