from fill_students import *

def make_popularity_list (courses_dictionary, con_mat):
        #this section is the popularityList from the write-up
        popularity = [] 
        for course in courses_dictionary:       #this structure is modeled after the con_mat lake built
                popularity.append((course,con_mat[(course,course)]))
        popularity.sort(key= lambda student: student[1])
        #print popularity
        return popularity

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
                conflict_dict[(teacher_dictionary[teacher][0],teacher_dictionary[teacher][1])] = float('inf')
                conflict_dict[(teacher_dictionary[teacher][1],teacher_dictionary[teacher][0])] = float('inf')
        #print conflict_dict
        return conflict_dict

def assign_rooms(class_times_dict, rooms, con_mat):
    class_to_room = {}
    big_rooms = sorted(rooms, reverse = True)
    for slot in class_times_dict:
        #sort descending based on popularity
        pop_slot = sorted(class_times_dict[slot], key = lambda x: con_mat[(x,x)], reverse = True)
        counter = 0
        for pop_course in pop_slot:
            class_to_room[pop_course] = big_rooms[counter]
            counter += 1
    return class_to_room

def courseAssignment(courses, rooms, courseTimesDict, teachers, studentPrefs):  
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
                        
        print courseTimesDict
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

courseList = [1, 2, 3, 4]
conflict_matrix = {(1,1):4, (1,2):2, (1,3):0, (1,4):2, (2,1):2, (2,2):8, (2,3):5, (2,4):1, (3,1):0, (3,2):5, (3,3):5, (3,4):0, (4,1):2, (4,2):1, (4,3): 0, (4,4):3}

teachers = {1:(1,3), 2:(2,4)}
inv_teachers = {}
for teacher in teachers:
    for course_taught in teachers[teacher]:
        inv_teachers[course_taught] = teacher
students = {1:[1, 4], 2:[4, 1], 3:[2, 1], 4:[1, 2], 5:[2, 3], 6:[3, 2], 7:[3, 2], 8:[3, 2], 9:[3, 2], 10:[2,4]}

times = {1:[], 2:[]}

rooms = {1:2, 2:8}

courseListNew = courseAssignment(courseList, rooms, times, teachers, students)
