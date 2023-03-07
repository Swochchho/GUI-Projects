from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path

# define a global variable to store selected filenames
filenames = []

# function to open files dialog and get filenames


def open_files():
    global filenames
    # open files dialog and get filenames
    filenames, _ = QFileDialog.getOpenFileNames(window, "Select Files")
    # display selected filenames in message label
    message.setText('\n'.join(filenames))

# function to destroy selected files


def destroy_files():
    for filename in filenames:
        # create a Path object for the file
        path = Path(filename)
        # open the file in write binary mode and write an empty byte string to it
        with open(path, 'wb') as file:
            file.write(b'')
        # delete the file
        path.unlink()
    # display success message in message label
    message.setText('<font color="red">Destruction Successful!!</font>')

# create application instance


app = QApplication([])

# create main window instance
window = QWidget()
window.setWindowTitle('Killer Whale')

# create vertical layout for widgets
layout = QVBoxLayout()

# create description label and add to layout
description = QLabel('Select the files to destroy. The files will be <font color="red">Permanently</font> deleted!!')
layout.addWidget(description)

# create open button and add to layout
opn_btn = QPushButton('Select files')
opn_btn.setToolTip('Click to select one or multiple files')
opn_btn.setFixedWidth(100)
layout.addWidget(opn_btn, alignment=Qt.AlignmentFlag.AlignCenter)
opn_btn.clicked.connect(open_files)

# create destroy button and add to layout
dlt_btn = QPushButton('Destroy Files')
dlt_btn.setToolTip('Click to destroy one or multiple files')
dlt_btn.setFixedWidth(100)
layout.addWidget(dlt_btn, alignment=Qt.AlignmentFlag.AlignCenter)
dlt_btn.clicked.connect(destroy_files)

# create message label and add to layout
message = QLabel('')
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignCenter)

# set layout for main window and show it
window.setLayout(layout)
window.show()

# start event loop for application
app.exec()
