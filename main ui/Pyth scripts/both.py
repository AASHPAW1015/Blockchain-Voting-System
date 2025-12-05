import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from tabs import Ui_Dialog as UiTabs  # Keep the original class name
from loginuser import Ui_Dialog as UiLoginUser  # Keep the original class name
from signupuser import Ui_Dialog as UiSignupUser  # Keep the original class name

class MainApp(QMainWindow, UiTabs):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect the buttons to their respective methods
        self.pushButton_2.clicked.connect(self.open_loginuser)  # Open login dialog for users
        self.pushButton_3.clicked.connect(self.open_signupuser)  # Open signup dialog for users
        self.pushButton.clicked.connect(self.open_moderator_login)  # Open login dialog for moderator

    def open_loginuser(self):
        self.loginuser_dialog = LoginUserDialog()
        self.loginuser_dialog.exec_()  # Show the login dialog as modal

    def open_signupuser(self):
        self.signupuser_dialog = SignupUserDialog()
        self.signupuser_dialog.exec_()  # Show the signup dialog as modal

    def open_moderator_login(self):
        # Open a separate dialog for moderator login
        self.moderator_login_dialog = LoginUserDialog()  # You can create a new class if needed
        self.moderator_login_dialog.exec_()  # Show the moderator login dialog

class LoginUserDialog(QDialog, UiLoginUser):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect the button in the login dialog
        self.pushButton.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()  # Assuming you have a password field
        print(f"Logging in with Username: {username}, Password: {password}")
        # Add your login logic here
        self.close()  # Close the dialog after logging in

class SignupUserDialog(QDialog, UiSignupUser):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Initially hide elements that should only show after signup
        self.label.setVisible(False)  # Hide the username label initially
        self.lineEdit_4.setVisible(False)  # Hide the password input for signup
        self.pushButton_2.setVisible(False)  # Hide the signup button

        # Connect buttons in the signup dialog
        self.pushButton.clicked.connect(self.show_signup)  # Show fields when clicked
        self.pushButton_2.clicked.connect(self.handle_signup)  # Handle the signup action

    def show_signup(self):
        # Show signup fields
        self.lineEdit_4.setVisible(True)  # Show password field for signup
        self.pushButton_2.setVisible(True)  # Show signup button
        self.label.setVisible(True)  # Show the username label
        self.pushButton.setVisible(False)  # Hide the initial button to enter username

    def handle_signup(self):
        username = self.lineEdit.text()  # Username input
        password = self.lineEdit_4.text()  # Password input
        print(f"Signing up with Username: {username}, Password: {password}")
        
        # Display the username
        self.label.setText(f"Your username is: {username}")
        self.label.setVisible(True)  # Show the label with username

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
