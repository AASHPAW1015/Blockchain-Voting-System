import sys
from PyQt5 import QtWidgets
from signupuser import Ui_Dialog  # Import the generated class from your UI file

class SignupApp(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Initially hide additional widgets
        self.lineEdit_4.setVisible(False)  # Password input
        self.pushButton_2.setVisible(False)  # Additional Enter button
        self.label.setVisible(False)  # Initially hide the label

        # Connect the button signals to their respective slots
        self.pushButton.clicked.connect(self.display_username)
        self.pushButton_2.clicked.connect(self.submit)

    def display_username(self):
        # Get the username from the lineEdit
        username = self.lineEdit.text()
        
        # Update the label to show the username
        self.label.setText(f"Your username is: 000000")
        
        # Show the label
        self.label.setVisible(True)  # Show the label
        
        # Hide the first "Enter" button
        self.pushButton.setVisible(False)  # Hide the first button
        
        # Show the password field and the additional button
        self.lineEdit_4.setVisible(True)  # Show password input
        self.pushButton_2.setVisible(True)  # Show additional Enter button

    def submit(self):
        # Handle submission logic here (e.g., print the details, save to a database, etc.)
        name = self.lineEdit.text()
        age = self.lineEdit_2.text()
        state = self.lineEdit_3.text()
        aadhar_number = self.lineEdit_6.text()
        password = self.lineEdit_4.text()

        # Example output
        print(f"Name: {name}, Age: {age}, State: {state}, Aadhar Number: {aadhar_number}, Password: {password}")

        # Optionally, you can close the dialog after submission
        self.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = SignupApp()
    dialog.show()
    sys.exit(app.exec_())
