'''
This file accepts the command line arguments and actually makes the schedule.
'''

from random import randint
import argparse

import parse_inputs

from fill_students import *
from make_output import *

parser = argparse.ArgumentParser(description='Create a schedule', usage =
                                 '<constraints> <preferences> <output>. [-h] for help.')
parser.add_argument('constraints', type=str, nargs=1,
                    help='Name of constraints file.')
parser.add_argument('preferences', type=str, nargs=1,
                    help='Name of student preferences file.')
parser.add_argument('output', type=str, nargs = 1,
                    help='Name of output file.')

args = parser.parse_args()

constraints = parse_inputs.parse_constraints(args.constraints[0])
# rooms is a dictionary that maps room id to capacity
rooms = constraints[0]

# courses is a list of course ids
courses = constraints[1]

# teachers is a dictionary that maps teacher id to the courses they teach
teachers = constraints[2]

# inv_teachers is the inversion of teachers that maps course ids to teacher ids
inv_teachers = {}
for teacher in teachers:
    for course_taught in teachers[teacher]:
        inv_teachers[course_taught] = teacher

# times is a dictionary that maps time slot ids to the classes in that time slot
# all slots start empty
times = constraints[3]

studentPrefs = parse_inputs.parse_prefs(args.preferences[0])



#some restructuring of other functions to make them work with the new conflict matrix might need to happen
def make_conflict_matrix(student_dictionary, teacher_dictionary, courses_dictionary):
	conflict_dict = {}
	#initializes conflict_dict:
	for course_first in courses_dictionary:
                for course_second in courses_dictionary:
                        conflict_dict[(course_first,course_second)] = 0
                        
	for student in student_dictionary:
                cur_pref_list = student_dictionary[student]
                for i in range (0, len(cur_pref_list)):
                        for j in range (i, len(cur_pref_list)):
                                conflict_dict[(cur_pref_list[i],cur_pref_list[j])] += 1
				if i != j:
                                	conflict_dict[(cur_pref_list[j],cur_pref_list[i])] += 1
        
        for teacher in teacher_dictionary:
                for course_first in teacher_dictionary[teacher]:
                        for course_second in teacher_dictionary[teacher]:
                                if course_first != course_second:
                                        conflict_dict[(course_first, course_second)] = float('inf')
                #conflict_dict[(teacher_dictionary[teacher][0],teacher_dictionary[teacher][1])] = float('inf')
                #conflict_dict[(teacher_dictionary[teacher][1],teacher_dictionary[teacher][0])] = float('inf')
        return conflict_dict


def assign_rooms(class_times_dict, rooms, con_mat):
    class_to_room = {}
    big_rooms = sorted(rooms, key = lambda x: rooms[x], reverse = True)
    for slot in class_times_dict:
        #sort descending based on popularity
        pop_slot = sorted(class_times_dict[slot], key = lambda x: con_mat[(x,x)], reverse = True)
        counter = 0
        for pop_course in pop_slot:
            class_to_room[pop_course] = big_rooms[counter]
            counter += 1
    return class_to_room


def make_popularity_list (courses_dictionary, con_mat):
	#this section is the popularityList from the write-up
	popularity = []	
	for course in courses_dictionary:       #this structure is modeled after the con_mat lake built
		popularity.append((course,con_mat[(course,course)]))
	popularity.sort(key= lambda student: student[1], reverse = True)
	#print popularity
	return popularity


		

# this function is almost identical with the pseudocode. It is responsible for
# creating the dictionary that maps a course to its teacher, room, students,
# and time. It calls several helper functions.
def courseAssignment(courses, rooms, courseTimesDict, teachers, studentPrefs,
                     inv_teachers):  
        courseToTime = {course: None for course in courses}
        conflicts = make_conflict_matrix(studentPrefs, teachers, courses)
        popularities = make_popularity_list(courses, conflicts)
        for course in popularities:
                bestSlot = None
                bestConflictNum = float('inf')
                for time in courseTimesDict:
                        tempConflictNum = 0
                        for conflictingCourse in courseTimesDict[time]:
                                tempConflictNum += conflicts[(conflictingCourse, course[0])]
                        if (tempConflictNum < bestConflictNum and len(courseTimesDict[time]) < len(rooms)):
                                bestSlot = time
                                bestConflictNum = tempConflictNum
                if bestSlot != None:
                        courseTimesDict[bestSlot].append(course[0])
                        courseToTime[course[0]] = bestSlot
                        
        roomDict = assign_rooms(courseTimesDict, rooms, conflicts)
        courseDict = { course:{
        'room': roomDict[course],
        'roomSize': rooms[roomDict[course]],
        'popularity': conflicts[course, course],
        'teacher': inv_teachers[course],
        'time': courseToTime[course],
        'students': []
        } for course in courses}


        fillStudents(studentPrefs, courseDict)
        return courseDict

#c = 100
#students = make_student_dictionary(c,1000)

#con_mat = make_conflict_matrix(studentPrefs,teachers,courses)


#teachers = make_teachers(c)


#rooms = [20, 30, 30, 40]

#class_times = {1:[0],2:[0],3:[0],4:[0],5:[0],6:[0]}

#make_schedule(class_times,rooms,students,teachers,con_mat,c)

courseListNew = courseAssignment(courses, rooms, times, teachers, studentPrefs,
                                 inv_teachers)

make_output(courseListNew, args.output[0])

print "Done!"













"""
def make_student_dictionary(c,s):
	student_dictionary = {}
	for student in range(0,s):
		student_dictionary[student]=[randint(0,c)]
		while len(student_dictionary[student]) != 4:
			new_class = randint(0,c)
			if new_class not in student_dictionary[student]:
				student_dictionary[student].append(new_class)
	return student_dictionary


def make_teachers(c):
	teachers={}
	n = 0
	for cc in range(0,c/2):
		teachers[cc]= [n,n+1]
		n+=1
	return teachers

#this running time is courses^2 * students new function is better and modeled after pseudocode
def make_conflict_matrix(student_dictionary,c):
	conflict_dict = {}
	for i in range(0,c):
		for j in range(0,c):
			conflict_dict[(i,j)] = 0
			for student in student_dictionary:
				if i in  student_dictionary[student] and j in  student_dictionary[student]:
					conflict_dict[(i,j)] += 1
	return conflict_dict

def make_schedule(class_times,rooms,students,teachers,con_mat,c, courses_dictionary):   
                #not sure if we need all of these inputs... especially c
        
	
	for key in class_times:
		class_times[key].append(popularity.pop())
	print class_times
	while len(popularity) != 0:
		current = popularity.pop()
		min_conflict = (55,1000000)     #what are these numbers based on?? -lake
		for time in class_times:
			conflict = 0
			for item in class_times[time][1:]:
				conflict += con_mat[(item[0],current[0])]
			if conflict<min_conflict[1]:
				min_conflict = (time, conflict)
		class_times[min_conflict[0]].append(current)
		class_times[min_conflict[0]][0] += min_conflict[1]
	print class_times
	total = 0
	for key in class_times:
		total += class_times[key][0]
	print "Total Conflict:",total

"""


