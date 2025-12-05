# vote.py

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(40, 40, 321, 231))
        self.frame.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 10, 191, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.pushButton_back = QtWidgets.QPushButton(self.frame)
        self.pushButton_back.setGeometry(QtCore.QRect(0, 0, 61, 16))
        self.pushButton_back.setObjectName("pushButton_back")

        # Create lists to hold button and label objects
        self.vote_buttons = []
        self.confirm_buttons = []
        self.tick_labels = []
        self.block_labels = []

        # Create buttons and labels for multiple houses
        for i in range(4):  # Assume 4 houses
            # House label
            house_label = QtWidgets.QLabel(self.frame)
            house_label.setGeometry(QtCore.QRect(30, 70 + (i * 30), 81, 16))
            font.setBold(True)
            house_label.setFont(font)
            house_label.setAlignment(QtCore.Qt.AlignCenter)
            house_label.setObjectName(f"label_{i}")
            house_label.setText(f"House {i + 1}")

            # Vote buttons
            vote_button = QtWidgets.QPushButton(self.frame)
            vote_button.setGeometry(QtCore.QRect(180, 70 + (i * 30), 75, 23))
            vote_button.setStyleSheet("background-color: rgb(0, 170, 0);\n"
                                       "color: rgb(255, 255, 255);")
            vote_button.setObjectName(f"pushButton_vote_{i}")
            vote_button.setText("Vote")
            self.vote_buttons.append(vote_button)

            # Confirm buttons
            confirm_button = QtWidgets.QPushButton(self.frame)
            confirm_button.setGeometry(QtCore.QRect(260, 70 + (i * 30), 75, 23))
            confirm_button.setObjectName(f"pushButton_confirm_{i}")
            confirm_button.setText("Confirm")
            confirm_button.hide()  # Initially hidden
            self.confirm_buttons.append(confirm_button)

            # Tick labels
            tick_label = QtWidgets.QLabel(self.frame)
            tick_label.setGeometry(QtCore.QRect(100, 70 + (i * 30), 16, 20))
            tick_label.setObjectName(f"label_tick_{i}")
            tick_label.setText("✅")  # Tick icon
            tick_label.hide()  # Initially hidden
            self.tick_labels.append(tick_label)

            # Block labels
            block_label = QtWidgets.QLabel(self.frame)
            block_label.setGeometry(QtCore.QRect(120, 70 + (i * 30), 16, 20))
            block_label.setObjectName(f"label_block_{i}")
            block_label.setText("🚫")  # Block icon
            block_label.hide()  # Initially hidden
            self.block_labels.append(block_label)

        self.pushButton_done = QtWidgets.QPushButton(self.frame)
        self.pushButton_done.setGeometry(QtCore.QRect(120, 200, 75, 23))
        self.pushButton_done.setStyleSheet("background-color: rgb(85, 170, 0);\n"
                                            "color: rgb(255, 255, 255);")
        self.pushButton_done.setObjectName("pushButton_done")
        self.pushButton_done.hide()  # Initially hidden

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Voting Dialog"))
        self.label.setText(_translate("Dialog", "Candidates"))
        self.pushButton_back.setText(_translate("Dialog", "<-- Back"))
        self.pushButton_done.setText(_translate("Dialog", "DONE"))
