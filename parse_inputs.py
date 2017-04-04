'''
This file contains functions that parse the inputs that are passed in as text
files. Currently they assume that all ids are integers. This will have to be
adapted for the Haverford data.

'''

def parse_constraints(constraints_name):
    with open(constraints_name,'r') as constraints_file:
        #last number of first line is number of time slots
        num_times = int(constraints_file.readline().split()[-1])
        times = {x:[] for x in range(1,num_times+1)}

        #set up rooms array
        num_rooms = int(constraints_file.readline().split()[-1])
        rooms = {}
        for i in range(0,num_rooms):
            line = constraints_file.readline().split()
            room_id = int(line[0])
            room_size = int(line[1])
            rooms[room_id] = room_size

        num_classes = int(constraints_file.readline().split()[-1])
        courses = [0] * num_classes

        num_teachers = int(constraints_file.readline().split()[-1])
        teacher_to_classes = {x:[] for x in range(1,num_teachers+1)}
        for i in range(0,num_classes):
            line = constraints_file.readline().split()
            class_id = int(line[0])
            courses[i] = class_id
            teacher_id = int(line[1])
            teacher_to_classes[teacher_id].append(class_id)
        return (rooms, courses, teacher_to_classes, times)

def parse_prefs(prefs_name):
    with open(prefs_name, 'r') as prefs_file:
        num_students = int(prefs_file.readline().split()[-1])
        student_prefs = {}
        for i in range(0, num_students):
            line = prefs_file.readline().split()
            student_id = int(line.pop(0))
            line = [int(num) for num in line]
            student_prefs[student_id] = line
        return student_prefs


