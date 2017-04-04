# all of this code can be copied later into the real file
# just doing this to test and make sure it all works on its own


'''
        takes a course and list of coursees and sees if the course conflicts with the others in the list
        listOfPrefs given does not include current course
        returns a boolean
'''
def hasNoConflicts(currentCourse, listOfPrefs, courseDict):
        # check if their time_id is the same
        for course in listOfPrefs:
                # make sure currentCourse != course bc that'll have the same time
                # hacky -1 solution to avoid courses we have already added a
                # student to
                if course != -1 and currentCourse != course and courseDict[currentCourse]['time'] == courseDict[course]['time']:
                        return False
        return True

'''
        takes the current course and the list of prefs
        returns a list of courses that conflict
'''
def coursesThatConflict(currentCourse, listOfPrefs, courseDict):
        conflicts = []
        for course in listOfPrefs:
                if course != -1 and courseDict[currentCourse]['time'] == courseDict[course]['time']:
                        # then it conflicts with this course, can be itself
                        conflicts.append(course)
        return conflicts

'''
        potential for overflow is defined by the popularity and room size
        overflow = room size - popularity
        positive or zero overflow means will not overflow
        negative overflow means has potential to overflow
        returns the course with the least potential for overflow
'''
def leastPotentialForOverflow(conflicts, courseDict):
        # if positive or zero has no potential to overflow
        # if negative, has potential, so looking for course with overflow closest to 0
        leastOverflowValue = float("-infinity")
        leastOverflowCourse = 0
        noOverflowList = []
        for course in conflicts:
                overflow = courseDict[course]['roomSize'] - courseDict[course]['popularity']
                if overflow >= 0:
                        # if there's a course with no overflow, then choose it (random one)
                        return course
                else:
                        if overflow > leastOverflowValue:
                                leastOverflowValue = overflow
                                leastOverflowCourse = course
        return leastOverflowCourse

# isNotFull will be 0 if it's full, so isNotFull is true if it's not full
def isNotFull(course, courseDict):
        # I think that the courses get assigned to the same room so this should be fine?
        return courseDict[course]['roomSize'] - len(courseDict[course]['students'])

def fillStudents(studentPrefs, courseDict):
        for student in studentPrefs:
                prefs = studentPrefs[student]
                for course in prefs:
                        if isNotFull(course, courseDict):
                                if  hasNoConflicts(course, prefs, courseDict):
                                        # if there's room in the course and it doesn't conflict with any other preferences
                                        courseDict[course]['students'].append(student)
                                        prefs[prefs.index(course)] = -1
        for student in studentPrefs:
                prefs = studentPrefs[student]
                for course in prefs:
                        if course != -1 and isNotFull(course, courseDict):
                                conflicts = coursesThatConflict(course, prefs, courseDict)
                                choice = leastPotentialForOverflow(conflicts, courseDict)
                                '''Need to change time analysis where it says to separate prefs into groups'''
                                for conflict in conflicts:
                                        prefs[prefs.index(conflict)] = -1



'''TESTING BELOW'''


# QUESTION: WHERE IS SCHEDULE DICT? IS IT IN THE FUNCTION OR IS IT JUST IN OUR CODE
'''
courseDict is a dict of dicts
courseId:
        'popularity': popularity                the popularity of the class
        'time': time_id                         the time slot it's in
        'room': room_id                         the id of the room it's in
        'roomSize': room_size_int              the size of the room it's in
        'students': students_list               list of the students in the course
                                                        this gets appended with our fill students
'''








