from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QListWidget,QLineEdit,QPushButton,QWidget,QMainWindow,QApplication,QComboBox,QMessageBox, QDateEdit
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QDate
import sys
import mysql.connector

#connect with MySql server LocalHost

mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='Sasi@2004',
        database='todo')
myc=mydb.cursor()

#Widget Class
class Window(QWidget):
    def __init__(self):
        super().__init__()
        #set window
        self.setWindowTitle("To-Do List Application")
        self.setGeometry(100, 100, 600, 400)
        
        #set up userr interface
        self.AUI()
        
    def AUI(self):
        #Set-up Window
        self.setWindowIcon(QIcon('todo.jpg'))
        #choose List-Layout and add widgets
        self.Layout=QVBoxLayout()
        self.List=QListWidget()
        self.setStyleSheet("background-color: #ECF0F1 ;") 
        self.List.setStyleSheet("background-color:#E5E7E9;color:#2C3E50;border:1px solid black;font-size: 25px;")
        self.Layout.addWidget(self.List)
        #choose Widget-List add buttons and all 
        self.H_Layout=QHBoxLayout()
        self.Input=QLineEdit()
        self.Input.setStyleSheet("background-color:#E5E7E9;color:#E74C3C;border:1px solid black;font-size: 20px;")
        self.Input.setPlaceholderText("Enter any Taks")
        self.AButton=QPushButton("ADD-Task")
        #style sheet for ADD button
        self.AButton.setStyleSheet("""QPushButton {
            background-color: #55F918; 
            height:27px;
            width:60px;
            border-radius:5px;
        }
        QPushButton:hover {
            background-color: #18F6F9;
        }
    """)
        self.H_Layout.addWidget(self.Input)
        self.H_Layout.addWidget(self.AButton)
        self.Layout.addLayout(self.H_Layout)
        self.AButton.clicked.connect(self.AddItem)
        
        self.opl=QHBoxLayout()
        self.SD=QDateEdit()
        self.SD.setDate(QDate.currentDate())
        self.SD.setCalendarPopup(True)
        self.opl.addWidget(self.SD)
        self.ED=QDateEdit()
        self.ED.setDate(QDate.currentDate())
        self.ED.setCalendarPopup(True)
        self.opl.addWidget(self.ED)
        self.Layout.addLayout(self.opl)
        #Add makeout list to the  Window :)
        self.FinalLayout=QHBoxLayout()
        self.RButton=QPushButton("REMOVE-TASK")
        self.prev=QPushButton("Works")
        self.FinalLayout.addWidget(self.prev)
        self.FinalLayout.addWidget(self.RButton)
        self.Layout.addLayout(self.FinalLayout)
        #style-sheet for Remove button
        self.RButton.setStyleSheet("""QPushButton {
            background-color: #F9183E; 
            color:white;
            height:27px;
            width:60px;
            border-radius:5px;
        }
        QPushButton:hover {
            background-color: black;
            color:yellow;
        }
    """)
        self.prev.setStyleSheet("""QPushButton {
            background-color: #D5DBDB; 
            color:black;
            height:27px;
            width:60px;
            border-radius:5px;
        }
        QPushButton:hover {
            background-color: #0DEED6 ;
            color:red;
        }
    """)
        #connect Remove Button
        self.RButton.clicked.connect(self.RItem)
        
        #connect works
        self.prev.clicked.connect(self.Write)
        
        #Final-Layout
        self.setLayout(self.Layout)
        
    def AddItem(self):
        text=self.Input.text()
        if text:
            sd=self.SD.date().toString('dd/MM/yyyy')
            ed=self.ED.date().toString('dd/MM/yyyy')
            text=text+" {"+sd+' - '+ed+'}'
            self.List.addItem(text)
            self.Input.clear()
            sql="insert into works values(%s,%s,%s)"
            myc.execute(sql,(text,sd,ed))
            mydb.commit()
        else:
            QMessageBox.warning(self,'Enter','a task to-do')
        #self.AButton.setStyleSheet("background-color: #4caf50; color: white; font-size: 14px; border: none; padding: 8px 12px; border-radius: 5px;")
        
    def RItem(self):
        done=self.List.currentItem()
        i=self.List.currentItem().text()
        if done:
            print(type(i))
            i=(i,)
            sql='delete from works where work=%s'
            myc.execute(sql,i)
            mydb.commit()
            self.List.takeItem(self.List.row(done))
        else:
            QMessageBox.warning(self,'Enter','a task to-do')
    def Write(self):
        myc.execute('select * from works')
        results=myc.fetchall()
        for i in results:
            string=str(i)
            string=string[2:len(string)-2]
            string=string.split(',')
            s=string[0]
            s=s[:len(s)-1]
            self.List.addItem(s)
            
app=QApplication(sys.argv)
win=Window()
win.show()
sys.exit(app.exec_())