'''
This file contains functions that parse the inputs that are passed in as text
files.

ADAPTED FOR HAVERFORD DATA

'''

def parse_constraints_mil_time(constraints_name):
    """
Adds a dictionary in poistions 4 (the 5th and last element of the list) that
contains:
     * the time (in millitary time) of the start and end of the class
     * the days of the week as a list the class is on
To clarify, the output looks like:
    [rooms, courses, teacher_to_classes, times,mil_times]
where mil_times looks like:
    {class_id: [start,end,[days, of, week]]}
    """
    with open(constraints_name,'r') as constraints_file:
        file = constraints_file.read()
        file = file.split('\n')
        times = []
        for line in file:
            line = line.split('\t')
            if line[0]== "Rooms":
                break
            else:
                times.append(line)
        time_dict = {}
        time_dict_info = {}
        for time in times[1:]:
            time_day = time[1].split()
            days = []
            if time_day[1]=="PM" and time_day[0][:2] != '12':
                hour_min = time_day[0].split(':')
                start = (int(hour_min[0])+12)*100 + int(hour_min[1])
            else:
                hour_min = time_day[0].split(':')
                start = (int(hour_min[0]))*100 + int(hour_min[1])               

            if time_day[3]=="PM" and time_day[2][:2] != '12':
                hour_min = time_day[2].split(':')
                end = (int(hour_min[0])+12)*100 + int(hour_min[1])
            else:
                hour_min = time_day[2].split(':')
                end = (int(hour_min[0]))*100 + int(hour_min[1])
            for item in time_day[4:]:
                    days.append(item)
            time_dict_info[int(time[0])]=[start,end,days]
            time_dict[int(time[0])]=[]
        a = parse_constraints(constraints_name)
        a.append(time_dict_info)
        return a
def parse_constraints_wiggle(constraints_name):
    """
Adds a dictionary in poistions 4 (the 5th and last element of the list) that
contains:
     * the time (in millitary time) of the start and end of the class
     * the days of the week as a list the class is on
To clarify, the output looks like:
    [rooms, courses, teacher_to_classes, times,mil_times]
where mil_times looks like:
    {class_id: [start,end,[days, of, week]]}
    """
    with open(constraints_name,'r') as constraints_file:
        file = constraints_file.read()
        file = file.split('\n')
        times = []
        for line in file:
            line = line.split('\t')
            if line[0]== "Rooms":
                break
            else:
                times.append(line)
        time_dict = {}
        time_dict_info = {}
        for time in times[1:]:
            time_day = time[1].split()
            days = []
            if time_day[1]=="PM" and time_day[0][:2] != '12':
                hour_min = time_day[0].split(':')
                start = (int(hour_min[0])+12)*100 + int(hour_min[1])
            else:
                hour_min = time_day[0].split(':')
                start = (int(hour_min[0]))*100 + int(hour_min[1])               

            if time_day[3]=="PM" and time_day[2][:2] != '12':
                hour_min = time_day[2].split(':')
                end = (int(hour_min[0])+12)*100 + int(hour_min[1])
            else:
                hour_min = time_day[2].split(':')
                end = (int(hour_min[0]))*100 + int(hour_min[1])
            for item in time_day[4:]:
                    time_dict_info[time[0]+item]=[start,end,item,end-start]
                    time_dict[time[0]+item]=[]
        a = parse_constraints(constraints_name)
        a[3]=time_dict
        a.append(time_dict_info)
        return a

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
        return [rooms, courses, teacher_to_classes, times]
def make_new_contraints(constraints_name):
    with open(constraints_name,'r') as constraints_file:
        with open('new_'+constraints_name,'w') as new_file:
            old_constraints = constraints_file.read()
            change=False
            for line in old_constraints.split('\n'):
                if line[:8]=='Teachers':
                    change=True
                    new_file.write(line+'\n')
                    continue
                elif change==True:
                    course_teacher = line.split("\t")
                    if len(course_teacher)!=2:
                        #print "potential problem with", course_teacher
                        pass
                    else:
                        course = course_teacher[0]
                        teacher = course_teacher[1]
                        new_file.write(str(course)+"a\t"+teacher+'\n')
                        new_file.write(str(course)+"b\t"+teacher+'\n')
                        new_file.write(str(course)+"c\t"+teacher+'\n')
                else:
                    new_file.write(line+'\n')
def make_new_prefs(prefs_name):
    with open(prefs_name, 'r') as prefs_file:
        with open('new_'+prefs_name,'w') as new_file:
            old_prefs = prefs_file.read().split('\n')
            first = True
            for student_prefs in old_prefs:
                if first:
                    new_file.write(student_prefs+'\n')
                    first = False
                else:
                    student_prefs = student_prefs.split('\t')
                    if len(student_prefs)==2:
                        student = student_prefs[0]
                        prefs = student_prefs[1]
                        prefs = prefs.split()
                        new_pref=""
                        for pref in prefs:
                            new_pref += pref+'a '+pref+'b '+pref+'c '
                        new_file.write(student+'\t'+new_pref+'\n')
def parse_prefs(prefs_name):
    with open(prefs_name, 'r') as prefs_file:
        num_students = int(prefs_file.readline().split()[-1])
        student_prefs = {}
        for i in range(0, num_students):
            line = prefs_file.readline().split()
            student_id = int(line.pop(0))
            line = [int(num) for num in line]
            line = [num for num in line if line.count(num) < 2] #not fast
            student_prefs[student_id] = line
        return student_prefs
make_new_contraints("haverfordConstraints.txt")
make_new_prefs("haverfordStudentPrefs.txt")