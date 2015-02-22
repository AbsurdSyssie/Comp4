__author__ = 'Oscar'
import pickle

def admincredentials():
        global adminPage
        adminPage = Createcredentials()
        adminPage.show()


def loadStudents():
    global students
    with open('C:\\Users\Oscar\Documents\GitHub\Comp4\Program\students.pickle', 'rb') as s:
        students = pickle.load(s)

        for people in students:
            # empty = []
            # people.questionstoanswer = empty
            print(people.username, people.password, people.studentid, people.questionstoanswer)
            # with open('students.pickle', 'wb') as f:
            # pickle.dump(students, f, pickle.HIGHEST_PROTOCOL)



def clearTeachers():
    global teachers
    with open('teachers.pickle', 'rb') as t:
        teachers = pickle.load(t)
    if teachers != []:
        areyousure()
    else:
        teachers = []
        with open('teachers.pickle', 'wb') as f:
            # Pickle the 'data' dictionary using the highest protocol available.
            pickle.dump(teachers, f, pickle.HIGHEST_PROTOCOL)


def clearQuestions():
    global questions
    with open('questions.pickle', 'rb') as t:
        questions = pickle.load(t)
    if questions != []:
        areyousure()
    else:
        questions = []
        with open('questions.pickle', 'wb') as f:
            # Pickle the 'data' dictionary using the highest protocol available.
            pickle.dump(questions, f, pickle.HIGHEST_PROTOCOL)

def clearQSets():
    global QSets
    with open('QSets.pickle', 'rb') as t:
        QSets = pickle.load(t)
    if QSets != []:
        areyousure()
    else:
        QSets = []
        with open('QSets.pickle', 'wb') as f:
            # Pickle the 'data' dictionary using the highest protocol available.
            pickle.dump(QSets, f, pickle.HIGHEST_PROTOCOL)

def areyousure():
    clearQSets()
    print("You can code!")

areyousure()