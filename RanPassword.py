import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QClipboard

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Generator')
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.password_label = QLabel(self)
        self.layout.addWidget(self.password_label)
        self.password_label.setStyleSheet("color:red;font-size:30px;border:1px solid black;")

        self.length_layout = QHBoxLayout()
        self.length_label = QLabel('Enter length of password:', self)
        self.length_layout.addWidget(self.length_label)

        self.length_input = QLineEdit(self)
        self.length_layout.addWidget(self.length_input)
        self.layout.addLayout(self.length_layout)
        self.length_label.setStyleSheet("color:blue;font-size:15px;border:1px solid black;")

        self.generate_button = QPushButton('Generate Password', self)
        self.generate_button.clicked.connect(self.generate_password)
        self.generate_button.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; border: none; padding: 10px; text-align: center; text-decoration: none; display: inline-block; font-size: 14px; margin: 4px 2px; cursor: pointer; border-radius: 4px; } QPushButton:hover { background-color: #45a049; }")
        self.layout.addWidget(self.generate_button)

        self.copy_button = QPushButton('Copy Password', self)
        self.copy_button.clicked.connect(self.copy_password)
        self.copy_button.setStyleSheet("QPushButton { background-color: #008CBA; color: white; border: none; padding: 10px; text-align: center; text-decoration: none; display: inline-block; font-size: 14px; margin: 4px 2px; cursor: pointer; border-radius: 4px; } QPushButton:hover { background-color: #0073e6; }")
        self.layout.addWidget(self.copy_button)

        self.regenerate_button = QPushButton('Regenerate Password', self)
        self.regenerate_button.clicked.connect(self.regenerate_password)
        self.regenerate_button.setStyleSheet("QPushButton { background-color: #f44336; color: white; border: none; padding: 10px; text-align: center; text-decoration: none; display: inline-block; font-size: 14px; margin: 4px 2px; cursor: pointer; border-radius: 4px; } QPushButton:hover { background-color: #db2828; }")
        self.layout.addWidget(self.regenerate_button)

        self.accept_button = QPushButton('Accept', self)
        self.accept_button.clicked.connect(self.accept_password)
        self.accept_button.setStyleSheet("QPushButton { background-color: #555555; color: white; border: none; padding: 10px; text-align: center; text-decoration: none; display: inline-block; font-size: 14px; margin: 4px 2px; cursor: pointer; border-radius: 4px; } QPushButton:hover { background-color: #333333; }")
        self.layout.addWidget(self.accept_button)

        self.setLayout(self.layout)

    def generate_password(self):
        password_length_text = self.length_input.text()
        if password_length_text.isdigit():
            password_length = int(password_length_text)
            password_characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(password_characters) for i in range(password_length))
            self.password_label.setText("Generated Password: " + password)
            self.generated_password = password
        else:
            QMessageBox.warning(self, 'Invalid Length', 'Please enter a valid integer length for the password.')

    def copy_password(self):
        if hasattr(self, 'generated_password'):
            clipboard = QApplication.clipboard()
            clipboard.setText(self.generated_password)
            QMessageBox.information(self, 'Password Copied', 'Password has been copied to clipboard.')
        else:
            QMessageBox.warning(self, 'No Password', 'Please generate a password first.')

    def regenerate_password(self):
        if hasattr(self, 'generated_password'):
            self.generate_password()
        else:
            QMessageBox.warning(self, 'No Password', 'Please generate a password first.')

    def accept_password(self):
        if hasattr(self, 'generated_password'):
            QMessageBox.information(self, 'Password Accepted', 'Password has been accepted.')
            # Do something with the accepted password here, like storing it securely.
        else:
            QMessageBox.warning(self, 'No Password', 'Please generate a password first.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec_())
