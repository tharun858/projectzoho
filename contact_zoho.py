import sys
from PyQt5.QtWidgets import (QApplication as QA, QWidget as QW, QPushButton as QPB, QLabel as QL, QLineEdit as QLE, QGridLayout as QGL, QMessageBox as QM)
import sqlite3
con= 'none'
def connections():
	global con
	con=sqlite3.connect("demo.db")

def Adding(Name, Ph_no, Email,t_table):
	global con
	Query= "insert into My_Contacts values('"+Name+"','"+Ph_no+"','"+Email+"')"
	try:
		con.execute(Query)
		con.commit()
	except:
		con.execute("create table My_Contacts(Name varchar(20),Ph_no INT, Email varchar(30))")
		con.execute(Query)
	check(t_table)

def check(t_table):
	global con
	cu = con.execute('select * from My_Contacts')
	k=0
	t_string="<table border=5><tr><th>Name</th><th>Ph_no</th><th>Email</th></tr>"
	for line in cu:
		if len(str(line[0]))!=0:
			t_string+="<tr><td>"+str(line[0])+"</td><td>"+str(line[1])+"</td><td>"+str(line[2])+"</td></tr>"
	t_string+="</table>"
	t_table.setText(t_string)


class LoginForm(QW):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Contact Form And Contact List Page')
		self.resize(400, 150)

		layout = QGL()
		#comment Dont have an account?
		label_ad = QL('<font size="5"> Add Contacts </font>')
		layout.addWidget(label_ad, 0, 1)

		#sign up button
		
		
		#Email___
		label_name = QL('<font size="4"> Name </font>')
		self.lineEdit_user_name = QLE()
		layout.addWidget(label_name, 1, 0)
		layout.addWidget(self.lineEdit_user_name, 2, 0, 1, 3)
		#Password___
		label_ph_no= QL('<font size="4"> Ph_no </font>')
		self.lineEdit_ph_no = QLE()
		layout.addWidget(label_ph_no, 3, 0)
		layout.addWidget(self.lineEdit_ph_no, 4, 0, 1, 3)

		label_Email= QL('<font size="4"> Email </font>')
		self.lineEdit_Email = QLE()
		layout.addWidget(label_Email, 5, 0)
		layout.addWidget(self.lineEdit_Email, 6, 0, 1, 3)

		# Forgot password dialog
		

		#sign in button
		button_login = QPB('Save')
		button_login.clicked.connect(self.extract)
		button_login.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : skyblue;"
                             "}"
                             )
		layout.addWidget(button_login, 7, 2)
		self.t_title = QL('<font size="6"> My Contacts </font>')
		layout.addWidget(self.t_title, 8, 1)

		self.t_table = QL()
		layout.addWidget(self.t_table, 9, 1)
		
		
		self.setLayout(layout)

	def extract(self):
		Name= self.lineEdit_user_name.text()
		Ph_no= self.lineEdit_ph_no.text()			
		Email= self. lineEdit_Email.text()
		Adding(Name,Ph_no,Email,self.t_table)

if __name__ == '__main__':
	app = QA(sys.argv)
	connections()
	form = LoginForm()
	form.show()

	sys.exit(app.exec_())