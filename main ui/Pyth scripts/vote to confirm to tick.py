# main.py

import sys
from PyQt5 import QtWidgets
from votechange import Ui_Dialog  # Import the Ui_Dialog class from vote.py

class VotingApp(QtWidgets.QDialog):
    def __init__(self):
        super(VotingApp, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Initialize the UI state
        self.initialize_ui()
        self.current_house_index = None  # Track the currently selected house index

    def initialize_ui(self):
        # Hide all confirm buttons, tick labels, block labels, and done button initially
        for i in range(len(self.ui.vote_buttons)):
            self.ui.confirm_buttons[i].hide()
            self.ui.tick_labels[i].hide()
            self.ui.block_labels[i].hide()
        
        self.ui.pushButton_done.hide()  # Initially hidden

        # Connect signals to the buttons
        for i in range(len(self.ui.vote_buttons)):
            self.ui.vote_buttons[i].clicked.connect(lambda _, index=i: self.handle_vote(index))
            self.ui.confirm_buttons[i].clicked.connect(lambda _, index=i: self.handle_confirm(index))

        self.ui.pushButton_done.clicked.connect(self.handle_done)  # Handle done button

    def handle_vote(self, house_index):
        # If there is a current house selected, reset its buttons
        if self.current_house_index is not None:
            # Hide the confirm button for the previously selected house
            self.ui.confirm_buttons[self.current_house_index].hide()
            # Show the vote button for the previously selected house
            self.ui.vote_buttons[self.current_house_index].show()

        # Update the current house index
        self.current_house_index = house_index
        
        # Hide the vote button for the selected house and show confirm button
        self.ui.vote_buttons[house_index].hide()  # Hide the vote button
        self.ui.confirm_buttons[house_index].show()  # Show confirm button

    def handle_confirm(self, house_index):
        # Hide the confirm button and show tick label and done button for the confirmed house
        self.ui.confirm_buttons[house_index].hide()  # Hide confirm button
        self.ui.tick_labels[house_index].show()  # Show tick label
        self.ui.pushButton_done.show()  # Show done button

        # Show block labels for all other houses
        for i in range(len(self.ui.block_labels)):
            if i != house_index:
                self.ui.block_labels[i].show()  # Show block label for other houses

        # Hide all other vote buttons
        for i in range(len(self.ui.vote_buttons)):
            if i != house_index:
                self.ui.vote_buttons[i].hide()  # Hide other vote buttons

        # Reset current house index since voting is complete
        self.current_house_index = None

    def handle_done(self):
        # Logic to handle what happens when DONE is clicked
        print("Voting completed.")
        self.close()  # Close the dialog or implement additional logic

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = VotingApp()
    window.show()
    sys.exit(app.exec_())
