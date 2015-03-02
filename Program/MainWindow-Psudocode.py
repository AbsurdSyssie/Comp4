__author__ <- 'Oscar'
import random, decimal, sys, pickle, math
from PyQt4 import QtCore, QtGui
from math import log10, floor
try:
    _fromUtf8 <- QtCore.QString.fromUtf8
except AttributeError:
    FUNCTION _fromUtf8(s):
        RETURN s
    ENDFUNCTION

try:
    _encoding <- QtGui.QApplication.UnicodeUTF8
    FUNCTION _translate(context, text, disambig):
        RETURN QtGui.QApplication.translate(context, text, disambig, _encoding)
    ENDFUNCTION

except AttributeError:
    FUNCTION _translate(context, text, disambig):
        RETURN QtGui.QApplication.translate(context, text, disambig)
    ENDFUNCTION

# start of main
# students <- []
teachers <- []
CLASS teacher():
    FUNCTION __init__(self, username, account_type, password, forename, surname, middlename, pupils):
                                                         ENDFOR
         account_type <- account_type
         username <- username
         forename <- forename
             ENDFOR
         password <- password
         surname <- surname
         middlename <- middlename
         pupils <- pupils
    ENDFUNCTION

ENDCLASS

CLASS Teacher_Main_Window(QtGui.QWidget):
    FUNCTION __init__(self):
        QtGui.QWidget.__init__(self)
         setupUi(self)
    ENDFUNCTION

    FUNCTION setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 324)
         verticalLayout <- QtGui.QVBoxLayout(Form)
         verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
         pushButton_3 <- QtGui.QPushButton(Form)
         pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
         verticalLayout.addWidget( pushButton_3)
        spacerItem <- QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
         verticalLayout.addItem(spacerItem)
         pushButton_2 <- QtGui.QPushButton(Form)
         pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
         verticalLayout.addWidget( pushButton_2)
        spacerItem1 <- QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        spacerItem5 <- QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
         verticalLayout.addItem(spacerItem5)
         pushButton_6 <- QtGui.QPushButton(Form)
         pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
         verticalLayout.addWidget( pushButton_6)
         verticalLayout.addItem(spacerItem1)
         pushButton <- QtGui.QPushButton(Form)
         pushButton.setObjectName(_fromUtf8("pushButton"))
         verticalLayout.addWidget( pushButton)
        spacerItem2 <- QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
         verticalLayout.addItem(spacerItem2)
         pushButton_4 <- QtGui.QPushButton(Form)
         pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
         verticalLayout.addWidget( pushButton_4)
        spacerItem3 <- QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
         verticalLayout.addItem(spacerItem3)
         editAcc <- QtGui.QPushButton(Form)
         editAcc.setObjectName(_fromUtf8("editAcc"))
         verticalLayout.addWidget( editAcc)
        spacerItem4 <- QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
         verticalLayout.addItem(spacerItem4)
         pushButton_5 <- QtGui.QPushButton(Form)
         pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
         verticalLayout.addWidget( pushButton_5)
         retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    ENDFUNCTION

    FUNCTION retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Logged in as " + username, None))
         pushButton_3.setText(_translate("Form", "Set Questions", None))
         pushButton_2.setText(_translate("Form", "Add Questions", None))
         pushButton.setText(_translate("Form", "See Student Progress", None))
         pushButton_4.setText(_translate("Form", "Add New Account", None))
         editAcc.setText(_translate("Form", "Edit Accounts", None))
         pushButton_6.setText(_translate("Form", "Make QSet", None))
         pushButton_5.setText(_translate("Form", "Log Out", None))
         pushButton_4.clicked.connect( showCreateNewAccountWindow)
         pushButton_5.clicked.connect( close)
         pushButton_5.clicked.connect( showLoginPage)
         pushButton_2.clicked.connect( showNewq)
         pushButton_3.clicked.connect( showSetQuestions)
         pushButton_6.clicked.connect( makeQSet)
         editAcc.clicked.connect( openEditStudents)
    ENDFUNCTION

    FUNCTION openEditStudents(self):
        editac <- EditStudents()
        editac.exec_()
    ENDFUNCTION

    FUNCTION makeQSet(self):
        myMakeQSet <- MakeQSet(QSets)
        myMakeQSet.exec_()
    ENDFUNCTION

    FUNCTION showSetQuestions(self):
        Setquestions <- SetQuestions()
        Setquestions.exec_()
    ENDFUNCTION

    FUNCTION showLoginPage(self):
        myLogInPage <- LogInPage()
        myLogInPage.exec_()
    ENDFUNCTION

    FUNCTION showCreateNewAccountWindow(self):
        global newAccountForm
        newAccountForm <- createaccount()
        newAccountForm.show()
    ENDFUNCTION

    FUNCTION showNewq(self):
        global newQForm
        newQForm <- AddQuestion()
        newQForm.show()
    ENDFUNCTION

ENDCLASS

CLASS SetQuestions(QtGui.QDialog):
    FUNCTION __init__(self):
        QtGui.QDialog.__init__(self)
         setupUi(self)
    ENDFUNCTION

    FUNCTION setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(682, 593)
         verticalLayout <- QtGui.QVBoxLayout(Form)
         verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
         verticalLayout_2 <- QtGui.QVBoxLayout()
         verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
         label <- QtGui.QLabel(Form)
         label.setObjectName(_fromUtf8("label"))
         verticalLayout_2.addWidget( label)
         FormBox <- QtGui.QComboBox(Form)
         FormBox.setObjectName(_fromUtf8("FormBox"))
         FormBox.addItem(_fromUtf8(""))
         verticalLayout_2.addWidget( FormBox)
         StudentBox <- QtGui.QComboBox(Form)
         StudentBox.setObjectName(_fromUtf8("StudentBox"))
         verticalLayout_2.addWidget( StudentBox)
        spacerItem <- QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
         verticalLayout_2.addItem(spacerItem)
         label_2 <- QtGui.QLabel(Form)
         label_2.setObjectName(_fromUtf8("label_2"))
         verticalLayout_2.addWidget( label_2)
         QuestionSetBox <- QtGui.QComboBox(Form)
         QuestionSetBox.setObjectName(_fromUtf8("QuestionSetBox"))
         verticalLayout_2.addWidget( QuestionSetBox)
         verticalLayout.addLayout( verticalLayout_2)
         SubmitButton <- QtGui.QPushButton(Form)
         SubmitButton.setObjectName(_fromUtf8("SubmitButton"))
         verticalLayout.addWidget( SubmitButton)
         retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    ENDFUNCTION

    FUNCTION retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
         label.setText(_translate("Form", "Select Student:", None))
         FormBox.setItemText(0, _translate("Form", "", None))
         label_2.setText(_translate("Form", "Select Question Set:", None))
         SubmitButton.setText(_translate("Form", "Submit", None))
         populateQSets
         FormBox.activated[str].connect( populatepupils)
         populateforms()
                     ENDFOR
         populateQSets()
         SubmitButton.clicked.connect( giveQuestions)
         SubmitButton.clicked.connect( checks)
    ENDFUNCTION

    FUNCTION checks(self):
        IF  StudentBox.currentText() = "":
                reply <- QtGui.QMessageBox()
                reply.setText("Please Select a Student.")
                reply.setIcon(3)
                reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
                ret <- reply.exec_()
        ENDIF
        IF  QuestionSetBox.currentText() = "":    
            reply <- QtGui.QMessageBox()
            reply.setText("Please Select a Question Set.")
            reply.setIcon(3)
            reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
            ret <- reply.exec_()
        ENDIF
    ENDFUNCTION

    FUNCTION populateforms(self):
                ENDFOR
        AllItems <- []
        for people in students:
            IF not people.form in AllItems:
                          ENDFOR
                 FormBox.addItem(people.form)
                                            ENDFOR
                AllItems.append(people.form)
            ENDIF
    ENDFUNCTION

        ENDFOR
                                       ENDFOR
    FUNCTION populatepupils(self, text):
        IF text != "":
             StudentBox.clear()
             StudentBox.addItem("All")
            for people in students:
                IF people.form = text:
                          ENDFOR
                     StudentBox.addItem(people.username)
                ENDIF
            ENDFOR
        ELSE:
                     StudentBox.clear()
        ENDIF
    ENDFUNCTION

    FUNCTION populateQSets(self):
        AllItems <- []
        for n in range(len(QSets) - 1):
            IF not QSets[n + 1].name in AllItems:
                 QuestionSetBox.addItem(QSets[n + 1].name)
                AllItems.append(QSets[n + 1].name)
            ENDIF
    ENDFUNCTION

        ENDFOR
    FUNCTION giveQuestions(self):
        IF  StudentBox.currentText() = "All":
            OUTPUT "hi all"
            for people in students:
                IF people.form =  FormBox.currentText():
                          ENDFOR
                    OUTPUT "hi again"
                    for question in QSets[ QuestionSetBox.currentIndex()+1].QList:
                        IF question not in people.questionstoanswer:
                            people.questionstoanswer.append(question)
                            OUTPUT "Adding"
                        ENDIF
                        with open('students.pickle', 'wb') as f:
                            pickle.dump(students, f, pickle.HIGHEST_PROTOCOL)
                ENDIF
            ENDFOR
                    ENDFOR
        ELSE:
            for people in students:
                IF people.username =  StudentBox.currentText():
                    OUTPUT "hi"
                    IF not  QuestionSetBox.currentText() in people.questionstoanswer:
                        OUTPUT "Adding"
                        for question in QSets[ QuestionSetBox.currentIndex()+1].QList:
                            people.questionstoanswer.append(question)
                        ENDFOR
                        with open('students.pickle', 'wb') as f:
                            pickle.dump(students, f, pickle.HIGHEST_PROTOCOL)
        ENDIF
                ENDIF
                    ENDIF
    ENDFUNCTION

ENDCLASS

            ENDFOR
CLASS createaccount(QtGui.QWidget):
    FUNCTION __init__(self):
        QtGui.QWidget.__init__(self)
         setupUi(self)
    ENDFUNCTION

    FUNCTION setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(606, 632)
         verticalLayout <- QtGui.QVBoxLayout(Form)
         verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
         scrollArea <- QtGui.QScrollArea(Form)
         scrollArea.setWidgetResizable(True)
         scrollArea.setObjectName(_fromUtf8("scrollArea"))
         scrollAreaWidgetContents <- QtGui.QWidget()
         scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 586, 612))
         scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
         verticalLayout_2 <- QtGui.QVBoxLayout( scrollAreaWidgetContents)
         verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
         label_8 <- QtGui.QLabel( scrollAreaWidgetContents)
        font <- QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
         label_8.setFont(font)
         label_8.setAlignment(QtCore.Qt.AlignCenter)
         label_8.setObjectName(_fromUtf8("label_8"))
         verticalLayout_2.addWidget( label_8)
         teacherCheck <- QtGui.QRadioButton( scrollAreaWidgetContents)
         teacherCheck.setObjectName(_fromUtf8("teacherCheck"))
         verticalLayout_2.addWidget( teacherCheck)
         studentCheck <- QtGui.QRadioButton( scrollAreaWidgetContents)
         studentCheck.setObjectName(_fromUtf8("studentCheck"))
         verticalLayout_2.addWidget( studentCheck)
         label <- QtGui.QLabel( scrollAreaWidgetContents)
         label.setObjectName(_fromUtf8("label"))
         verticalLayout_2.addWidget( label)
         forenameBox <- QtGui.QLineEdit( scrollAreaWidgetContents)
             ENDFOR
         forenameBox.setObjectName(_fromUtf8("forenameBox"))
             ENDFOR
         verticalLayout_2.addWidget( forenameBox)
                                             ENDFOR
         label_2 <- QtGui.QLabel( scrollAreaWidgetContents)
         label_2.setObjectName(_fromUtf8("label_2"))
         verticalLayout_2.addWidget( label_2)
         middlenameBox <- QtGui.QLineEdit( scrollAreaWidgetContents)
         middlenameBox.setObjectName(_fromUtf8("middlenameBox"))
         verticalLayout_2.addWidget( middlenameBox)
         label_4 <- QtGui.QLabel( scrollAreaWidgetContents)
         label_4.setObjectName(_fromUtf8("label_4"))
         verticalLayout_2.addWidget( label_4)
         surnameBox <- QtGui.QLineEdit( scrollAreaWidgetContents)
         surnameBox.setObjectName(_fromUtf8("surnameBox"))
         verticalLayout_2.addWidget( surnameBox)
         label_3 <- QtGui.QLabel( scrollAreaWidgetContents)
         label_3.setObjectName(_fromUtf8("label_3"))
         verticalLayout_2.addWidget( label_3)
         passwordBox <- QtGui.QLineEdit( scrollAreaWidgetContents)
         passwordBox.setObjectName(_fromUtf8("passwordBox"))
         verticalLayout_2.addWidget( passwordBox)
         label_5 <- QtGui.QLabel( scrollAreaWidgetContents)
         label_5.setObjectName(_fromUtf8("label_5"))
         verticalLayout_2.addWidget( label_5)
         usernameBox <- QtGui.QLineEdit( scrollAreaWidgetContents)
         usernameBox.setObjectName(_fromUtf8("usernameBox"))
         verticalLayout_2.addWidget( usernameBox)
         label_6 <- QtGui.QLabel( scrollAreaWidgetContents)
         label_6.setObjectName(_fromUtf8("label_6"))
         verticalLayout_2.addWidget( label_6)
         formBox <- QtGui.QLineEdit( scrollAreaWidgetContents)
             ENDFOR
         formBox.setObjectName(_fromUtf8("formBox"))
             ENDFOR
         verticalLayout_2.addWidget( formBox)
                                             ENDFOR
         label_7 <- QtGui.QLabel( scrollAreaWidgetContents)
         label_7.setObjectName(_fromUtf8("label_7"))
         verticalLayout_2.addWidget( label_7)
         gradeBox <- QtGui.QLineEdit( scrollAreaWidgetContents)
         gradeBox.setObjectName(_fromUtf8("gradeBox"))
         verticalLayout_2.addWidget( gradeBox)
         submitButton <- QtGui.QPushButton( scrollAreaWidgetContents)
         submitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
         submitButton.setObjectName(_fromUtf8("submitButton"))
         verticalLayout_2.addWidget( submitButton)
         cancelButton <- QtGui.QPushButton( scrollAreaWidgetContents)
         cancelButton.setObjectName(_fromUtf8("cancelButton"))
         verticalLayout_2.addWidget( cancelButton)
         scrollArea.setWidget( scrollAreaWidgetContents)
         verticalLayout.addWidget( scrollArea)
         retranslateUi(Form)
        QtCore.QObject.connect( teacherCheck, QtCore.SIGNAL(_fromUtf8("clicked()")),  label_6.hide)
        QtCore.QObject.connect( teacherCheck, QtCore.SIGNAL(_fromUtf8("clicked()")),  formBox.hide)
                                                                                              ENDFOR
        QtCore.QObject.connect( teacherCheck, QtCore.SIGNAL(_fromUtf8("clicked()")),  label_7.hide)
        QtCore.QObject.connect( teacherCheck, QtCore.SIGNAL(_fromUtf8("clicked()")),  gradeBox.hide)
        QtCore.QObject.connect( studentCheck, QtCore.SIGNAL(_fromUtf8("clicked()")),  label_6.show)
        QtCore.QObject.connect( studentCheck, QtCore.SIGNAL(_fromUtf8("clicked()")),  formBox.show)
                                                                                              ENDFOR
        QtCore.QObject.connect( studentCheck, QtCore.SIGNAL(_fromUtf8("clicked()")),  label_7.show)
        QtCore.QObject.connect( studentCheck, QtCore.SIGNAL(_fromUtf8("clicked()")),  gradeBox.show)
        QtCore.QObject.connect( cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)
    ENDFUNCTION

    FUNCTION retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Logged in as " + username, None))
         label_8.setText(_translate("Form", "Create Account", None))
         teacherCheck.setText(_translate("Form", "Teacher", None))
         studentCheck.setText(_translate("Form", "Student", None))
         label.setText(_translate("Form", " First Name:", None))
         label_2.setText(_translate("Form", "Middle Name(IF applicable):", None))
                                                             ENDIF
         label_4.setText(_translate("Form", "Surname:", None))
         label_3.setText(_translate("Form", "Password:", None))
         label_5.setText(_translate("Form", "Username:", None))
         label_6.setText(_translate("Form", "Form:", None))
         label_7.setText(_translate("Form", "Target Grade:", None))
         submitButton.setText(_translate("Form", "Submit", None))
         cancelButton.setText(_translate("Form", "Cancel", None))
         submitButton.clicked.connect( checktype)
    ENDFUNCTION

    FUNCTION checktype(self):
        valid <- True
        IF (not  studentCheck) AND (not  teacherCheck):
             fieldsNotComplete()
        ENDIF
        IF  studentCheck.isChecked() = True:
            for people in teachers:
                IF  usernameBox.text() = people.username:
                     usernameinuse()
                    valid <- False            
                ENDIF
            ENDFOR
            for people in students:
                IF  usernameBox.text() = people.username:
                     usernameinuse()
                    valid <- False
                ENDIF
            ENDFOR
            IF  gradeBox.text() = "" OR  formBox.text() = "" or  surnameBox.text() = "" or  forenameBox.text() = "" or  passwordBox.text() = "" or self.usernameBox.text() = "":
                                                  ENDFOR
                 fieldsNotComplete()
                valid <- False
            ENDIF
            IF valid = True:
                 create_new_Student()
                 close()
        ENDIF
            ENDIF
        IF  teacherCheck.isChecked() = True:
                for people in teachers:
                    IF  usernameBox.text() = people.username:
                         usernameinuse()
                        valid <- False
                    ENDIF
                ENDFOR
                for people in students:
                    IF  usernameBox.text() = people.username:
                         usernameinuse()
                        valid <- False                    
                    ENDIF
                ENDFOR
                IF  surnameBox.text() = "" OR  forenameBox.text() = "" or  passwordBox.text() = "" or  usernameBox.text() = "":
                                                        ENDFOR
                             fieldsNotComplete()
                            valid <- False
                ENDIF
                IF valid = True:
                         create_new_Teacher()
        ENDIF
                ENDIF
    ENDFUNCTION

    FUNCTION usernameinuse(self):
        reply <- QtGui.QMessageBox()
        reply.setText("That username is already in use.")
        reply.setIcon(3)
        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
        ret <- reply.exec_()
    ENDFUNCTION

    FUNCTION fieldsNotComplete(self):
        reply <- QtGui.QMessageBox()
        reply.setText("Some fields are not complete.")
        reply.setIcon(3)
        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
        ret <- reply.exec_()
    ENDFUNCTION

    FUNCTION create_new_Student(self):
        student_id <- len(students) + 1
        newstudent <- student(student_id,  usernameBox.text(), "S",  passwordBox.text(),  forenameBox.text(),
                                                                                                     ENDFOR
                              surnameBox.text(),  middlenameBox.text(),  formBox.text(),
                                                                                     ENDFOR
                              gradeBox.text(), [], [], [])
        students.append(newstudent)
        with open('students.pickle', 'wb') as f:
            pickle.dump(students, f, pickle.HIGHEST_PROTOCOL)
         studentconfirmation()
    ENDFUNCTION

    FUNCTION studentconfirmation(self):
        reply <- QtGui.QMessageBox()
        reply.setText("New Student Created.")
        reply.setIcon(0)
        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
        ret <- reply.exec_()
         close()
    ENDFUNCTION

    FUNCTION create_new_Teacher(self):
        newteacher <- teacher( usernameBox.text(), "T",  passwordBox.text(),  forenameBox.text(),
                                                                                         ENDFOR
                              surnameBox.text(),  middlenameBox.text(), [])
        teachers.append(newteacher)
        with open('teachers.pickle', 'wb') as t:
            pickle.dump(teachers, t, pickle.HIGHEST_PROTOCOL)
         teacherconfirmation()
    ENDFUNCTION

    FUNCTION teacherconfirmation(self):
        reply <- QtGui.QMessageBox()
        reply.setText("New Teacher Created.")
        reply.setIcon(0)
        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
        ret <- reply.exec_()
         close()
    ENDFUNCTION

ENDCLASS

CLASS Student_Main_Window(QtGui.QWidget):
    FUNCTION __init__(self):
        QtGui.QWidget.__init__(self)
         setupUi(self)
    ENDFUNCTION

    FUNCTION setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
         pushButton <- QtGui.QPushButton(Form)
         pushButton.setGeometry(QtCore.QRect(150, 90, 91, 23))
         pushButton.setObjectName(_fromUtf8("pushButton"))
         pushButton_2 <- QtGui.QPushButton(Form)
         pushButton_2.setGeometry(QtCore.QRect(150, 130, 91, 23))
         pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
         pushButton_3 <- QtGui.QPushButton(Form)
         pushButton_3.setGeometry(QtCore.QRect(150, 170, 91, 23))
         pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
         pushButton_4 <- QtGui.QPushButton(Form)
         pushButton_4.setGeometry(QtCore.QRect(294, 20, 91, 23))
         pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
         retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    ENDFUNCTION

    FUNCTION retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Logged in as " + username, None))
         pushButton.setText(_translate("Form", "Practice Q", None))
         pushButton_2.setText(_translate("Form", "See Set Work", None))
         pushButton_3.setText(_translate("Form", "Solve Questions", None))
         pushButton_4.setText(_translate("Form", "Log Out", None))
         pushButton.clicked.connect( launchPracticeQwindow)
         pushButton_4.clicked.connect( close)
         pushButton_4.clicked.connect( showLoginPage)
         pushButton_2.clicked.connect( showsetwork)
    ENDFUNCTION

    FUNCTION showsetwork(self):
        global workPage
        workPage <- WorkList()
        workPage.show()
    ENDFUNCTION

    FUNCTION showLoginPage(self):
        myLogInPage <- LogInPage()
        myLogInPage.exec_()
    ENDFUNCTION

    FUNCTION launchPracticeQwindow(self):
        global PracticeForm
        PracticeForm <- Practice_Questions_Window()
        PracticeForm.show()
    ENDFUNCTION

ENDCLASS

CLASS WorkList(QtGui.QWidget):
    FUNCTION __init__(self):
        QtGui.QWidget.__init__(self)
         setupUi(self)
    ENDFUNCTION

    FUNCTION setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(523, 516)
         verticalLayout <- QtGui.QVBoxLayout(Form)
         verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
         QuestionLabel <- QtGui.QLabel(Form)
         QuestionLabel.setObjectName(_fromUtf8("QuestionLabel"))
         verticalLayout.addWidget( QuestionLabel)
         listWidget <- QtGui.QListWidget(Form)
         listWidget.setObjectName(_fromUtf8("listWidget"))
         verticalLayout.addWidget( listWidget)
         AttemptButton <- QtGui.QPushButton(Form)
         AttemptButton.setObjectName(_fromUtf8("AttemptButton"))
         verticalLayout.addWidget( AttemptButton)
         CancelButton <- QtGui.QPushButton(Form)
         CancelButton.setObjectName(_fromUtf8("CancelButton"))
         verticalLayout.addWidget( CancelButton)
         retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    ENDFUNCTION

    FUNCTION retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
         QuestionLabel.setText(_translate("Form", "Your Set Work:", None))
         AttemptButton.setText(_translate("Form", "Attempt", None))
         CancelButton.setText(_translate("Form", "Cancel", None))
         CancelButton.clicked.connect( close)
         populateQuestions()
         AttemptButton.clicked.connect( AttemptQ)
    ENDFUNCTION

    FUNCTION populateQuestions(self):
        n <- 0
        global username
         shownList <- []
         listWidget.clear()
        for people in students:
            IF people.username = username:
                for question in people.questionstoanswer:
                    IF question != None:
                        shownList.append(question)
                        listWidget.addItem(question.question_type + " : " + str(question.ID))
                       n <- n + 1
            ENDIF
                    ENDIF
    ENDFUNCTION

        ENDFOR
                ENDFOR
    FUNCTION AttemptQ(self):
        for item in  listWidget.selectedIndexes():
            thisIndex <- item.row()        
            IF  shownList[thisIndex].question_type = "Rate Constant":
                attemptQ <- Practice_K_Window( shownList[thisIndex])
                attemptQ.exec_()
                 populateQuestions()
            ELSEIF  shownList[thisIndex].question_type = "Hardy-Weinberg":
                attemptQ <- hardy_weinberg( shownList[thisIndex])
                attemptQ.exec_()
                 populateQuestions()
            ENDIF
    ENDFUNCTION

ENDCLASS

        ENDFOR
CLASS Practice_Questions_Window(QtGui.QWidget):
    FUNCTION __init__(self):
        QtGui.QWidget.__init__(self)
         setupUi(self)
    ENDFUNCTION

    FUNCTION setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
         verticalLayout <- QtGui.QVBoxLayout(Form)
         verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
         label <- QtGui.QLabel(Form)
         label.setAlignment(QtCore.Qt.AlignCenter)
         label.setObjectName(_fromUtf8("label"))
         verticalLayout.addWidget( label)
         pushButton_3 <- QtGui.QPushButton(Form)
         pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
         verticalLayout.addWidget( pushButton_3)
        spacerItem <- QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
         verticalLayout.addItem(spacerItem)
         pushButton <- QtGui.QPushButton(Form)
         pushButton.setObjectName(_fromUtf8("pushButton"))
         verticalLayout.addWidget( pushButton)
        spacerItem1 <- QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
         verticalLayout.addItem(spacerItem1)
         pushButton_2 <- QtGui.QPushButton(Form)
         pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
         verticalLayout.addWidget( pushButton_2)
        spacerItem2 <- QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
         verticalLayout.addItem(spacerItem2)
         hardyweinberg <- QtGui.QPushButton(Form)
         hardyweinberg.setObjectName(_fromUtf8("hardyweinberg"))
         verticalLayout.addWidget( hardyweinberg)
        spacerItem3 <- QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
         verticalLayout.addItem(spacerItem3)
         pushButton_5 <- QtGui.QPushButton(Form)
         pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
         verticalLayout.addWidget( pushButton_5)
         retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    ENDFUNCTION

    FUNCTION retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Logged in as " + username, None))
         pushButton.setText(_translate("Form", "Standard Deviation", None))
         pushButton_2.setText(_translate("Form", "Ideal Gas Equation", None))
         pushButton_3.setText(_translate("Form", "K Questions", None))
         hardyweinberg.setText(_translate("Form", "Hardy-Weinberg", None))
         label.setText(_translate("Form", "Practice Questions", None))
         pushButton_5.setText(_translate("Form", "Close", None))
         pushButton_3.clicked.connect( launchPracticeQWindow)
         pushButton_5.clicked.connect( close)
         hardyweinberg.clicked.connect( launch_hardy_weinberg)
    ENDFUNCTION

    FUNCTION launch_hardy_weinberg(self):
        global HWForm
        HWForm <- hardy_weinberg()
        HWForm.show()
    ENDFUNCTION

    FUNCTION launchPracticeQWindow(self):
        global PracticeQuestion
        PracticeQuestion <- Practice_K_Window()
        PracticeQuestion.show()
    ENDFUNCTION

ENDCLASS

CLASS MakeQSet(QtGui.QDialog):
    FUNCTION __init__(self, QSet):
        QtGui.QDialog.__init__(self)
         setupUi(self)
         shownList <-  populateQuestions(questions)
         newList <- []
    ENDFUNCTION

    FUNCTION setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(627, 447)
         label <- QtGui.QLabel(Form)
         label.setGeometry(QtCore.QRect(10, 30, 151, 16))
         label.setObjectName(_fromUtf8("label"))
         listWidget <- QtGui.QListWidget(Form)
         listWidget.setGeometry(QtCore.QRect(360, 60, 256, 341))
         listWidget.setObjectName(_fromUtf8("listWidget"))
         lineEdit <- QtGui.QLineEdit(Form)
         lineEdit.setGeometry(QtCore.QRect(442, 30, 161, 20))
         lineEdit.setObjectName(_fromUtf8("lineEdit"))
         label_2 <- QtGui.QLabel(Form)
         label_2.setGeometry(QtCore.QRect(360, 30, 71, 16))
         label_2.setObjectName(_fromUtf8("label_2"))
         pushButton_3 <- QtGui.QPushButton(Form)
         pushButton_3.setGeometry(QtCore.QRect(480, 420, 75, 23))
         pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
         listWidget1 <- QtGui.QListWidget(Form)
         listWidget1.setGeometry(QtCore.QRect(10, 60, 256, 341))
         listWidget1.setObjectName(_fromUtf8("listWidget1"))
         pushButton <- QtGui.QPushButton(Form)
         pushButton.setGeometry(QtCore.QRect(272, 270, 75, 23))
         pushButton.setObjectName(_fromUtf8("pushButton"))
         pushButton_2 <- QtGui.QPushButton(Form)
         pushButton_2.setGeometry(QtCore.QRect(270, 180, 75, 23))
         pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
         retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    ENDFUNCTION

    FUNCTION retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
         label.setText(_translate("Form", "All Questions", None))
         label_2.setText(_translate("Form", "New Set:", None))
         pushButton_3.setText(_translate("Form", "Save", None))
         pushButton.setText(_translate("Form", "<", None))
         pushButton_2.setText(_translate("Form", ">", None))
         pushButton_2.clicked.connect( addQuestionToList)
         pushButton.clicked.connect( removeQuestion)
         pushButton_3.clicked.connect( makeNewSet)
    ENDFUNCTION

    FUNCTION removeQuestion(self):
        for item in  listWidget.selectedIndexes():
            thisIndex <- item.row()
             newList.pop(thisIndex)
             listWidget.takeItem(thisIndex)
        ENDFOR
        OUTPUT "NewList now contains:"
        printQList( newList)
    ENDFUNCTION

    FUNCTION makeNewSet(self):
        IF  listWidget.count() != 0:
            IF  lineEdit.text() != "":
                    try:
                        ListID <- len(QSets) + 1
                    except:
                        ListID <- len(QSets.QList) + 1
                    newQSet <-  newList
                    name <-  lineEdit.text()
                    owner <- username
                    newQSet <- Question_Set(ListID, name, newQSet, owner)
                    QSets.append(newQSet)
                    with open('QSets.pickle', 'wb') as f:
                        pickle.dump(QSets, f, pickle.HIGHEST_PROTOCOL)
                     SetConfirmation()
            ELSE:
                    reply <- QtGui.QMessageBox()
                    reply.setText("Please enter a name.")
                    reply.setIcon(3)
                    reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
                    ret <- reply.exec_()
            ENDIF
        ELSE:
                reply <- QtGui.QMessageBox()
                reply.setText('Please add questions to the set.')
                reply.setIcon(3)
                reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
                ret <- reply.exec_()
        ENDIF
    ENDFUNCTION

    FUNCTION SetConfirmation(self):
        reply <- QtGui.QMessageBox()
        reply.setText("Question Set Created Successfully.")
        reply.setIcon(0)
        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
        ret <- reply.exec_()
         close()
    ENDFUNCTION

    FUNCTION addQuestionToList(self):
        for item in  listWidget1.selectedIndexes():
            thisIndex <- item.row()
            # add this question to the right hand list
            IF not  shownList[thisIndex] in  newList:
                 newList.append( shownList[thisIndex])
                 listWidget.addItem( listWidget1.item(thisIndex).text())
            ENDIF
        ENDFOR
        OUTPUT "NewList now contains:"
        printQList( newList)
    ENDFUNCTION

    FUNCTION populateQuestions(self, questions):
        shownList <- []
        for question in questions:
            shownList.append(question)
             listWidget1.addItem(str(question.ID) +"  :  " + question.question_type)
        ENDFOR
        RETURN shownList
    ENDFUNCTION

ENDCLASS

FUNCTION printQList(qlist):
    for q in qlist:
        OUTPUT q.ID, " ", q.question_type
ENDFUNCTION

    ENDFOR
CLASS AddQuestion(QtGui.QWidget):
    FUNCTION __init__(self):
        QtGui.QWidget.__init__(self)
         setupUi(self)
    ENDFUNCTION

    FUNCTION setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(718, 659)
         verticalLayout_2 <- QtGui.QVBoxLayout(Form)
         verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
         verticalLayout <- QtGui.QVBoxLayout()
         verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
         label_6 <- QtGui.QLabel(Form)
         label_6.setObjectName(_fromUtf8("label_6"))
         verticalLayout.addWidget( label_6)
         QuestiontypeBox <- QtGui.QComboBox(Form)
         QuestiontypeBox.setObjectName(_fromUtf8("QuestiontypeBox"))
         QuestiontypeBox.addItem(_fromUtf8(""))
         QuestiontypeBox.addItem(_fromUtf8(""))
         QuestiontypeBox.addItem(_fromUtf8(""))
         QuestiontypeBox.addItem(_fromUtf8(""))
         verticalLayout.addWidget( QuestiontypeBox)
         label <- QtGui.QLabel(Form)
         label.setObjectName(_fromUtf8("label"))
         verticalLayout.addWidget( label)
         firstValue <- QtGui.QLineEdit(Form)
         firstValue.setObjectName(_fromUtf8("firstValue"))
         verticalLayout.addWidget( firstValue)
         label_2 <- QtGui.QLabel(Form)
         label_2.setObjectName(_fromUtf8("label_2"))
         verticalLayout.addWidget( label_2)
         secondValue <- QtGui.QLineEdit(Form)
         secondValue.setObjectName(_fromUtf8("secondValue"))
         verticalLayout.addWidget( secondValue)
         label_3 <- QtGui.QLabel(Form)
         label_3.setObjectName(_fromUtf8("label_3"))
         verticalLayout.addWidget( label_3)
         thirdValue <- QtGui.QLineEdit(Form)
         thirdValue.setObjectName(_fromUtf8("thirdValue"))
         verticalLayout.addWidget( thirdValue)
         label_4 <- QtGui.QLabel(Form)
         label_4.setObjectName(_fromUtf8("label_4"))
         verticalLayout.addWidget( label_4)
         FourthValue <- QtGui.QLineEdit(Form)
         FourthValue.setObjectName(_fromUtf8("FourthValue"))
         verticalLayout.addWidget( FourthValue)
         label_5 <- QtGui.QLabel(Form)
         label_5.setObjectName(_fromUtf8("label_5"))
         verticalLayout.addWidget( label_5)
         FifthValue <- QtGui.QLineEdit(Form)
              ENDIF
         FifthValue.setObjectName(_fromUtf8("FifthValue"))
              ENDIF
         verticalLayout.addWidget( FifthValue)
                                            ENDIF
         Submit <- QtGui.QPushButton(Form)
         Submit.setObjectName(_fromUtf8("Submit"))
         verticalLayout.addWidget( Submit)
         Cancel <- QtGui.QPushButton(Form)
         Cancel.setObjectName(_fromUtf8("Cancel"))
         verticalLayout.addWidget( Cancel)
         verticalLayout_2.addLayout( verticalLayout)
         retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    ENDFUNCTION

    FUNCTION retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
         label_6.setText(_translate("Form", "QuestionType:", None))
         QuestiontypeBox.setItemText(1, _translate("Form", " ", None))
         QuestiontypeBox.setItemText(1, _translate("Form", "Rate Constant", None))
         QuestiontypeBox.setItemText(2, _translate("Form", "Hardy-Weinberg", None))
         QuestiontypeBox.setItemText(3, _translate("Form", "Ideal Gas Equation", None))
         QuestiontypeBox.setItemText(4, _translate("Form", "Standard-Deviation", None))
        #  label.setText(_translate("Form", "First Value:", None))
        #  label_2.setText(_translate("Form", "Second Value:", None))
        # label_3.setText(_translate("Form", "Third Value:", None))
        # label_4.setText(_translate("Form", "Fourth Value:", None))
        # label_5.setText(_translate("Form", "Fifth Value", None))
                                                   ENDIF
         Submit.setText(_translate("Form", "Submit", None))
         Cancel.setText(_translate("Form", "Cancel", None))
         QuestiontypeBox.activated[str].connect( typechosen)
         Submit.clicked.connect( validate)
         clickedit <- False
         Cancel.clicked.connect( close)
    ENDFUNCTION

    FUNCTION typechosen(self, text):
         clickedit <- True
         questiontype <- text
        IF text = " ":
             typeNotSelected()
        ENDIF
        IF text = "Rate Constant":
             label.setText(_translate("Form", "Conc of A:", None))
             label_2.setText(_translate("Form", "Conc of B:", None))
             label_3.setText(_translate("Form", "Order of A:", None))
             thirdValue.setVisible(True)
             FourthValue.setVisible(True)
             FifthValue.setVisible(True)
                  ENDIF
             label_4.setText(_translate("Form", "Order of B:", None))
             label_5.setText(_translate("Form", "Rate of reaction", None))
        ENDIF
        IF text = "Hardy-Weinberg":
             label.setText(_translate("Form", "Total Population:", None))
             label_2.setText(_translate("Form", "No of Homozygotic Recessive:", None))
             label_3.setText(_translate("Form", "", None))
             thirdValue.setVisible(False)
             label_4.setText(_translate("Form", "", None))
             FourthValue.setVisible(False)
             label_5.setText(_translate("Form", "", None))
             FifthValue.setVisible(False)
        ENDIF
                  ENDIF
        IF text = "Ideal Gas Equation":
             label.setText(_translate("Form", "Pressure:", None))
             label_2.setText(_translate("Form", "Volume:", None))
             label_3.setText(_translate("Form", "No of Moles:", None))
             thirdValue.setVisible(True)
             label_4.setText(_translate("Form", "Temperature:", None))
             FourthValue.setVisible(True)
             label_5.setText(_translate("Form", " ", None))
             FifthValue.setVisible(False)
        ENDIF
                  ENDIF
        OUTPUT  questiontype
    ENDFUNCTION

    FUNCTION validate(self, text):
        IF  clickedit = False OR  questiontype = "":
             typeNotSelected()
        ELSE:
            valid <- True
            text <-  questiontype
            IF text = "Rate Constant":
                try:
                    FirstVal <- float( firstValue.text())
                    SecondVal <- float( secondValue.text())
                    ThirdVal <- int( thirdValue.text())
                    FourthVal <- int( FourthValue.text())
                    FifthVal <- float( FifthValue.text())
                     ENDIF
                except:
                    reply <- QtGui.QMessageBox()
                    reply.setText("Please enter numbers only.\nOrders must be integers.")
                    reply.setIcon(3)
                    reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
                    ret <- reply.exec_()
                    valid <- False
                IF ThirdVal > 3:
                    reply <- QtGui.QMessageBox()
                    reply.setText("Orders must be 1 OR 2.")
                    reply.setIcon(3)
                    reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
                    ret <- reply.exec_()                    
                    valid <- False
                ENDIF
                IF FourthVal > 3:
                    reply <- QtGui.QMessageBox()
                    reply.setText("Orders must be 1 OR 2.")
                    reply.setIcon(3)
                    reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
                    ret <- reply.exec_() 
                    valid <- False
                ENDIF
                try:
                        pow(FirstVal, ThirdVal) * (pow(SecondVal, FourthVal))
                except:
                        reply <- QtGui.QMessageBox()
                        reply.setText("Please use smaller concentrations.")
                        reply.setIcon(3)
                        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
                        ret <- reply.exec_()
                        valid <- False
            ENDIF
            IF text = "Hardy-Weinberg":
                try:
                    FirstVal <- float( firstValue.text())
                    SecondVal <- float( secondValue.text())
                    IF SecondVal > FirstVal:
                        reply <- QtGui.QMessageBox()
                        reply.setText("First Value must be larger than Second Value.")
                        reply.setIcon(3)
                        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
                        ret <- reply.exec_()
                        valid <- False
                    ENDIF
                except:
                     fieldsIncorrect()
                    valid <- False
            ENDIF
            IF valid = True:
                 create()
        ENDIF
            ENDIF
    ENDFUNCTION

    FUNCTION create(self):
        QID <- len(questions) + 1
        values <- [convertTofloat( firstValue.text()), convertTofloat( secondValue.text()),
                  convertTofloat( thirdValue.text()), convertTofloat( FourthValue.text()),
                  convertTofloat( FifthValue.text())]
                                       ENDIF
        OUTPUT "Making A Question with", QID,  questiontype, values
        newQuestion <- Question(QID,  questiontype, values)
        questions.append(newQuestion)
        with open('questions.pickle', 'wb') as f:
            pickle.dump(questions, f, pickle.HIGHEST_PROTOCOL)
         questionconfirmation()
        for question in questions:
            try:
                OUTPUT question.ID, question.values
            except:
                OUTPUT "Nope"
    ENDFUNCTION

        ENDFOR
    FUNCTION questionconfirmation(self):
        reply <- QtGui.QMessageBox()
        reply.setText("Question Added Successfully.")
        reply.setIcon(0)
        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
        ret <- reply.exec_()
         close()
    ENDFUNCTION

    FUNCTION fieldsIncorrect(self):
        reply <- QtGui.QMessageBox()
        reply.setText("Some fields are not correct.")
        reply.setIcon(3)
        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
        ret <- reply.exec_()
    ENDFUNCTION

    FUNCTION typeNotSelected(self):
        reply <- QtGui.QMessageBox()
        reply.setText("Question Type Field is not complete.")
        reply.setIcon(3)
        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
        ret <- reply.exec_()
    ENDFUNCTION

ENDCLASS

CLASS Question(object):
    FUNCTION __init__(self, ID, questiontype, values):
         question_type <- questiontype
         ID <- ID
        OUTPUT "storing",  ID
         values <- values
        IF  question_type = "Rate Constant":
             kQuestion()
        ENDIF
        IF  question_type = "Hardy-Weinberg":
             hardy_weinberg()
        ENDIF
    ENDFUNCTION

    FUNCTION kQuestion(self):
         conc_of_A <-  values[0]
         conc_of_B <-  values[1]
         order_of_A <-  values[2]
         order_of_B <-  values[3]
         rateOfReaction <-  values[4]
    ENDFUNCTION

    FUNCTION hardy_weinberg(self):
         totalpop <-  values[0]
         q_sqrdaspop <-  values[1]
         HWwindow
    ENDFUNCTION

    FUNCTION findK(self, window):
            QtGui.QApplication.processEvents()
            n <- 0
             intermediary <- pow( conc_of_A,  order_of_A) * (pow( conc_of_B,  order_of_B))
             k <-  rateOfReaction /  intermediary
            correct <- False
            window.label.setText(_translate("Form", "The conc of reactant A is " + str(
                "%.2E" %  conc_of_A) + " moldm^-3. The conc of B is " + str("%.2E" % conc_of_B) + " moldm^-3\n"
                                                                                "The order of A is " + str(
                 order_of_A) + " AND the order of B is " + str( order_of_B) + ". The rate of reaction is " + str(
                "%.2E" % rateOfReaction), None))
    ENDFUNCTION

    FUNCTION HWwindow(self):
        window.label.setText(_translate("hardy_weinberg", "If " + str("%.2G"%  q_sqrdaspop) + " out of " + str(
                  totalpop) + " individuals in a population express the recessive phenotype, what percent of the population would you predict would be heterozygotes? ",
                None))       
    ENDFUNCTION

ENDCLASS

CLASS Question_Set(object):
    FUNCTION __init__(self, ID, name, newQList, owner):
         QID <- ID
         name <- name
         QList <- newQList
         owner <- owner
    ENDFUNCTION

ENDCLASS

CLASS Practice_K_Window(QtGui.QDialog):
    FUNCTION __init__(self, values <- None):
        QtGui.QDialog.__init__(self)
         setupUi(self, values)
    ENDFUNCTION

    FUNCTION setupUi(self, Form, values):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(728, 437)
         verticalLayout_2 <- QtGui.QVBoxLayout(Form)
         verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
         label <- QtGui.QLabel(Form)
         label.setObjectName(_fromUtf8("label"))
         verticalLayout_2.addWidget( label)
        spacerItem <- QtGui.QSpacerItem(20, 60, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
         verticalLayout_2.addItem(spacerItem)
         verticalLayout <- QtGui.QVBoxLayout()
         verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
         verticalLayout_2.addLayout( verticalLayout)
         label_2 <- QtGui.QLabel(Form)
         label_2.setObjectName(_fromUtf8("label_2"))
         verticalLayout_2.addWidget( label_2)
        spacerItem1 <- QtGui.QSpacerItem(20, 50, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
         verticalLayout_2.addItem(spacerItem1)
         lineEdit <- QtGui.QLineEdit(Form)
         lineEdit.setObjectName(_fromUtf8("lineEdit"))
         verticalLayout_2.addWidget( lineEdit)
        spacerItem2 <- QtGui.QSpacerItem(20, 53, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
         verticalLayout_2.addItem(spacerItem2)
         pushButton <- QtGui.QPushButton(Form)
         pushButton.setEnabled(True)
         pushButton.setObjectName(_fromUtf8("pushButton"))
         verticalLayout_2.addWidget( pushButton)
        spacerItem3 <- QtGui.QSpacerItem(20, 72, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
         verticalLayout_2.addItem(spacerItem3)
         retranslateUi(Form, values)
        QtCore.QMetaObject.connectSlotsByName(Form)
    ENDFUNCTION

    FUNCTION retranslateUi(self, Form, values):
        IF values = None:
             thisQuestion <- generateK()
        ELSE:
             thisQuestion <- values
        ENDIF
        Form.setWindowTitle(_translate("Form", "Logged in as " + username, None))
         label.setText(_translate("Form", "Question Text Here", None))
         label_2.setText(_translate("Form", "Enter answer below to 3 sig fig in standard form replacing the ^ sign with an E. Specify plus or minus and use always usetwo numbers after the sign: 5.67E+01", None))
                                                                                                                                      ENDIF
                                                                                             ENDFOR
         pushButton.setText(_translate("Form", "Submit", None))
         pushButton.clicked.connect( checkAnswer)
         thisQuestion.findK(self)
    ENDFUNCTION

    FUNCTION checkAnswer(self):
        OUTPUT '%.2E' %  thisQuestion.k
         answer <- ('%.2E' %  thisQuestion.k)
         wrongorright()
    ENDFUNCTION

    FUNCTION wrongorright(self):
        reply <- QtGui.QMessageBox()
        IF str( lineEdit.text()) = str( answer):
            reply.setText("That is correct.")
            reply.setIcon(0)
            reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
            ret <- reply.exec_()
             close()
            IF  thisQuestion != None:
                 findStudent()              
            ENDIF
        ELSE:
                IF str( lineEdit.text()) = str( answer+"0"):
                        reply.setText("That is correct.")
                        reply.setIcon(0)
                        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
                        ret <- reply.exec_()
                         close()
                ELSE:
                        reply.setText("That is incorrect, try again.")
                        reply.setIcon(3)
                        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)  #
                        ret <- reply.exec_()
        ENDIF
                ENDIF
    ENDFUNCTION

    FUNCTION findStudent(self):
                    global username
                    for people in students:
                                IF people.username = username:
                                    people.questionAnswered( thisQuestion)
                                ENDIF
    ENDFUNCTION

ENDCLASS

                    ENDFOR
CLASS student():
    FUNCTION __init__(self, studentid, username, account_type, password, forename, surname, middlename, form, targetgrade,
                                                                    ENDFOR
                 questionsanswered, questionstoanswer, answeredcorrectly):
         forename <- forename
             ENDFOR
         username <- username
         account_type <- account_type
         password <- password
         surname <- surname
         middlename <- middlename
         answered <- questionsanswered
         questionstoanswer <- questionstoanswer
         answeredcorrectly <- answeredcorrectly
         studentid <- studentid
         form <- form
             ENDFOR
         targetgrade <- targetgrade
    ENDFUNCTION

    FUNCTION percentage(self):
         percentage <- int((len( answeredcorrectly) / len( answered)) * 100)
        OUTPUT  percentage
        RETURN  percentage
    ENDFUNCTION

    FUNCTION findgrade(self):
        isOntarget <- False
         percentage()
        x <-  percentage
        targetpercentage <- 0
        IF  targetgrade = "A":
            targetpercentage <- 75
        ENDIF
        IF  targetgrade = "B":
            targetpercentage <- 65
        ENDIF
        IF  targetgrade = "C":
            targetpercentage <- 55
        ENDIF
        IF  targetgrade = "D":
            targetpercentage <- 45
        ENDIF
        IF  targetgrade = "E":
            targetpercentage <- 35
        ENDIF
        IF  targetgrade = "F":
            targetpercentage <- 25
        ENDIF
        IF  targetgrade = "U":
            targetpercentage = 0
        ENDIF
        OUTPUT targetpercentage
        IF x > targetpercentage:
            isOntarget <- True
        ELSE:
            isOntarget <- False
        ENDIF
    ENDFUNCTION

    FUNCTION questionAnswered(self, question):
        for q in  questionstoanswer:
            OUTPUT q.ID
        ENDFOR
        try:
             questionstoanswer.remove(question)
             answered.append(question)
        except:
            with open('students.pickle', 'wb') as f:
                pickle.dump(students, f, pickle.HIGHEST_PROTOCOL)        
    ENDFUNCTION

ENDCLASS

CLASS hardy_weinberg(QtGui.QDialog):
    FUNCTION __init__(self, thisQuestion= None):
        QtGui.QDialog.__init__(self)
         Question <- thisQuestion
         setupUi(self)
    ENDFUNCTION

    FUNCTION setupUi(self, hardy_weinberg):
        hardy_weinberg.setObjectName(_fromUtf8("hardy_weinberg"))
        hardy_weinberg.resize(400, 300)
         verticalLayout <- QtGui.QVBoxLayout(hardy_weinberg)
         verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
         questions_text <- QtGui.QLabel(hardy_weinberg)
         questions_text.setObjectName(_fromUtf8("questions_text"))
         verticalLayout.addWidget( questions_text)
        spacerItem <- QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
         verticalLayout.addItem(spacerItem)
         answerBox <- QtGui.QLineEdit(hardy_weinberg)
         answerBox.setObjectName(_fromUtf8("answerBox"))
         verticalLayout.addWidget( answerBox)
         SubmitAnswer <- QtGui.QPushButton(hardy_weinberg)
         SubmitAnswer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
         SubmitAnswer.setObjectName(_fromUtf8("SubmitAnswer"))
         verticalLayout.addWidget( SubmitAnswer)
         retranslateUi(hardy_weinberg)
        QtCore.QMetaObject.connectSlotsByName(hardy_weinberg)
    ENDFUNCTION

    FUNCTION retranslateUi(self, hardy_weinberg):
        IF  Question = None:
             generate_H_W()
        ENDIF
        IF  Question != None:
             recessiveInpop <-  Question.values[1]
             totalpop <-  Question.values[0]
             calculateAnswer()
             updateForm(hardy_weinberg)
        ENDIF
    ENDFUNCTION

    FUNCTION findstudent(self):
        global username
        for people in students:
                    IF people.username = username:
                        people.questionAnswered( Question)
                    ENDIF
    ENDFUNCTION

        ENDFOR
    FUNCTION updateForm(self, hardy_weinberg):
         setWindowTitle(_translate("hardy_weinberg", "hardy_weinberg", None))
         questions_text.setText(_translate("hardy_weinberg", "If " + str(  q_sqrdaspop) + " out of " + str(
              totalpop) + " individuals in a population express the recessive phenotype, what percent of the population would you predict would be heterozygotes? ",
                                           None))
         SubmitAnswer.setText(_translate("hardy_weinberg", "Submit", None))
         SubmitAnswer.clicked.connect( checkAnswerpq)        
    ENDFUNCTION

    FUNCTION generate_H_W(self):
         totalpop <- random.randint(10,1000)
        IF  totalpop % 2 = 0:
             percentageReccessive <- random.randrange(0, 99, 2)
        ELSE:
             percentageReccessive <- random.randrange(1, 99, 2)
        ENDIF
         calculateAnswerfromRand()
         updateForm(hardy_weinberg)
    ENDFUNCTION

    FUNCTION calculateAnswerfromRand(self):        
        percentageReccessive <-  percentageReccessive
        totalpop <-  totalpop
        recessiveInpop <- ((totalpop * percentageReccessive) / 100)  # unrounded. Makes a percentage of the population have recessive alleles. 
        q_sqrdaspop <- Round_To_n(recessiveInpop, 1)  # now rounded
        qsqrd <- Round_To_n(q_sqrdaspop / totalpop, 3) # Finds q squared as a decimal.
        OUTPUT "recessives", q_sqrdaspop
        OUTPUT "qsqrd", qsqrd
        q <- Round_To_n(math.sqrt(qsqrd), 3) # finds the number of reccessive alleles
        p <- Round_To_n(1 - q, 3) #finds the number of dominant alleles
        psqrd <- Round_To_n(p * p, 3) #finds the number of homozygous dominant
        OUTPUT "psqrd", psqrd
        pq <- Round_To_n(p * q, 3) # finds heterozygotes
        OUTPUT "p", p, "q", q
        OUTPUT "2pq", pq * 2
         q_sqrdaspop <- q_sqrdaspop
         qsqrd <- qsqrd
         psqrd <- psqrd
         q <- q
         p <- p
         pq <- pq
    ENDFUNCTION

    FUNCTION calculateAnswer(self):
        totalpop <-  totalpop
        recessiveInpop <-  recessiveInpop
        q_sqrdaspop <- Round_To_n(recessiveInpop, 1)  # now rounded
        qsqrd <- Round_To_n(q_sqrdaspop / totalpop, 2) # Finds q squared as a decimal.
        OUTPUT "recessives", q_sqrdaspop
        OUTPUT "qsqrd", qsqrd
        q <- Round_To_n(math.sqrt(qsqrd), 2) # finds the number of reccessive alleles
        p <- Round_To_n(1 - q, 3) #finds the number of dominant alleles
        psqrd <- Round_To_n(p * p, 3) #finds the number of homozygous dominant
        OUTPUT "psqrd", psqrd
        pq <- Round_To_n(p * q, 3) # finds heterozygotes
        OUTPUT "p", p, "q", q
        OUTPUT "2pq", pq * 2
         q_sqrdaspop <- q_sqrdaspop
         qsqrd <- qsqrd
         psqrd <- psqrd
         q <- q
         p <- p
         pq <- pq        
    ENDFUNCTION

    FUNCTION checkAnswerpq(self):
        OUTPUT 2 *  pq
        IF  answerBox.text() = str(2 *  pq):
            reply <- QtGui.QMessageBox()
            reply.setText("Correct.")
            reply.setIcon(0)
            reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
            ret <- reply.exec_()
             close()
            IF  Question != None:
                 findstudent() # finds the person who is logged in
            ENDIF
        ELSE:
            reply <- QtGui.QMessageBox()
            reply.setText("Incorrect. Please try again.")
            reply.setIcon(3)
            reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
            ret <- reply.exec_()
        ENDIF
    ENDFUNCTION

ENDCLASS

CLASS findKreaction():
    FUNCTION __init__(self, conc_of_A, conc_of_B, order_of_A, order_of_B, rateOfReaction):
         conc_of_A <- conc_of_A
         conc_of_B <- conc_of_B
         order_of_A <- order_of_A
         order_of_B <- order_of_B
        #  rateNumber <- rateNumber
        #  rateExponent <- rateExponent
         rateOfReaction <- rateOfReaction
         noOfMoles <- (order_of_A + order_of_B)
    ENDFUNCTION

    FUNCTION walk_throughK(self):
        OUTPUT "To calculate the rate constant, k, we must first multiply the concentrations of our reactants together."
              "However the concentrations must be raised to the power of their orders."
              "The concentrations of A AND B are", str("%.2E" %  conc_of_A), "AND", str("%.2E" %  conc_of_B), "respectively."
                                                                                          "The order of A is",
               order_of_A, "AND the order of B is ",  order_of_B, " .")
        OUTPUT "This means our intermediary value is ", str("%.2E" %  intermediary, "."
                                                                          "We then divide our rate of reaction by this number. The reate of reaction is",
              str("%.2E" %  rateOfReaction), ".")
        OUTPUT "This equals",  k
        OUTPUT "Next we must find the units of k \n"
        OUTPUT "To find the units of k we must cancel the number of moles per dm cubed on both sides of the equation. "
              "\We do this by adding the powers of the two reactants AND putting them into the formula: "
                                                                                               ENDFOR
              "\nmol^-x dm^+x*3. Where x is the powers added together minus 1."
              "\nUnless the number of moles is one, then there are no units.\n ")
        IF  noOfMoles > 1:
            x <- int(( noOfMoles) - 1)
            OUTPUT "The units are mol^-", x, "dm^+", 3 * x, "s^-1"
        ELSE:
            OUTPUT "No units"
        ENDIF
    ENDFUNCTION

    FUNCTION findK(self, window):
        QtGui.QApplication.processEvents()
        n <- 0
         intermediary <- pow( conc_of_A,  order_of_A) * (pow( conc_of_B,  order_of_B))
         k <-  rateOfReaction /  intermediary
        correct <- False
        window.label.setText(_translate("Form", "The conc of reactant A is " + str("%.2E" %
             conc_of_A) + " moldm^-3. The conc of B is " + str("%.2E" %  conc_of_B) + " moldm^-3\n"
                                                                                     "The order of A is " + str(
             order_of_A) + " AND the order of B is " + str( order_of_B) + ". The rate of reaction is " + str(
           "%.2E" %   rateOfReaction) + "Find k of this reaction", None))
        # while correct = False:
          ENDWHILE
        # k <-  k
        #k <- ("%.3G" % (k))
        #studentAnswer <- input("Enter in your value of k to 3 sig fig: ")
        #if studentAnswer = k:
         ENDIF
        #correct <- True
        #another <- input("Would you like to try again? y/n")
        #if another = "y":
         ENDIF
        #loadQuestion()
        #if another = "n":
         ENDIF
        #if studentAnswer != k:
         ENDIF
        #n += 1
        #if n > 2:
         ENDIF
        #walkthrough <- input("Would you like a walk-through? y/n")
        #if walkthrough = "y":
         ENDIF
        #findKreaction.walk_throughK(self)
    ENDFUNCTION

    FUNCTION findunitsofK(self):
        OUTPUT "To find the units of k we must cancel the number of moles per dm cubed on both sides of the equation. "
              "\We do this by adding the powers of the two reactants AND putting them into the formula: "
                                                                                               ENDFOR
              "\nmol^-x dm^+x*3. Where x is the powers added together minus 1."
              "\nUnless the number of moles is one, then there are no units.\n ")
        IF  noOfMoles > 1:
            x <- int(( noOfMoles) - 1)
            OUTPUT "The units are mol^-", x, "dm^+", 3 * x, "s^-1"
        ELSE:
            OUTPUT "No units"
            # FUNCTION getRateOfReaction(self):
              ENDFUNCTION

            # rateOfReaction <-  k*(pow(10, rateExponent))
            # RETURN rateOfReaction
        ENDIF
    ENDFUNCTION

ENDCLASS

FUNCTION generateK():
    sig <- 3
    concofa <- random.uniform(0.001, 0.9)
                       ENDIF
                        ENDFOR
    concofA <- Round_To_n(concofa, 3)
    concofb <- random.uniform(0.001, 0.9)
                       ENDIF
                        ENDFOR
    concofB <- Round_To_n(concofb, 3)
    orderofA <- random.randrange(1, 3)
    orderofB <- random.randrange(1, 3)
    rate <- random.uniform(0.00000001, 0.0009)
                    ENDIF
                     ENDFOR
    rateofreaction <- Round_To_n(rate, 3)
    y <- findKreaction(concofA, concofB, orderofA, orderofB, rateofreaction)
    RETURN y
ENDFUNCTION

FUNCTION loadkQuestion():
    Q1 <- findKreaction(0.4, 0.4, 2, 1, 0.00000585)
    Q2 <- findKreaction(0.2, 0.3, 1, 2, 0.0000657)
    Q3 <- findKreaction(0.2, 0.3, 1, 2, 0.0000257)
    Q4 <- findKreaction(0.2, 0.3, 1, 2, 0.0000457)
    Q5 <- findKreaction(0.2, 0.3, 1, 2, 0.0000127)
    Q6 <- findKreaction(0.2, 0.3, 1, 2, 0.0100687)
    Q7 <- findKreaction(0.2, 0.3, 1, 2, 0.0000757)
    Q8 <- findKreaction(0.2, 0.3, 1, 2, 0.0000357)
    Q9 <- findKreaction(0.2, 0.3, 1, 2, 0.0000257)
    Questions <- [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9]
    x <- random.randrange(9)
    y <- Questions[x]
    RETURN y
ENDFUNCTION

FUNCTION format(number):
    ENDFOR
    number <- "%.2E"%number
    RETURN number
ENDFUNCTION

CLASS LogInPage(QtGui.QDialog):
    FUNCTION __init__(self):
        QtGui.QDialog.__init__(self)
         setupUi(self)
    ENDFUNCTION

    FUNCTION setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
         verticalLayout <- QtGui.QVBoxLayout(Form)
         verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
         label <- QtGui.QLabel(Form)
         label.setObjectName(_fromUtf8("label"))
         verticalLayout.addWidget( label)
         UsernameBox <- QtGui.QLineEdit(Form)
         UsernameBox.setObjectName(_fromUtf8("UsernameBox"))
         verticalLayout.addWidget( UsernameBox)
        spacerItem <- QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
         verticalLayout.addItem(spacerItem)
         label_2 <- QtGui.QLabel(Form)
         label_2.setObjectName(_fromUtf8("label_2"))
         verticalLayout.addWidget( label_2)
         PasswordBox <- QtGui.QLineEdit(Form)
         PasswordBox.setEchoMode(QtGui.QLineEdit.Password)
         PasswordBox.setObjectName(_fromUtf8("PasswordBox"))
         verticalLayout.addWidget( PasswordBox)
        spacerItem1 <- QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
         verticalLayout.addItem(spacerItem1)
         pushButton <- QtGui.QPushButton(Form)
         pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
         pushButton.setObjectName(_fromUtf8("pushButton"))
         verticalLayout.addWidget( pushButton)
         pushButton_2 <- QtGui.QPushButton(Form)
         pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
         pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
         verticalLayout.addWidget( pushButton_2)
         retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    ENDFUNCTION

    FUNCTION retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Log In", "Log In", None))
         label.setText(_translate("Form", "Username:", None))
         label_2.setText(_translate("Form", "Password:", None))
         pushButton.setText(_translate("Form", "Log In", None))
         pushButton_2.setText(_translate("Form", "Cancel", None))
         pushButton_2.clicked.connect( close)
         pushButton.clicked.connect( checkCredentials)
    ENDFUNCTION

    FUNCTION checkCredentials(self, Form):
        global username
         isStudent <- False
         isTeacher <- False
        for people in students:
            IF  UsernameBox.text() = people.username AND  PasswordBox.text() = people.password:
                IF people.account_type = "S":
                     close()
                    username <- people.username
                    global studentmainForm
                    studentmainForm <- Student_Main_Window()
                    studentmainForm.show()
                     isStudent <- True
            ENDIF
                ENDIF
        ENDFOR
        for people in teachers:
            IF  UsernameBox.text() = people.username AND  PasswordBox.text() = people.password:
                username <- people.username
                IF people.account_type = "T" OR people.account_type = "A":
                     close()
                    global teacherMainForm
                    teacherMainForm <- Teacher_Main_Window()
                    teacherMainForm.show()
                     isTeacher <- True
            ENDIF
                ENDIF
        ENDFOR
        IF  isTeacher = False AND  isStudent = False:
             incorrectID()
        ENDIF
    ENDFUNCTION

    FUNCTION incorrectID(self):
        reply <- QtGui.QMessageBox()
        reply.setText("Your Username OR Password is incorrect. Please try again.")
        reply.setIcon(0)
        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
        ret <- reply.exec_()
        reply.close()
    ENDFUNCTION

ENDCLASS

FUNCTION loadTeachers():
    global teachers
    with open('teachers.pickle', 'rb') as t:
        teachers <- pickle.load(t)
    IF teachers = []:
        reply <- QtGui.QMessageBox()
        reply.setText("Please make an admin account using AdminTools.")
        reply.setIcon(3)
        reply.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
        ret <- reply.exec_()
        #for people in teachers:
           # OUTPUT people.username, people.password
    ENDIF
ENDFUNCTION

         ENDFOR
FUNCTION loadStudents():
    global students
    with open('students.pickle', 'rb') as s:
        students <- pickle.load(s)
        #for people in students:
            # empty <- []
            # people.questionstoanswer <- empty
            # with open('students.pickle', 'wb') as f:
            # pickle.dump(students, f, pickle.HIGHEST_PROTOCOL)
ENDFUNCTION

         ENDFOR
FUNCTION Round_To_n(x, n):
    RETURN round(x, int(n - math.ceil(math.log10(abs(x)))))
ENDFUNCTION

CLASS EditStudents(QtGui.QDialog):
    FUNCTION __init__(self, values <- None):
        QtGui.QDialog.__init__(self)
         setupUi(self)
    ENDFUNCTION

    FUNCTION setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Delete Students"))
        Form.resize(769, 659)
         verticalLayout <- QtGui.QVBoxLayout(Form)
         verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
         treeWidget <- QtGui.QTreeWidget(Form)
         treeWidget.setObjectName(_fromUtf8("treeWidget"))
         verticalLayout.addWidget( treeWidget)
         Delete <- QtGui.QPushButton(Form)
         Delete.setObjectName(_fromUtf8("Delete"))
         verticalLayout.addWidget( Delete)
         Cancel <- QtGui.QPushButton(Form)
         Cancel.setObjectName(_fromUtf8("Cancel"))
         verticalLayout.addWidget( Cancel)
         retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    ENDFUNCTION

    FUNCTION retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Delete Student Accounts", None))
         treeWidget.headerItem().setText(0, _translate("Form", "Student ID", None))
         treeWidget.headerItem().setText(1, _translate("Form", "Name", None))
         treeWidget.headerItem().setText(2, _translate("Form", "Username", None))
         treeWidget.headerItem().setText(3, _translate("Form", "Password", None))
         treeWidget.headerItem().setText(4, _translate("Form", "Form", None))
         Delete.setText(_translate("Form", "Delete", None))
         Cancel.setText(_translate("Form", "Cancel", None))
         Delete.clicked.connect( delete)
         Cancel.clicked.connect( close)
         populateTree()
    ENDFUNCTION

    FUNCTION delete(self):
        thisID <-  treeWidget.currentItem().text(0)
        OUTPUT thisID
        for people in students:
            IF str(people.studentid) = thisID:
                students.remove(people)
                OUTPUT "removed", thisID
                with open('students.pickle', 'wb') as f:
                    pickle.dump(students, f, pickle.HIGHEST_PROTOCOL)
            ENDIF
        ENDFOR
         populateTree()
    ENDFUNCTION

    FUNCTION populateTree(self):
         treeWidget.clear()
        rowCount <- -1
        global students
        for people in students:
            rowCount += 1
            QtGui.QTreeWidgetItem( treeWidget)
             treeWidget.topLevelItem(rowCount).setText(0, str(people.studentid))
             treeWidget.topLevelItem(rowCount).setText(1, people.forename)
                                                                     ENDFOR
             treeWidget.topLevelItem(rowCount).setText(2, people.username)
             treeWidget.topLevelItem(rowCount).setText(3, people.password)
             treeWidget.topLevelItem(rowCount).setText(4, people.form)
    ENDFUNCTION

ENDCLASS

        ENDFOR
                                                                     ENDFOR
FUNCTION convertTofloat(thing):
    try:
        thing <- float(thing)
        RETURN thing
    except:
        RETURN 0.0
ENDFUNCTION

FUNCTION loadQuestions():
    global questions
    with open('questions.pickle', 'rb') as q:
        questions <- []
        questions <- pickle.load(q)
ENDFUNCTION

FUNCTION loadQSet():
    global QSets
    QSets <- []
    with open('QSets.pickle', 'rb') as q:
        QSets <- pickle.load(q)
        #for n in range(len(QSets) - 1):
           # OUTPUT QSets[n + 1].name
            # OUTPUT QSets
            # OUTPUT QSets[1].QList[1].values
ENDFUNCTION

         ENDFOR
loadQuestions()
loadQSet()
loadStudents()
loadTeachers()
app <- QtGui.QApplication(sys.argv)
thisForm <- LogInPage()
thisForm.show()
sys.exit(app.exec_())
