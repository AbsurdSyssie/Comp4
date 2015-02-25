__author__ = 'Oscar'
import pickle, sys



from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class AdminTools(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)   
        
    def setupUi(self, AdminTools):
            AdminTools.setObjectName(_fromUtf8("AdminTools"))
            AdminTools.resize(400, 300)
            self.verticalLayout = QtGui.QVBoxLayout(AdminTools)
            self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
            self.Admin = QtGui.QPushButton(AdminTools)
            self.Admin.setObjectName(_fromUtf8("Admin"))
            self.verticalLayout.addWidget(self.Admin)
            self.Students = QtGui.QPushButton(AdminTools)
            self.Students.setObjectName(_fromUtf8("Students"))
            self.verticalLayout.addWidget(self.Students)
            self.Teachers = QtGui.QPushButton(AdminTools)
            self.Teachers.setObjectName(_fromUtf8("Teachers"))
            self.verticalLayout.addWidget(self.Teachers)
            self.Questions = QtGui.QPushButton(AdminTools)
            self.Questions.setObjectName(_fromUtf8("Questions"))
            self.verticalLayout.addWidget(self.Questions)
            self.QuestionSets = QtGui.QPushButton(AdminTools)
            self.QuestionSets.setObjectName(_fromUtf8("QuestionSets"))
            self.verticalLayout.addWidget(self.QuestionSets)
    
            self.retranslateUi(AdminTools)
            QtCore.QMetaObject.connectSlotsByName(AdminTools)
    
    def retranslateUi(self, AdminTools):
            AdminTools.setWindowTitle(_translate("AdminTools", "Admin Tools", None))
            self.Admin.setText(_translate("AdminTools", "Create / Change Admin Account", None))
            self.Students.setText(_translate("AdminTools", "Create / Clear Students Pickle", None))
            self.Teachers.setText(_translate("AdminTools", "Create / Clear Teachers", None))
            self.Questions.setText(_translate("AdminTools", "Create / Clear Questions", None))
            self.QuestionSets.setText(_translate("AdminTools", "Create / Clear Question Sets", None))
            self.Admin.clicked.connect(self.admincredentials)
            self.Students.clicked.connect(self.clearStudents)
            self.Teachers.clicked.connect(self.clearTeachers)
            self.Questions.clicked.connect(self.clearQuestions)
            self.QuestionSets.clicked.connect(self.clearQSets)
    
            
    def admincredentials(self):
        #launches MakeAdmin form
        thisForm = MakeAdmin()
        thisForm.exec_()
        
    
    def clearStudents(self):
        global students
        #loads student pickle
        with open('students.pickle', 'rb') as s:
            students = pickle.load(s)
        #checks if students.pickle is empty or not
        if students != []:
            self.areyousurestudents()
        else:
            students = []
            with open('students.pickle', 'wb') as f:
            # Pickle the 'data' dictionary using the highest protocol available.
                 pickle.dump(teachers, f, pickle.HIGHEST_PROTOCOL)    
    
            reply = QtGui.QMessageBox()
            reply.setText("students.pickle created.")
            reply.setIcon(1)
            reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
    
            ret = reply.exec_() 
            
    def clearTeachers(self):
        global teachers
        with open('teachers.pickle', 'rb') as t:
            teachers = pickle.load(t)
            #checks if teachers.pickle is empty or not
        if teachers != []:
            self.areyousureteachers()
        else:
            teachers = []
            with open('teachers.pickle', 'wb') as f:
                # Pickle the 'data' dictionary using the highest protocol available.
                pickle.dump(teachers, f, pickle.HIGHEST_PROTOCOL)
    
            reply = QtGui.QMessageBox()
            reply.setText("teachers.pickle created.")
            reply.setIcon(1)
            reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
    
            ret = reply.exec_()    
    def clearQuestions(self):
        global questions
        with open('questions.pickle', 'rb') as t:
            questions = pickle.load(t)
            #checks if questions.pickle is empty or not
        if questions != []:
            self.areyousurequestions()
        else:
            questions = []
            with open('questions.pickle', 'wb') as f:
                # Pickle the 'data' dictionary using the highest protocol available.
                pickle.dump(questions, f, pickle.HIGHEST_PROTOCOL)
            reply = QtGui.QMessageBox()
            reply.setText("questions.pickle created.")
            reply.setIcon(1)
            reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
    
            ret = reply.exec_()    
    def clearQSets(self):
        global QSets
        with open('QSets.pickle', 'rb') as t:
            QSets = pickle.load(t)
        if QSets != []:
            #checks if QSets.pickle is empty or not
            self.areyousureqsets()
        else:
            QSets = []
            with open('QSets.pickle', 'wb') as f:
                # Pickle the 'data' dictionary using the highest protocol available.
                pickle.dump(QSets, f, pickle.HIGHEST_PROTOCOL)
            reply = QtGui.QMessageBox()
            reply.setText("QSets.pickle created.")
            reply.setIcon(1)
            reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
    
            ret = reply.exec_()                
    def areyousureteachers(self):
        #opens message box asking for confirmation
            reply = QtGui.QMessageBox.question(self, 'Message',
                "Are you sure to clear teachers?\nThis will require a new Admin to be made.", QtGui.QMessageBox.Yes | 
                QtGui.QMessageBox.No, QtGui.QMessageBox.No) 
    
            if reply == QtGui.QMessageBox.Yes:
                teachers = []
                with open('teachers.pickle', 'wb') as f:
                    # Pickle the 'data' dictionary using the highest protocol available.
                    pickle.dump(teachers, f, pickle.HIGHEST_PROTOCOL)                
                          #either allow the event to happen, or ignore it
                reply = QtGui.QMessageBox()
                reply.setText("teachers.pickle cleared.")
                reply.setIcon(1)
                reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
        
                ret = reply.exec_()
                self.close()

    def areyousurestudents(self):
        #opens message box asking for confirmation
                reply = QtGui.QMessageBox.question(self, 'Message',
                    "Are you sure to clear students?", QtGui.QMessageBox.Yes | 
                    QtGui.QMessageBox.No, QtGui.QMessageBox.No) 
        
                if reply == QtGui.QMessageBox.Yes:
                    students = []
                    with open('students.pickle', 'wb') as f:
                        # Pickle the 'data' dictionary using the highest protocol available.
                        pickle.dump(students, f, pickle.HIGHEST_PROTOCOL)                
                              #either allow the event to happen, or ignore it
                    reply = QtGui.QMessageBox()
                    reply.setText("students.pickle cleared.")
                    reply.setIcon(1)
                    reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
            
                    ret = reply.exec_()                
                       
    def areyousurequestions(self):
        #opens message box asking for confirmation
                reply = QtGui.QMessageBox.question(self, 'Message',
                    "Are you sure to clear questions?", QtGui.QMessageBox.Yes | 
                    QtGui.QMessageBox.No, QtGui.QMessageBox.No) 
        
                if reply == QtGui.QMessageBox.Yes:
                    questions = []
                    with open('questions.pickle', 'wb') as f:
                        # Pickle the 'data' dictionary using the highest protocol available.
                        pickle.dump(questions, f, pickle.HIGHEST_PROTOCOL)                
                              #either allow the event to happen, or ignore it
                reply = QtGui.QMessageBox()
                reply.setText("questions.pickle cleared.")
                reply.setIcon(1)
                reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
        
                ret = reply.exec_()
                       
    
    def areyousureqsets(self):
        #opens message box asking for confirmation
                reply = QtGui.QMessageBox.question(self, 'Message',
                    "Are you sure to clear Question Sets?", QtGui.QMessageBox.Yes | 
                    QtGui.QMessageBox.No, QtGui.QMessageBox.No) 
        
                if reply == QtGui.QMessageBox.Yes:
                    QSets = []
                    with open('QSets.pickle', 'wb') as f:
                        # Pickle the 'data' dictionary using the highest protocol available.
                        pickle.dump(QSets, f, pickle.HIGHEST_PROTOCOL)                
                              #either allow the event to happen, or ignore it
                reply = QtGui.QMessageBox()
                reply.setText("QSets.pickle cleared.")
                reply.setIcon(1)
                reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
        
                ret = reply.exec_()                
                      
class MakeAdmin(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)      
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.passbox = QtGui.QLineEdit(Dialog)
        self.passbox.setObjectName(_fromUtf8("passbox"))
        self.verticalLayout.addWidget(self.passbox)
        self.Submit = QtGui.QPushButton(Dialog)
        self.Submit.setObjectName(_fromUtf8("Submit"))
        self.verticalLayout.addWidget(self.Submit)
        self.Cancel = QtGui.QPushButton(Dialog)
        self.Cancel.setObjectName(_fromUtf8("Cancel"))
        self.verticalLayout.addWidget(self.Cancel)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_2.setText(_translate("Dialog", "Administrator username = \"Admin\"", None))
        self.label.setText(_translate("Dialog", "Create Administrator Password:", None))
        self.Submit.setText(_translate("Dialog", "Submit", None))
        self.Cancel.setText(_translate("Dialog", "Cancel", None))
        self.Submit.clicked.connect(self.createAdmin)
        self.Cancel.clicked.connect(self.close)

    def createAdmin(self):
        replace = False
        #checks if a password has been entered
        if self.passbox.text() == "":
            reply = QtGui.QMessageBox()
            reply.setText("Please enter a password.")
            reply.setIcon(3)
            reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
    
            ret = reply.exec_()
        else:
            global teachers
            found = False
            with open('teachers.pickle', 'rb') as t:
                teachers = pickle.load(t)      
            #finds if an admin account exists
            for people in teachers:
                # if admin exists, delete it and make a new one with the entered password
                if people.username == "Admin":
                    print(people.username)
                    print(people.password)
                    teachers.remove(people)
                    replace = True
                    newAdmin = teacher("Admin", "A", self.passbox.text(), "Admin",
                                         "Admin", "Admin", [])
                    teachers.append(newAdmin)
                    with open('teachers.pickle', 'wb') as t:
                        pickle.dump(teachers, t, pickle.HIGHEST_PROTOCOL)
                    
                    self.Adminreplaced()
            #if an admin doesn't exist then make a new one
            if replace == False:    
                newAdmin = teacher("Admin", "A", self.passbox.text(), "Admin",
                                     "Admin", "Admin", [])
                teachers.append(newAdmin)
                with open('teachers.pickle', 'wb') as t:
                    pickle.dump(teachers, t, pickle.HIGHEST_PROTOCOL)
                                    
                self.Adminconfirmation()
                Admintools = AdminTools()
                Admintools.exec_()

    
    def Adminconfirmation(self):
            reply = QtGui.QMessageBox()
            reply.setText("Admin Created.")
            reply.setIcon(0)
            reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
    
            ret = reply.exec_()
            self.close()


    def Adminreplaced(self):
        reply = QtGui.QMessageBox()
        reply.setText("Admin Password Changed.")
        reply.setIcon(0)
        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)

        ret = reply.exec_()
        self.close()        
        
        
class LogInPage(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)


    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.PasswordBox = QtGui.QLineEdit(Form)
        self.PasswordBox.setEchoMode(QtGui.QLineEdit.Password)
        self.PasswordBox.setObjectName(_fromUtf8("PasswordBox"))
        self.verticalLayout.addWidget(self.PasswordBox)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Log In", "Log In", None))
        
        self.label_2.setText(_translate("Form", "Enter Admin Password:", None))
        self.pushButton.setText(_translate("Form", "Log In", None))
        self.pushButton_2.setText(_translate("Form", "Cancel", None))
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.checkCredentials)


    def checkCredentials(self, Form):
        

        self.isAdmin = False
        #goes through teachers.pickle and checks if entered password is correct 
        for people in teachers:
            if people.username == "Admin" and self.PasswordBox.text() == people.password:

                username = people.username

                if people.account_type == "A":
                    self.close()
                    #if the password is correct sets isAdmin to true
                    self.isAdmin = True
        if self.isAdmin == False:
            self.incorrectID()
        if self.isAdmin == True:
            #opens admin tools page
            adminpage = AdminTools()
            adminpage.exec_()
    def incorrectID(self):
        reply = QtGui.QMessageBox()
        reply.setText("Your Password is incorrect. Please try again.")
        reply.setIcon(0)
        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)

        ret = reply.exec_()
        reply.close()



#classes from main program
    
class teacher():
       def __init__(self, username, account_type, password, forename, surname, middlename, pupils):
           self.account_type = account_type
           self.username = username
           self.forename = forename
           self.password = password
           self.surname = surname
           self.middlename = middlename
    
           self.pupils = pupils


class student():
    def __init__(self, studentid, username, account_type, password, forename, surname, middlename, form, targetgrade,
                 questionsanswered, questionstoanswer, answeredcorrectly):
        self.forename = forename
        self.username = username
        self.account_type = account_type
        self.password = password
        self.surname = surname
        self.middlename = middlename
        self.answered = questionsanswered
        self.questionstoanswer = questionstoanswer
        self.answeredcorrectly = answeredcorrectly
        self.studentid = studentid
        self.form = form
        self.targetgrade = targetgrade

    def percentage(self):
        self.percentage = int((len(self.answeredcorrectly) / len(self.answered)) * 100)

        print(self.percentage)
        return self.percentage
    
    
    def findgrade(self):
        isOntarget = False
        self.percentage()
        x = self.percentage
        targetpercentage = 0
        if self.targetgrade == "A":
            targetpercentage = 75
        if self.targetgrade == "B":
            targetpercentage = 65
        if self.targetgrade == "C":
            targetpercentage = 55
        if self.targetgrade == "D":
            targetpercentage = 45
        if self.targetgrade == "E":
            targetpercentage = 35
        if self.targetgrade == "F":
            targetpercentage = 25
        if self.targetgrade == "U":
            targetpercentage == 0

        print(targetpercentage)
        if x > targetpercentage:
            isOntarget = True
        else:
            isOntarget = False

    def questionAnswered(self, question):
        for q in self.questionstoanswer:
            print(q.ID)
        self.questionstoanswer.remove(question)
        self.answered.append(question)
        with open('students.pickle', 'wb') as f:
            
            pickle.dump(students, f, pickle.HIGHEST_PROTOCOL)  

class Question(object):
        def __init__(self, ID, questiontype, values):
            self.question_type = questiontype
            self.ID = ID
            print("storing", self.ID)
            self.values = values
            if self.question_type == "Rate Constant":
                self.kQuestion()
            if self.question_type == "Hardy-Weinberg":
                self.hardy_weinberg()
    
        def kQuestion(self):
            self.conc_of_A = self.values[0]
            self.conc_of_B = self.values[1]
            self.rateOfReaction = self.values[2]
            self.order_of_A = self.values[3]
            self.order_of_B = self.values[4]
            
    
    
        def hardy_weinberg(self):
            self.totalpop = self.values[0]
            self.q_sqrdaspop = self.values[1]
            self.HWwindow
        
        def findK(self, window):
        
                QtGui.QApplication.processEvents()
                n = 0
                self.intermediary = pow(self.conc_of_A, self.order_of_A) * (pow(self.conc_of_B, self.order_of_B))
                self.k = self.rateOfReaction / self.intermediary
                correct = False
                window.label.setText(_translate("Form", "The conc of reactant A is " + str(
                    self.conc_of_A) + " moldm^-3. The conc of B is " + str(self.conc_of_B) + " moldm^-3\n"
                                                                                             "The order of A is " + str(
                    self.order_of_A) + " and the order of B is " + str(self.order_of_B) + ". The rate of reaction is " + str(
                    self.rateOfReaction), None))
        def HWwindow(self):
            window.label.setText(_translate("hardy_weinberg", "If " + str(self.q_sqrdaspop) + " out of " + str(
                    self.totalpop) + " individuals in a population express the recessive phenotype, what percent of the population would you predict would be heterozygotes? ",
                    None))       
    
    
class Question_Set(object):
        def __init__(self, ID, name, newQList, owner):
            self.QID = ID
            self.name = name
            self.QList = newQList
            self.owner = owner


def checkadmin():
        global teachers
        found = False
        with open('teachers.pickle', 'rb') as t:
            teachers = pickle.load(t)        
        for people in teachers:
            if people.username == "Admin":
                found = True
                break
        if found == True:
            app = QtGui.QApplication(sys.argv)
            thisForm = LogInPage()
            thisForm.show()
            sys.exit(app.exec_())
        
        if found == False:
            app = QtGui.QApplication(sys.argv)
            thisForm = MakeAdmin()
            thisForm.show()
            sys.exit(app.exec_())


checkadmin()


