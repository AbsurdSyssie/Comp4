__author__ = 'Oscar'
import random, decimal, sys, pickle, math
from PyQt4 import QtCore, QtGui
from math import log10, floor

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

# start of main
# students = []
teachers = []


class teacher():
    def __init__(self, username, account_type, password, forename, surname, middlename, pupils):
        self.account_type = account_type
        self.username = username
        self.forename = forename
        self.password = password
        self.surname = surname
        self.middlename = middlename

        self.pupils = pupils


class Teacher_Main_Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 324)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)

        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.verticalLayout.addWidget(self.pushButton_6)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout.addWidget(self.pushButton_4)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.editAcc = QtGui.QPushButton(Form)
        self.editAcc.setObjectName(_fromUtf8("editAcc"))
        self.verticalLayout.addWidget(self.editAcc)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout.addWidget(self.pushButton_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Logged in as " + username, None))
        self.pushButton_3.setText(_translate("Form", "Set Questions", None))
        self.pushButton_2.setText(_translate("Form", "Add Questions", None))
        self.pushButton.setText(_translate("Form", "See Student Progress", None))
        self.pushButton_4.setText(_translate("Form", "Add New Account", None))
        self.editAcc.setText(_translate("Form", "Edit Accounts", None))
        self.pushButton_6.setText(_translate("Form", "Make QSet", None))
        self.pushButton_5.setText(_translate("Form", "Log Out", None))
        self.pushButton_4.clicked.connect(self.showCreateNewAccountWindow)
        self.pushButton_5.clicked.connect(self.close)
        self.pushButton_5.clicked.connect(self.showLoginPage)
        self.pushButton_2.clicked.connect(self.showNewq)
        self.pushButton_3.clicked.connect(self.showSetQuestions)
        self.pushButton_6.clicked.connect(self.makeQSet)
        self.editAcc.clicked.connect(self.openEditStudents)



    def openEditStudents(self):
        editac = EditStudents()
        editac.exec_()
    def makeQSet(self):

        myMakeQSet = MakeQSet(QSets)
        myMakeQSet.exec_()

    def showSetQuestions(self):
        Setquestions = SetQuestions()
        Setquestions.exec_()

    def showLoginPage(self):
        myLogInPage = LogInPage()
        myLogInPage.exec_()
    def showCreateNewAccountWindow(self):
        global newAccountForm
        newAccountForm = createaccount()
        newAccountForm.show()

    def showNewq(self):
        global newQForm
        newQForm = AddQuestion()
        newQForm.show()


class SetQuestions(QtGui.QDialog):
    def __init__(self):

        QtGui.QDialog.__init__(self)

        self.setupUi(self)


    def setupUi(self, Form):

        Form.setObjectName(_fromUtf8("Form"))

        Form.resize(682, 593)

        self.verticalLayout = QtGui.QVBoxLayout(Form)

        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.verticalLayout_2 = QtGui.QVBoxLayout()

        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))

        self.label = QtGui.QLabel(Form)

        self.label.setObjectName(_fromUtf8("label"))

        self.verticalLayout_2.addWidget(self.label)

        self.FormBox = QtGui.QComboBox(Form)

        self.FormBox.setObjectName(_fromUtf8("FormBox"))

        self.FormBox.addItem(_fromUtf8(""))

        self.verticalLayout_2.addWidget(self.FormBox)

        self.StudentBox = QtGui.QComboBox(Form)

        self.StudentBox.setObjectName(_fromUtf8("StudentBox"))

        self.verticalLayout_2.addWidget(self.StudentBox)

        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(spacerItem)

        self.label_2 = QtGui.QLabel(Form)

        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.verticalLayout_2.addWidget(self.label_2)

        self.QuestionSetBox = QtGui.QComboBox(Form)

        self.QuestionSetBox.setObjectName(_fromUtf8("QuestionSetBox"))

        self.verticalLayout_2.addWidget(self.QuestionSetBox)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.SubmitButton = QtGui.QPushButton(Form)

        self.SubmitButton.setObjectName(_fromUtf8("SubmitButton"))

        self.verticalLayout.addWidget(self.SubmitButton)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):

        Form.setWindowTitle(_translate("Form", "Form", None))

        self.label.setText(_translate("Form", "Select Student:", None))

        self.FormBox.setItemText(0, _translate("Form", "", None))

        self.label_2.setText(_translate("Form", "Select Question Set:", None))

        self.SubmitButton.setText(_translate("Form", "Submit", None))
        self.populateQSets
        self.FormBox.activated[str].connect(self.populatepupils)
        self.populateforms()
        self.populateQSets()
        self.SubmitButton.clicked.connect(self.giveQuestions)
        self.SubmitButton.clicked.connect(self.checks)
        
    def checks(self):
        if self.StudentBox.currentText() == "":
                reply = QtGui.QMessageBox()
                reply.setText("Please Select a Student.")
                reply.setIcon(3)
                reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
        
                ret = reply.exec_()
        if self.QuestionSetBox.currentText() == "":    
            reply = QtGui.QMessageBox()
            reply.setText("Please Select a Question Set.")
            reply.setIcon(3)
            reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
    
            ret = reply.exec_()
    def populateforms(self):

        AllItems = []
        for people in students:

            if not people.form in AllItems:
                self.FormBox.addItem(people.form)
                AllItems.append(people.form)

    def populatepupils(self, text):
        if text != "":
            self.StudentBox.clear()
            self.StudentBox.addItem("All")
            for people in students:
                if people.form == text:
                    self.StudentBox.addItem(people.username)
            
        else:
                    self.StudentBox.clear()
    
    def populateQSets(self):
        AllItems = []
        for n in range(len(QSets) - 1):
            if not QSets[n + 1].name in AllItems:
                self.QuestionSetBox.addItem(QSets[n + 1].name)
                AllItems.append(QSets[n + 1].name)

    def giveQuestions(self):
        if self.StudentBox.currentText() == "All":
            print("hi all")
            for people in students:
                if people.form == self.FormBox.currentText():
                    print("hi again")
 
                    for question in QSets[self.QuestionSetBox.currentIndex()+1].QList:
                        if question not in people.questionstoanswer:
                            people.questionstoanswer.append(question)
                            print("Adding")
                        with open('students.pickle', 'wb') as f:
                            pickle.dump(students, f, pickle.HIGHEST_PROTOCOL)
        else:

            for people in students:
                if people.username == self.StudentBox.currentText():
                    print("hi")
                    if not self.QuestionSetBox.currentText() in people.questionstoanswer:
                        print("Adding")
                        for question in QSets[self.QuestionSetBox.currentIndex()+1].QList:
                            
                            people.questionstoanswer.append(question)
                        with open('students.pickle', 'wb') as f:
                            pickle.dump(students, f, pickle.HIGHEST_PROTOCOL)


class createaccount(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(606, 632)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 586, 612))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_8 = QtGui.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_2.addWidget(self.label_8)
        self.teacherCheck = QtGui.QRadioButton(self.scrollAreaWidgetContents)
        self.teacherCheck.setObjectName(_fromUtf8("teacherCheck"))
        self.verticalLayout_2.addWidget(self.teacherCheck)
        self.studentCheck = QtGui.QRadioButton(self.scrollAreaWidgetContents)
        self.studentCheck.setObjectName(_fromUtf8("studentCheck"))
        self.verticalLayout_2.addWidget(self.studentCheck)
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.forenameBox = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.forenameBox.setObjectName(_fromUtf8("forenameBox"))
        self.verticalLayout_2.addWidget(self.forenameBox)
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.middlenameBox = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.middlenameBox.setObjectName(_fromUtf8("middlenameBox"))
        self.verticalLayout_2.addWidget(self.middlenameBox)
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.surnameBox = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.surnameBox.setObjectName(_fromUtf8("surnameBox"))
        self.verticalLayout_2.addWidget(self.surnameBox)
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.passwordBox = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.passwordBox.setObjectName(_fromUtf8("passwordBox"))
        self.verticalLayout_2.addWidget(self.passwordBox)
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.usernameBox = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.usernameBox.setObjectName(_fromUtf8("usernameBox"))
        self.verticalLayout_2.addWidget(self.usernameBox)
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.formBox = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.formBox.setObjectName(_fromUtf8("formBox"))
        self.verticalLayout_2.addWidget(self.formBox)
        self.label_7 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_2.addWidget(self.label_7)
        self.gradeBox = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.gradeBox.setObjectName(_fromUtf8("gradeBox"))
        self.verticalLayout_2.addWidget(self.gradeBox)
        self.submitButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.submitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitButton.setObjectName(_fromUtf8("submitButton"))
        self.verticalLayout_2.addWidget(self.submitButton)
        self.cancelButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.verticalLayout_2.addWidget(self.cancelButton)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.teacherCheck, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_6.hide)
        QtCore.QObject.connect(self.teacherCheck, QtCore.SIGNAL(_fromUtf8("clicked()")), self.formBox.hide)
        QtCore.QObject.connect(self.teacherCheck, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_7.hide)
        QtCore.QObject.connect(self.teacherCheck, QtCore.SIGNAL(_fromUtf8("clicked()")), self.gradeBox.hide)
        QtCore.QObject.connect(self.studentCheck, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_6.show)
        QtCore.QObject.connect(self.studentCheck, QtCore.SIGNAL(_fromUtf8("clicked()")), self.formBox.show)
        QtCore.QObject.connect(self.studentCheck, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_7.show)
        QtCore.QObject.connect(self.studentCheck, QtCore.SIGNAL(_fromUtf8("clicked()")), self.gradeBox.show)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Logged in as " + username, None))
        self.label_8.setText(_translate("Form", "Create Account", None))
        self.teacherCheck.setText(_translate("Form", "Teacher", None))
        self.studentCheck.setText(_translate("Form", "Student", None))
        self.label.setText(_translate("Form", " First Name:", None))
        self.label_2.setText(_translate("Form", "Middle Name(if applicable):", None))
        self.label_4.setText(_translate("Form", "Surname:", None))
        self.label_3.setText(_translate("Form", "Password:", None))
        self.label_5.setText(_translate("Form", "Username:", None))
        self.label_6.setText(_translate("Form", "Form:", None))
        self.label_7.setText(_translate("Form", "Target Grade:", None))
        self.submitButton.setText(_translate("Form", "Submit", None))
        self.cancelButton.setText(_translate("Form", "Cancel", None))
        self.submitButton.clicked.connect(self.checktype)


    def checktype(self):
        valid = True
        if (not self.studentCheck) and (not self.teacherCheck):
            self.fieldsNotComplete()
        if self.studentCheck.isChecked() == True:
            for people in teachers:
                if self.usernameBox.text() == people.username:
                    self.usernameinuse()
                    valid = False            
            for people in students:
                if self.usernameBox.text() == people.username:
                    self.usernameinuse()
                    valid = False
            if self.gradeBox.text() == "" or self.formBox.text() == "" or self.surnameBox.text() == "" or self.forenameBox.text() == "" or self.passwordBox.text() == "" or self.usernameBox.text() == "":
                self.fieldsNotComplete()
                valid = False
            if valid == True:
                self.create_new_Student()
                self.close()
        
        if self.teacherCheck.isChecked() == True:
            
                for people in teachers:
                    if self.usernameBox.text() == people.username:
                        self.usernameinuse()
                        valid = False
                for people in students:
                    if self.usernameBox.text() == people.username:
                        self.usernameinuse()
                        valid = False                    
                if self.surnameBox.text() == "" or self.forenameBox.text() == "" or self.passwordBox.text() == "" or self.usernameBox.text() == "":
                            self.fieldsNotComplete()
                            valid = False
                if valid == True:
                        self.create_new_Teacher()

    def usernameinuse(self):
        reply = QtGui.QMessageBox()
        reply.setText("That username is already in use.")
        reply.setIcon(3)
        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)

        ret = reply.exec_()

    def fieldsNotComplete(self):
        reply = QtGui.QMessageBox()
        reply.setText("Some fields are not complete.")
        reply.setIcon(3)
        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)

        ret = reply.exec_()


    def create_new_Student(self):

        student_id = len(students) + 1
        newstudent = student(student_id, self.usernameBox.text(), "S", self.passwordBox.text(), self.forenameBox.text(),
                             self.surnameBox.text(), self.middlenameBox.text(), self.formBox.text(),
                             self.gradeBox.text(), [], [], [])
        students.append(newstudent)
        with open('students.pickle', 'wb') as f:
            pickle.dump(students, f, pickle.HIGHEST_PROTOCOL)
        self.studentconfirmation()

    def studentconfirmation(self):
        reply = QtGui.QMessageBox()
        reply.setText("New Student Created.")
        reply.setIcon(0)
        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)

        ret = reply.exec_()
        self.close()

    def create_new_Teacher(self):
        newteacher = teacher(self.usernameBox.text(), "T", self.passwordBox.text(), self.forenameBox.text(),
                             self.surnameBox.text(), self.middlenameBox.text(), [])
        teachers.append(newteacher)
        with open('teachers.pickle', 'wb') as t:
            pickle.dump(teachers, t, pickle.HIGHEST_PROTOCOL)
        self.teacherconfirmation()

    def teacherconfirmation(self):
        reply = QtGui.QMessageBox()
        reply.setText("New Teacher Created.")
        reply.setIcon(0)
        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)

        ret = reply.exec_()
        self.close()


class Student_Main_Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 90, 91, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 130, 91, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 170, 91, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(294, 20, 91, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Logged in as " + username, None))
        self.pushButton.setText(_translate("Form", "Practice Q", None))
        self.pushButton_2.setText(_translate("Form", "See Set Work", None))
        self.pushButton_3.setText(_translate("Form", "Solve Questions", None))
        self.pushButton_4.setText(_translate("Form", "Log Out", None))
        self.pushButton.clicked.connect(self.launchPracticeQwindow)
        self.pushButton_4.clicked.connect(self.close)
        self.pushButton_4.clicked.connect(self.showLoginPage)
        self.pushButton_2.clicked.connect(self.showsetwork)
    def showsetwork(self):
        global workPage
        workPage = WorkList()
        workPage.show()
    def showLoginPage(self):
        myLogInPage = LogInPage()
        myLogInPage.exec_()

    def launchPracticeQwindow(self):
        global PracticeForm
        PracticeForm = Practice_Questions_Window()
        PracticeForm.show()
        
        
class WorkList(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(523, 516)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.QuestionLabel = QtGui.QLabel(Form)
        self.QuestionLabel.setObjectName(_fromUtf8("QuestionLabel"))
        self.verticalLayout.addWidget(self.QuestionLabel)
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.AttemptButton = QtGui.QPushButton(Form)
        self.AttemptButton.setObjectName(_fromUtf8("AttemptButton"))
        self.verticalLayout.addWidget(self.AttemptButton)
        self.CancelButton = QtGui.QPushButton(Form)
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))
        self.verticalLayout.addWidget(self.CancelButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.QuestionLabel.setText(_translate("Form", "Your Set Work:", None))
        self.AttemptButton.setText(_translate("Form", "Attempt", None))
        self.CancelButton.setText(_translate("Form", "Cancel", None))
        self.CancelButton.clicked.connect(self.close)
        self.populateQuestions()
        self.AttemptButton.clicked.connect(self.AttemptQ)
        
    def populateQuestions(self):
        n = 0
        global username
        self.shownList = []
        self.listWidget.clear()
        for people in students:
            if people.username == username:
                for question in people.questionstoanswer:
                    if question != None:
                       self.shownList.append(question)
                       self.listWidget.addItem(question.question_type + " : " + str(question.ID))
                       n = n + 1

            
    def AttemptQ(self):
        for item in self.listWidget.selectedIndexes():
            thisIndex = item.row()        
            if self.shownList[thisIndex].question_type == "Rate Constant":
                attemptQ = Practice_K_Window(self.shownList[thisIndex])
                attemptQ.exec_()
                self.populateQuestions()
            elif self.shownList[thisIndex].question_type == "Hardy-Weinberg":
                attemptQ = hardy_weinberg(self.shownList[thisIndex])
                attemptQ.exec_()
                self.populateQuestions()
                
                
                
                
                
class Practice_Questions_Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.hardyweinberg = QtGui.QPushButton(Form)
        self.hardyweinberg.setObjectName(_fromUtf8("hardyweinberg"))
        self.verticalLayout.addWidget(self.hardyweinberg)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout.addWidget(self.pushButton_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Logged in as " + username, None))
        self.pushButton.setText(_translate("Form", "Standard Deviation", None))
        self.pushButton_2.setText(_translate("Form", "Ideal Gas Equation", None))
        self.pushButton_3.setText(_translate("Form", "K Questions", None))
        self.hardyweinberg.setText(_translate("Form", "Hardy-Weinberg", None))
        self.label.setText(_translate("Form", "Practice Questions", None))
        self.pushButton_5.setText(_translate("Form", "Close", None))
        self.pushButton_3.clicked.connect(self.launchPracticeQWindow)
        self.pushButton_5.clicked.connect(self.close)
        self.hardyweinberg.clicked.connect(self.launch_hardy_weinberg)

    def launch_hardy_weinberg(self):
        global HWForm
        HWForm = hardy_weinberg()
        HWForm.show()

    def launchPracticeQWindow(self):
        global PracticeQuestion
        PracticeQuestion = Practice_K_Window()
        PracticeQuestion.show()


class MakeQSet(QtGui.QDialog):
    def __init__(self, QSet):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.shownList = self.populateQuestions(questions)
        self.newList = []

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(627, 447)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 30, 151, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(360, 60, 256, 341))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(442, 30, 161, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(360, 30, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 420, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.listWidget1 = QtGui.QListWidget(Form)
        self.listWidget1.setGeometry(QtCore.QRect(10, 60, 256, 341))
        self.listWidget1.setObjectName(_fromUtf8("listWidget1"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(272, 270, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 180, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "All Questions", None))
        self.label_2.setText(_translate("Form", "New Set:", None))
        self.pushButton_3.setText(_translate("Form", "Save", None))
        self.pushButton.setText(_translate("Form", "<", None))
        self.pushButton_2.setText(_translate("Form", ">", None))

        self.pushButton_2.clicked.connect(self.addQuestionToList)
        self.pushButton.clicked.connect(self.removeQuestion)
        self.pushButton_3.clicked.connect(self.makeNewSet)

    def removeQuestion(self):
        for item in self.listWidget.selectedIndexes():
            thisIndex = item.row()
            self.newList.pop(thisIndex)
            self.listWidget.takeItem(thisIndex)
        print("NewList now contains:")
        printQList(self.newList)

    def makeNewSet(self):
        if self.listWidget.count() != 0:
            if self.lineEdit.text() != "":
                    try:
                        ListID = len(QSets) + 1
                    except:
                        ListID = len(QSets.QList) + 1
                    newQSet = self.newList
                    name = self.lineEdit.text()
                    owner = username
                    newQSet = Question_Set(ListID, name, newQSet, owner)
                    QSets.append(newQSet)

                    with open('QSets.pickle', 'wb') as f:
                        pickle.dump(QSets, f, pickle.HIGHEST_PROTOCOL)
                    self.SetConfirmation()
            else:
                    reply = QtGui.QMessageBox()
                    reply.setText("Please enter a name.")
                    reply.setIcon(3)
                    reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)

                    ret = reply.exec_()
        else:
                reply = QtGui.QMessageBox()
                reply.setText('Please add questions to the set.')
                reply.setIcon(3)
                reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
                ret = reply.exec_()

    def SetConfirmation(self):

        reply = QtGui.QMessageBox()
        reply.setText("Question Set Created Successfully.")
        reply.setIcon(0)
        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)

        ret = reply.exec_()
        self.close()


    def addQuestionToList(self):
        for item in self.listWidget1.selectedIndexes():
            thisIndex = item.row()
            # add this question to the right hand list
            if not self.shownList[thisIndex] in self.newList:
                self.newList.append(self.shownList[thisIndex])
                self.listWidget.addItem(self.listWidget1.item(thisIndex).text())
        print("NewList now contains:")
        printQList(self.newList)

    def populateQuestions(self, questions):
        shownList = []
        for question in questions:
            shownList.append(question)
            self.listWidget1.addItem(str(question.ID) +"  :  " + question.question_type)
        return shownList


def printQList(qlist):
    for q in qlist:
        print(q.ID, " ", q.question_type)


class AddQuestion(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(718, 659)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.QuestiontypeBox = QtGui.QComboBox(Form)
        self.QuestiontypeBox.setObjectName(_fromUtf8("QuestiontypeBox"))
        self.QuestiontypeBox.addItem(_fromUtf8(""))
        self.QuestiontypeBox.addItem(_fromUtf8(""))
        self.QuestiontypeBox.addItem(_fromUtf8(""))
        self.QuestiontypeBox.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.QuestiontypeBox)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.firstValue = QtGui.QLineEdit(Form)
        self.firstValue.setObjectName(_fromUtf8("firstValue"))
        self.verticalLayout.addWidget(self.firstValue)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.secondValue = QtGui.QLineEdit(Form)
        self.secondValue.setObjectName(_fromUtf8("secondValue"))
        self.verticalLayout.addWidget(self.secondValue)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.thirdValue = QtGui.QLineEdit(Form)
        self.thirdValue.setObjectName(_fromUtf8("thirdValue"))
        self.verticalLayout.addWidget(self.thirdValue)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.FourthValue = QtGui.QLineEdit(Form)
        self.FourthValue.setObjectName(_fromUtf8("FourthValue"))
        self.verticalLayout.addWidget(self.FourthValue)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.FifthValue = QtGui.QLineEdit(Form)
        self.FifthValue.setObjectName(_fromUtf8("FifthValue"))
        self.verticalLayout.addWidget(self.FifthValue)
        self.Submit = QtGui.QPushButton(Form)
        self.Submit.setObjectName(_fromUtf8("Submit"))
        self.verticalLayout.addWidget(self.Submit)
        self.Cancel = QtGui.QPushButton(Form)
        self.Cancel.setObjectName(_fromUtf8("Cancel"))
        self.verticalLayout.addWidget(self.Cancel)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_6.setText(_translate("Form", "QuestionType:", None))
        self.QuestiontypeBox.setItemText(1, _translate("Form", " ", None))
        self.QuestiontypeBox.setItemText(1, _translate("Form", "Rate Constant", None))
        self.QuestiontypeBox.setItemText(2, _translate("Form", "Hardy-Weinberg", None))
        self.QuestiontypeBox.setItemText(3, _translate("Form", "Ideal Gas Equation", None))
        self.QuestiontypeBox.setItemText(4, _translate("Form", "Standard-Deviation", None))
        # self.label.setText(_translate("Form", "First Value:", None))
        # self.label_2.setText(_translate("Form", "Second Value:", None))
        #self.label_3.setText(_translate("Form", "Third Value:", None))
        #self.label_4.setText(_translate("Form", "Fourth Value:", None))
        #self.label_5.setText(_translate("Form", "Fifth Value", None))
        self.Submit.setText(_translate("Form", "Submit", None))
        self.Cancel.setText(_translate("Form", "Cancel", None))

        self.QuestiontypeBox.activated[str].connect(self.typechosen)
        self.Submit.clicked.connect(self.validate)
        self.clickedit = False
        self.Cancel.clicked.connect(self.close)

    def typechosen(self, text):
        self.clickedit = True
        self.questiontype = text
        if text == " ":
            self.typeNotSelected()

        if text == "Rate Constant":
            self.label.setText(_translate("Form", "Conc of A:", None))
            self.label_2.setText(_translate("Form", "Conc of B:", None))
            self.label_3.setText(_translate("Form", "Order of A:", None))
            self.thirdValue.setVisible(True)

            self.FourthValue.setVisible(True)
            self.FifthValue.setVisible(True)
            self.label_4.setText(_translate("Form", "Order of B:", None))
            self.label_5.setText(_translate("Form", "Rate of reaction", None))
        if text == "Hardy-Weinberg":
            self.label.setText(_translate("Form", "Total Population:", None))
            self.label_2.setText(_translate("Form", "No of Homozygotic Recessive:", None))
            self.label_3.setText(_translate("Form", "", None))
            self.thirdValue.setVisible(False)
            self.label_4.setText(_translate("Form", "", None))
            self.FourthValue.setVisible(False)
            self.label_5.setText(_translate("Form", "", None))
            self.FifthValue.setVisible(False)
        if text == "Ideal Gas Equation":
            self.label.setText(_translate("Form", "Pressure:", None))
            self.label_2.setText(_translate("Form", "Volume:", None))
            self.label_3.setText(_translate("Form", "No of Moles:", None))
            self.thirdValue.setVisible(True)
            self.label_4.setText(_translate("Form", "Temperature:", None))
            self.FourthValue.setVisible(True)
            self.label_5.setText(_translate("Form", " ", None))
            self.FifthValue.setVisible(False)
        print(self.questiontype)

    def validate(self, text):
        if self.clickedit == False or self.questiontype == "":
            self.typeNotSelected()

        else:
            valid = True
            text = self.questiontype

            if text == "Rate Constant":
                try:
                    FirstVal = float(self.firstValue.text())
                    SecondVal = float(self.secondValue.text())
                    ThirdVal = int(self.thirdValue.text())
                    FourthVal = int(self.FourthValue.text())
                    FifthVal = float(self.FifthValue.text())

                except:
                    reply = QtGui.QMessageBox()
                    reply.setText("Please enter numbers only.\nOrders must be integers.")
                    reply.setIcon(3)
                    reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)

                    
                    ret = reply.exec_()
                    valid = False
                if ThirdVal > 3:
                    reply = QtGui.QMessageBox()
                    reply.setText("Orders must be 1 or 2.")
                    reply.setIcon(3)
                    reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)


                    ret = reply.exec_()                    
                    valid = False
                if FourthVal > 3:
                    reply = QtGui.QMessageBox()
                    reply.setText("Orders must be 1 or 2.")
                    reply.setIcon(3)
                    reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)


                    ret = reply.exec_() 
                    valid = False
                try:
                        pow(FirstVal, ThirdVal) * (pow(SecondVal, FourthVal))

                except:
                        reply = QtGui.QMessageBox()
                        reply.setText("Please use smaller concentrations.")
                        reply.setIcon(3)
                        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)

                        ret = reply.exec_()
                        valid = False

            if text == "Hardy-Weinberg":
                try:

                    FirstVal = float(self.firstValue.text())
                    SecondVal = float(self.secondValue.text())
                    if SecondVal > FirstVal:
                        reply = QtGui.QMessageBox()
                        reply.setText("First Value must be larger than Second Value.")
                        reply.setIcon(3)
                        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)

                        ret = reply.exec_()
                        valid = False
                except:
                    self.fieldsIncorrect()
                    valid = False
            if valid == True:
                self.create()


    def create(self):
        QID = len(questions) + 1
        values = [convertTofloat(self.firstValue.text()), convertTofloat(self.secondValue.text()),
                  convertTofloat(self.thirdValue.text()), convertTofloat(self.FourthValue.text()),
                  convertTofloat(self.FifthValue.text())]
        print("Making A Question with", QID, self.questiontype, values)
        newQuestion = Question(QID, self.questiontype, values)
        questions.append(newQuestion)
        with open('questions.pickle', 'wb') as f:
            pickle.dump(questions, f, pickle.HIGHEST_PROTOCOL)
        self.questionconfirmation()
        for question in questions:
            try:
                print(question.ID, question.values)
            except:
                print("Nope")

    def questionconfirmation(self):
        reply = QtGui.QMessageBox()
        reply.setText("Question Added Successfully.")
        reply.setIcon(0)
        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)

        ret = reply.exec_()
        self.close()

    def fieldsIncorrect(self):
        reply = QtGui.QMessageBox()
        reply.setText("Some fields are not correct.")
        reply.setIcon(3)
        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)

        ret = reply.exec_()

    def typeNotSelected(self):
        reply = QtGui.QMessageBox()
        reply.setText("Question Type Field is not complete.")
        reply.setIcon(3)
        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)

        ret = reply.exec_()


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
        self.order_of_A = self.values[2]
        self.order_of_B = self.values[3]
        self.rateOfReaction = self.values[4]


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
                "%.2E" % self.conc_of_A) + " moldm^-3. The conc of B is " + str("%.2E" %self.conc_of_B) + " moldm^-3\n"
                                                                                "The order of A is " + str(
                self.order_of_A) + " and the order of B is " + str(self.order_of_B) + ". The rate of reaction is " + str(
                "%.2E" %self.rateOfReaction), None))
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


class Practice_K_Window(QtGui.QDialog):
    def __init__(self, values = None):
        QtGui.QDialog.__init__(self)
        self.setupUi(self, values)

    def setupUi(self, Form, values):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(728, 437)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 60, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(20, 50, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_2.addWidget(self.lineEdit)
        spacerItem2 = QtGui.QSpacerItem(20, 53, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setEnabled(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_2.addWidget(self.pushButton)
        spacerItem3 = QtGui.QSpacerItem(20, 72, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)

        self.retranslateUi(Form, values)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form, values):
        if values == None:
            self.thisQuestion = generateK()
        else:
            self.thisQuestion = values

        Form.setWindowTitle(_translate("Form", "Logged in as " + username, None))
        self.label.setText(_translate("Form", "Question Text Here", None))
        self.label_2.setText(_translate("Form", "Enter answer below to 3 sig fig in standard form replacing the ^ sign with an E. Specify plus or minus and use always usetwo numbers after the sign: 5.67E+01", None))
        self.pushButton.setText(_translate("Form", "Submit", None))
        self.pushButton.clicked.connect(self.checkAnswer)
        self.thisQuestion.findK(self)


    def checkAnswer(self):
        print('%.2E' % self.thisQuestion.k)
        self.answer = ('%.2E' % self.thisQuestion.k)
        self.wrongorright()

    def wrongorright(self):
        reply = QtGui.QMessageBox()
        if str(self.lineEdit.text()) == str(self.answer):
            reply.setText("That is correct.")
            reply.setIcon(0)
            reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)

            ret = reply.exec_()
            self.close()
            if self.thisQuestion != None:
                self.findStudent()              
        else:

                if str(self.lineEdit.text()) == str(self.answer+"0"):
                    
                        reply.setText("That is correct.")
                        reply.setIcon(0)
                        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
            
                        ret = reply.exec_()
                        self.close()
                else:
                        reply.setText("That is incorrect, try again.")
                        reply.setIcon(3)
                        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)  #
                        ret = reply.exec_()

    def findStudent(self):
                    global username
                    for people in students:
                                if people.username == username:
                                    people.questionAnswered(self.thisQuestion)

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
        try:
            self.questionstoanswer.remove(question)
            self.answered.append(question)
        except:
            with open('students.pickle', 'wb') as f:
            
                pickle.dump(students, f, pickle.HIGHEST_PROTOCOL)        

class hardy_weinberg(QtGui.QDialog):
    def __init__(self, thisQuestion= None):
        QtGui.QDialog.__init__(self)
        self.Question = thisQuestion
        self.setupUi(self)
        
        
    def setupUi(self, hardy_weinberg):
        hardy_weinberg.setObjectName(_fromUtf8("hardy_weinberg"))
        hardy_weinberg.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(hardy_weinberg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.questions_text = QtGui.QLabel(hardy_weinberg)
        self.questions_text.setObjectName(_fromUtf8("questions_text"))
        self.verticalLayout.addWidget(self.questions_text)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.answerBox = QtGui.QLineEdit(hardy_weinberg)
        self.answerBox.setObjectName(_fromUtf8("answerBox"))
        self.verticalLayout.addWidget(self.answerBox)
        self.SubmitAnswer = QtGui.QPushButton(hardy_weinberg)
        self.SubmitAnswer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SubmitAnswer.setObjectName(_fromUtf8("SubmitAnswer"))
        self.verticalLayout.addWidget(self.SubmitAnswer)

        self.retranslateUi(hardy_weinberg)
        QtCore.QMetaObject.connectSlotsByName(hardy_weinberg)
        
    def retranslateUi(self, hardy_weinberg):
        if self.Question == None:
            self.generate_H_W()
            
        if self.Question != None:
            self.recessiveInpop = self.Question.values[0]
            self.totalpop = self.Question.values[1]
            self.calculateAnswer()
            self.updateForm(hardy_weinberg)
            
    def findstudent(self):
        global username
        for people in students:
                    if people.username == username:
                        people.questionAnswered(self.Question)
    def updateForm(self, hardy_weinberg):
        self.setWindowTitle(_translate("hardy_weinberg", "hardy_weinberg", None))
        self.questions_text.setText(_translate("hardy_weinberg", "If " + str(self.q_sqrdaspop) + " out of " + str(
        self.totalpop) + " individuals in a population express the recessive phenotype, what percent of the population would you predict would be heterozygotes? ",
                                           None))
        self.SubmitAnswer.setText(_translate("hardy_weinberg", "Submit", None))
        self.SubmitAnswer.clicked.connect(self.checkAnswerpq)        

    def generate_H_W(self):

        
        self.totalpop = random.randint(10,1000)
        if self.totalpop % 2 == 0:
            self.percentageReccessive = random.randrange(0, 99, 2)
        else:
            self.percentageReccessive = random.randrange(1, 99, 2)
        self.calculateAnswerfromRand()
        self.updateForm(hardy_weinberg)
    def calculateAnswerfromRand(self):        
        percentageReccessive = self.percentageReccessive
        totalpop = self.totalpop
        recessiveInpop = ((totalpop * percentageReccessive) / 100)  # unrounded. Makes a percentage of the population have recessive alleles. 
        q_sqrdaspop = Round_To_n(recessiveInpop, 1)  # now rounded
        qsqrd = Round_To_n(q_sqrdaspop / totalpop, 3) # Finds q squared as a decimal.
        print("recessives", q_sqrdaspop)
        print("qsqrd", qsqrd)
        q = Round_To_n(math.sqrt(qsqrd), 3) # finds the number of reccessive alleles
        p = Round_To_n(1 - q, 3) #finds the number of dominant alleles
        psqrd = Round_To_n(p * p, 3) #finds the number of homozygous dominant
        print("psqrd", psqrd)
        pq = Round_To_n(p * q, 3) # finds heterozygotes
        print("p", p, "q", q)

        print("2pq", pq * 2)
        
        self.q_sqrdaspop = q_sqrdaspop
        self.qsqrd = qsqrd
        self.psqrd = psqrd
        self.q = q
        self.p = p
        self.pq = pq
    def calculateAnswer(self):
        totalpop = self.totalpop
        recessiveInpop = self.recessiveInpop
        q_sqrdaspop = Round_To_n(recessiveInpop, 1)  # now rounded
        qsqrd = Round_To_n(q_sqrdaspop / totalpop, 2) # Finds q squared as a decimal.
        print("recessives", q_sqrdaspop)
        print("qsqrd", qsqrd)
        q = Round_To_n(math.sqrt(qsqrd), 2) # finds the number of reccessive alleles
        p = Round_To_n(1 - q, 3) #finds the number of dominant alleles
        psqrd = Round_To_n(p * p, 3) #finds the number of homozygous dominant
        print("psqrd", psqrd)
        pq = Round_To_n(p * q, 3) # finds heterozygotes
        print("p", p, "q", q)

        print("2pq", pq * 2)
        
        self.q_sqrdaspop = q_sqrdaspop
        self.qsqrd = qsqrd
        self.psqrd = psqrd
        self.q = q
        self.p = p
        self.pq = pq        

    def checkAnswerpq(self):
        print(2 * self.pq)
        if self.answerBox.text() == str(2 * self.pq):
            reply = QtGui.QMessageBox()
            reply.setText("Correct.")
            reply.setIcon(0)
            reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
    
            ret = reply.exec_()
            self.close()
            if self.Question != None:
                self.findstudent() # finds the person who is logged in
            
        else:
            reply = QtGui.QMessageBox()
            reply.setText("Incorrect. Please try again.")
            reply.setIcon(3)
            reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
    
            ret = reply.exec_()
            
            


class findKreaction():
    def __init__(self, conc_of_A, conc_of_B, order_of_A, order_of_B, rateOfReaction):
        self.conc_of_A = conc_of_A
        self.conc_of_B = conc_of_B
        self.order_of_A = order_of_A
        self.order_of_B = order_of_B
        # self.rateNumber = rateNumber
        # self.rateExponent = rateExponent
        self.rateOfReaction = rateOfReaction
        self.noOfMoles = (order_of_A + order_of_B)


    def walk_throughK(self):
        print("To calculate the rate constant, k, we must first multiply the concentrations of our reactants together."
              "However the concentrations must be raised to the power of their orders."
              "The concentrations of A and B are", str("%.2E" % self.conc_of_A), "and", str("%.2E" % self.conc_of_B), "respectively."
                                                                                          "The order of A is",
              self.order_of_A, "and the order of B is ", self.order_of_B, " .")
        print("This means our intermediary value is ", str("%.2E" % self.intermediary), "."
                                                                          "We then divide our rate of reaction by this number. The reate of reaction is",
              str("%.2E" % self.rateOfReaction), ".")
        print("This equals", self.k)
        print("Next we must find the units of k \n")
        print("To find the units of k we must cancel the number of moles per dm cubed on both sides of the equation. "
              "\We do this by adding the powers of the two reactants and putting them into the formula: "
              "\nmol^-x dm^+x*3. Where x is the powers added together minus 1."
              "\nUnless the number of moles is one, then there are no units.\n ")
        if self.noOfMoles > 1:
            x = int((self.noOfMoles) - 1)

            print("The units are mol^-", x, "dm^+", 3 * x, "s^-1")
        else:
            print("No units")


    def findK(self, window):

        QtGui.QApplication.processEvents()
        n = 0
        self.intermediary = pow(self.conc_of_A, self.order_of_A) * (pow(self.conc_of_B, self.order_of_B))
        self.k = self.rateOfReaction / self.intermediary
        correct = False
        window.label.setText(_translate("Form", "The conc of reactant A is " + str("%.2E" %
            self.conc_of_A) + " moldm^-3. The conc of B is " + str("%.2E" % self.conc_of_B) + " moldm^-3\n"
                                                                                     "The order of A is " + str(
            self.order_of_A) + " and the order of B is " + str(self.order_of_B) + ". The rate of reaction is " + str(
           "%.2E" %  self.rateOfReaction) + "Find k of this reaction", None))





        # while correct == False:
        # k = self.k
        #k = ("%.3G" % (k))


        #studentAnswer = input("Enter in your value of k to 3 sig fig: ")
        #if studentAnswer == k:
        #correct = True
        #print("Well done, that was correct!")
        #another = input("Would you like to try again? y/n")
        #if another == "y":
        #print("  ")
        #loadQuestion()
        #if another == "n":
        #print("Goodbye!")
        #if studentAnswer != k:
        #n += 1
        #print("Sorry that's not right, try again.")
        #if n > 2:
        #walkthrough = input("Would you like a walk-through? y/n")
        #if walkthrough == "y":
        #print("  ")
        #findKreaction.walk_throughK(self)


    def findunitsofK(self):
        print("To find the units of k we must cancel the number of moles per dm cubed on both sides of the equation. "
              "\We do this by adding the powers of the two reactants and putting them into the formula: "
              "\nmol^-x dm^+x*3. Where x is the powers added together minus 1."
              "\nUnless the number of moles is one, then there are no units.\n ")
        if self.noOfMoles > 1:
            x = int((self.noOfMoles) - 1)

            print("The units are mol^-", x, "dm^+", 3 * x, "s^-1")
        else:
            print("No units")


            # def getRateOfReaction(self):
            # rateOfReaction = self.k*(pow(10,self.rateExponent))
            # return rateOfReaction


def generateK():
    sig = 3

    concofa = random.uniform(0.001, 0.9)
    concofA = Round_To_n(concofa, 3)
    concofb = random.uniform(0.001, 0.9)
    concofB = Round_To_n(concofb, 3)
    orderofA = random.randrange(1, 3)
    orderofB = random.randrange(1, 3)
    rate = random.uniform(0.00000001, 0.0009)
    rateofreaction = Round_To_n(rate, 3)
    y = findKreaction(concofA, concofB, orderofA, orderofB, rateofreaction)
    return y


def loadkQuestion():
    Q1 = findKreaction(0.4, 0.4, 2, 1, 0.00000585)
    Q2 = findKreaction(0.2, 0.3, 1, 2, 0.0000657)
    Q3 = findKreaction(0.2, 0.3, 1, 2, 0.0000257)
    Q4 = findKreaction(0.2, 0.3, 1, 2, 0.0000457)
    Q5 = findKreaction(0.2, 0.3, 1, 2, 0.0000127)
    Q6 = findKreaction(0.2, 0.3, 1, 2, 0.0100687)
    Q7 = findKreaction(0.2, 0.3, 1, 2, 0.0000757)
    Q8 = findKreaction(0.2, 0.3, 1, 2, 0.0000357)
    Q9 = findKreaction(0.2, 0.3, 1, 2, 0.0000257)
    Questions = [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9]
    x = random.randrange(9)
    y = Questions[x]
    return y


def format(number):
    number = "%.2E"%number
    return number
    

class LogInPage(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)


    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.UsernameBox = QtGui.QLineEdit(Form)
        self.UsernameBox.setObjectName(_fromUtf8("UsernameBox"))
        self.verticalLayout.addWidget(self.UsernameBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
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
        self.label.setText(_translate("Form", "Username:", None))
        self.label_2.setText(_translate("Form", "Password:", None))
        self.pushButton.setText(_translate("Form", "Log In", None))
        self.pushButton_2.setText(_translate("Form", "Cancel", None))
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.checkCredentials)


    def checkCredentials(self, Form):
        global username

        self.isStudent = False
        self.isTeacher = False
        for people in students:
            if self.UsernameBox.text() == people.username and self.PasswordBox.text() == people.password:
                if people.account_type == "S":
                    self.close()

                    username = people.username

                    global studentmainForm
                    studentmainForm = Student_Main_Window()
                    studentmainForm.show()
                    self.isStudent = True
        for people in teachers:
            if self.UsernameBox.text() == people.username and self.PasswordBox.text() == people.password:

                username = people.username

                if people.account_type == "T" or people.account_type == "A":
                    self.close()
                    global teacherMainForm
                    teacherMainForm = Teacher_Main_Window()
                    teacherMainForm.show()
                    self.isTeacher = True
        if self.isTeacher == False and self.isStudent == False:
            self.incorrectID()

    def incorrectID(self):
        reply = QtGui.QMessageBox()
        reply.setText("Your Username or Password is incorrect. Please try again.")
        reply.setIcon(0)
        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)

        ret = reply.exec_()
        reply.close()


def loadTeachers():
    global teachers
    with open('teachers.pickle', 'rb') as t:
        teachers = pickle.load(t)

        for people in teachers:
            print(people.username, people.password)


def loadStudents():
    global students
    with open('students.pickle', 'rb') as s:
        students = pickle.load(s)

        for people in students:
            # empty = []
            # people.questionstoanswer = empty
            print(people.username, people.password, people.studentid, people.questionstoanswer)
            # with open('students.pickle', 'wb') as f:
            # pickle.dump(students, f, pickle.HIGHEST_PROTOCOL)


def Round_To_n(x, n):
    return round(x, int(n - math.ceil(math.log10(abs(x)))))


class EditStudents(QtGui.QDialog):
    def __init__(self, values = None):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Delete Students"))
        Form.resize(769, 659)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.treeWidget = QtGui.QTreeWidget(Form)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.verticalLayout.addWidget(self.treeWidget)
        self.Delete = QtGui.QPushButton(Form)
        self.Delete.setObjectName(_fromUtf8("Delete"))
        self.verticalLayout.addWidget(self.Delete)
        self.Cancel = QtGui.QPushButton(Form)
        self.Cancel.setObjectName(_fromUtf8("Cancel"))
        self.verticalLayout.addWidget(self.Cancel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Delete Student Accounts", None))
        self.treeWidget.headerItem().setText(0, _translate("Form", "Student ID", None))
        self.treeWidget.headerItem().setText(1, _translate("Form", "Name", None))
        self.treeWidget.headerItem().setText(2, _translate("Form", "Username", None))
        self.treeWidget.headerItem().setText(3, _translate("Form", "Password", None))
        self.treeWidget.headerItem().setText(4, _translate("Form", "Form", None))
        self.Delete.setText(_translate("Form", "Delete", None))
        self.Cancel.setText(_translate("Form", "Cancel", None))
        self.Delete.clicked.connect(self.delete)
        self.Cancel.clicked.connect(self.close)
        self.populateTree()

    
    def delete(self):
        
        thisID = self.treeWidget.currentItem().text(0)
        print(thisID)
        for people in students:
            if str(people.studentid) == thisID:
                students.remove(people)
                print("removed", thisID)
                with open('students.pickle', 'wb') as f:
                    pickle.dump(students, f, pickle.HIGHEST_PROTOCOL)

                
        self.populateTree()
    
    def populateTree(self):
        self.treeWidget.clear()
        rowCount = -1
        global students
        for people in students:
            rowCount += 1
           
            QtGui.QTreeWidgetItem(self.treeWidget)
            self.treeWidget.topLevelItem(rowCount).setText(0, str(people.studentid))
            self.treeWidget.topLevelItem(rowCount).setText(1, people.forename)
            self.treeWidget.topLevelItem(rowCount).setText(2, people.username)
            self.treeWidget.topLevelItem(rowCount).setText(3, people.password)
            self.treeWidget.topLevelItem(rowCount).setText(4, people.form)
            
def convertTofloat(thing):
    try:
        thing = float(thing)
        return thing
    except:
        return 0.0


def loadQuestions():
    global questions
    with open('questions.pickle', 'rb') as q:
        questions = []
        questions = pickle.load(q)


def loadQSet():
    global QSets
    QSets = []
    with open('QSets.pickle', 'rb') as q:
        QSets = pickle.load(q)
        for n in range(len(QSets) - 1):
            print(QSets[n + 1].name)
            # print(QSets)

            # print(QSets[1].QList[1].values)


loadQuestions()
loadQSet()
loadStudents()
loadTeachers()
username = "Teacher"

app = QtGui.QApplication(sys.argv)
thisForm = Teacher_Main_Window()
thisForm.show()
sys.exit(app.exec_())

