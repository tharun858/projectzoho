import sys
from PyQt5.QtWidgets import (QApplication as QA, QWidget as QW, QPushButton as QPB, QLabel as QL, QLineEdit as QLE, QGridLayout as QGL, QMessageBox as QMB)
import sqlite3
import contact_zoho
con = 'none'
def connections():
	global con
	con=sqlite3.connect("demo.db")

def Adding(Query):
	global con
	try:

		con.execute(Query)
		con.commit()
	except:
		con.execute("create table cred(Email varchar(20),password varchar(20),Secret varchar(20))")
	return 1
def check(Email, password, Query):
	global con
	cu = con.execute(Query)
	k=0
	for row in cu:
		if row[0]==Email and row[1]==password:
			return 1
		else:
			k=1
	if k==1:
		return 0

class LoginForm(QW):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Sign In')
		self.resize(700, 220)

		layout = QGL()
		#comment Dont have an account?
		label_ad = QL('<font size="3"> Dont have an account? </font>')
		layout.addWidget(label_ad, 0, 0)

		#sign up button
		label1=QL()
		label1.setText('SignUp')
		label1.mouseReleaseEvent = final2
		layout.addWidget(label1, 0, 1)
		
		#Email___
		label_name = QL('<font size="4"> Email </font>')
		self.lineEdit_username = QLE()
		layout.addWidget(label_name, 1, 0)
		layout.addWidget(self.lineEdit_username, 2, 0, 1, 3)
		#Password___
		label_password = QL('<font size="4"> Password </font>')
		self.lineEdit_password = QLE()
		layout.addWidget(label_password, 3, 0)
		layout.addWidget(self.lineEdit_password, 4, 0, 1, 3)

		# Forgot password dialog
		label_ad = QL('<font size="3"> Forgot Password? </font>')
		layout.addWidget(label_ad, 5, 2)

		#sign in button
		button_login = QPB('Sign In')
		button_login.clicked.connect(self.check_password)
		button_login.setStyleSheet("QPushButton"
                             "{"
                             "background-color : skyblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : green;"
                             "}"
                             )
		layout.addWidget(button_login, 6, 0, 1, 3)
		
		self.setLayout(layout)

	def check_password(self):
		msg = QMB()
		Email= self.lineEdit_username.text()
		password= self.lineEdit_password.text()
		Query= "select * from cred"
		flag= check(Email, password, Query)
		if flag == 1  :
			#msg.setText('Success')
			#msg.exec_()
			#app.quit()
			contact.connections()
			self.show_c = contact.LoginForm()
			self.show_c.show()
		else:
			msg.setText('Incorrect Password')
			msg.exec_()



class SignUp(QW):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Sign Up')
		self.resize(700, 220)

		layout = QGL()
		#Already have an account?
		label_ad = QL('<font size="3"> Already have an account?  </font>')
		layout.addWidget(label_ad, 0, 0)
		#SignIn
		label1=QL()
		label1.setText('SignIn')
		label1.mouseReleaseEvent = final1
		layout.addWidget(label1, 0, 1)
		#Email
		label_name = QL('<font size="4"> Email </font>')
		self.lineEdit_username = QLE()
		layout.addWidget(label_name, 1, 0)
		layout.addWidget(self.lineEdit_username, 2, 0)

		label_password = QL('<font size="4"> Password </font>')
		self.lineEdit_password = QLE()
		layout.addWidget(label_password, 3, 0)
		layout.addWidget(self.lineEdit_password, 4, 0)

		label_Secret = QL('<font size="4"> Secret </font>')
		self.lineEdit_Secret = QLE()
		layout.addWidget(label_Secret, 5, 0)
		layout.addWidget(self.lineEdit_Secret, 6, 0)	


		button_login = QPB('Sign Up')
		button_login.clicked.connect(self.checking_password)
		button_login.setStyleSheet("QPushButton"
                             "{"
                             "background-color : skyblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : green;"
                             "}"
                             )
		layout.addWidget(button_login, 7, 0, 1, 2)
		#layout.setRowMinimumHeight(2, 75)

		label_ad = QL('<font size="3"> By clicking the "SignUp" button, you are creating an account, and you agree to the Terms of Use. </font>')
		layout.addWidget(label_ad, 8, 0, 1, 2)
		

		self.setLayout(layout)

	

	def checking_password(self):
		msg = QMB()
		Email= self.lineEdit_username.text()
		password= self.lineEdit_password.text()
		Secret= self. lineEdit_Secret.text()
		Query= "insert into cred values('"+Email+"','"+password+"','"+Secret+"')"
		flag= Adding(Query)
		if flag == 1  :
			msg.setText('User Created')
			msg.exec_()
			app.quit()
		else:
			msg.setText('Failed to create')
			msg.exec_()


def final2(a1):
	global form
	form = SignUp()
	form.show()
def final1(a2):
	global form
	form = LoginForm()
	form.show()
if __name__ == '__main__':
	app = QA(sys.argv)
	connections()
	form = LoginForm()
	form.show()

	sys.exit(app.exec_())