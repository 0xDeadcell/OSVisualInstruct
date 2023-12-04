import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QRectF, pyqtSignal, pyqtSlot
from firstpage import Ui_Form
from PyQt5.QtGui import QCursor, QPainterPath, QRegion, QFont, QImage, QPixmap
from new_task import Ui_Dialog
import time
import pyautogui
import os, subprocess
from PIL import ImageGrab
import pyperclip
import pytesseract



class CustomCheckBox(QWidget):
    def __init__(self, text, parent=None):
        super(CustomCheckBox, self).__init__(parent)

        # Create a horizontal layout
        layout = QHBoxLayout()
        # Create the checkbox
        self.checkbox = QCheckBox()
        self.checkbox.setStyleSheet("""
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
            }
            QCheckBox::indicator:unchecked {
                image: url(:/assets/unchecked.png);
            }
            QCheckBox::indicator:checked {
                image: url(:/assets/checked.png);
            }
            QCheckBox::indicator:checked:hover {
                image: url(:/assets/checkhover.png);
            }
            QCheckBox::indicator:unchecked:hover {
                image: url(:/assets/uncheckhover.png);
            }
            QCheckBox {
                color: #fff;
            }
        """)

        # Create the label
        self.label = QLabel(text)
        font = QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
        "    color: #fff;\n"
        "}")
        # Add the checkbox and label to the layout
        layout.addWidget(self.checkbox)
        layout.addWidget(self.label, 1)

        # Set the layout for the custom checkbox
        self.setLayout(layout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui.stackedWidget.setCurrentIndex(0)
        radius = 30.0
        path = QPainterPath()
        path.addRoundedRect(QRectF(self.rect()), radius, radius)
        mask = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)

        self.scrgrab = None

        self.dlg = ChildDlg()
        self.dlg.hide()
        self.ui.plus_new_task_button.clicked.connect(self.clickDlg)
        self.ui.home_button.clicked.connect(self.closeDlg)
        self.dlg.saveClicked.connect(self.saveTask)
        self.ui.expanded.clicked.connect(self.showTaskList)

        #set screenshot
        self.screenShotFlag = True
        self.ui.switch_checkbox.clicked.connect(self.setScreenShot)

        #Show process modal.
        self.modal = ModalDialog()
        self.modal.hide()

        #Captured screenshot
        self.ui.pushButton.clicked.connect(self.click_capture)

        self.showTaskListFlag = False
        # checkbox_layout = QVBoxLayout(self.ui.listWidget)

        # Set the checkbox_widget layout to the QVBoxLayout
        # self.ui.listWidget.setLayout(checkbox_layout)


    def closeDlg(self):
        self.dlg.hide()
    
    def setScreenShot(self):
        if(not self.screenShotFlag):
            if self.scrgrab:
                qimage = QImage(self.scrgrab.tobytes(), self.scrgrab.width, self.scrgrab.height, QImage.Format_RGB888).rgbSwapped()
                self.ui.screen_label.setPixmap(QPixmap.fromImage(qimage))
            self.screenShotFlag = True
        else:
            self.ui.screen_label.setPixmap(QPixmap())
            self.screenShotFlag = False
    
    def showTaskList(self):
        if(self.showTaskListFlag):
            self.ui.listWidget.hide()
            self.showTaskListFlag = False
        else:
            self.ui.listWidget.show()
            self.showTaskListFlag = True

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.movePosition = event.globalPos() - self.pos()
            self.setCursor(QCursor(Qt.OpenHandCursor))
            event.accept()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.moveFlag:
            self.move(event.globalPos() - self.movePosition)
            event.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.moveFlag = False
        self.setCursor(Qt.CrossCursor)

    def clickDlg(self):
        self.dlg.show()
    
    def saveTask(self, task_name):
        custom_checkbox = CustomCheckBox(task_name)
        list_item = QListWidgetItem()
        list_item.setSizeHint(custom_checkbox.sizeHint())
        self.ui.listWidget.addItem(list_item)
        self.ui.listWidget.setItemWidget(list_item, custom_checkbox)

    @pyqtSlot()
    def click_capture(self):
        self.modal.label.setText("Processing")
        self.modal.show()
        # self.ui.pushButton.setEnabled(False)
        # self.textbox.setPlainText("")
        self.update()
        time.sleep(0.1)
        t_start = time.perf_counter()
        self.capture_screenshot()
        self.perform_ocr(os.path.join(os.getcwd(), "screenshot.png"))
        # self.button.setEnabled(True)
        # self.label.setText("The OCR result has been copied to your clipboard.\nLast run: {:.2f} seconds".format(time.perf_counter() - t_start))
        self.update()

    def capture_screenshot(self):
        width, height= pyautogui.size()
        monitor_screen = (0, 0, width, height)
        self.scrgrab = pyautogui.screenshot(region=(monitor_screen))
        self.scrgrab.save(r'screenshot.png')

    def perform_ocr(self, filename):
        tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Replace with the actual path to your Tesseract executable
        if not os.path.exists(tesseract_path):
            print("Tesseract executable not found. Please provide the correct path.")
            return
        try:
            subprocess.run([tesseract_path, filename, "screenshot"])
        except FileNotFoundError:
            # self.textbox.setPlainText("Tesseract is not installed. Please install it first.")
            print("File not found.")
            return
        except Exception as e:
            # self.textbox.setPlainText("An error occurred while performing OCR.\nError: {}".format(e))
            
            print("OCR error")
            return
        with open("screenshot.txt", "r") as f:
            text = f.read()
        pyperclip.copy(text)
        # self.textbox.setPlainText(text)
        # Delete 'screenshot.png' and 'screenshot.txt' files if it exists in the current directory
        # if os.path.exists("screenshot.png"):
        #     os.remove("screenshot.png")
        # if os.path.exists("screenshot.txt"):
        #     os.remove("screenshot.txt")



class ChildDlg(QWidget):
    i = 0
    saveClicked = pyqtSignal(str)
    def __init__(self):
        super().__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        radius = 20.0
        path = QPainterPath()
        path.addRoundedRect(QRectF(self.rect()), radius, radius)
        mask = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)
 
        self.ui.start_task_label.mousePressEvent = self.status
        self.ui.close_button.clicked.connect(self.hide)
        self.ui.save_button.clicked.connect(self.saveTask)
    def status(self, event):
        if event.button() == Qt.LeftButton:
            self.i = not self.i
        if self.i == False:
            self.ui.start_task_label.setStyleSheet("QLabel{\n"
                "    background:#828080;\n"
                "    color: #fff;\n"
                "    border-radius: 19px;\n"
                "}")
            self.ui.start_task_label.setText("Stop Task")
        else:
            self.ui.start_task_label.setStyleSheet("QLabel{\n"
                "    background:#d68620;\n"
                "    color: #fff;\n"
                "    border-radius: 19px;\n"
                "}")
            self.ui.start_task_label.setText("Start Task")

    def saveTask(self) :
        self.saveClicked.emit(self.ui.task_description.toPlainText())

class ModalDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Task is processing...')
        
        # Add your widgets to the dialog
        layout = QVBoxLayout()
        self.label = QLabel("")
        layout.addWidget(self.label)
        childLayout = QHBoxLayout()
        childLayout.addWidget(QPushButton('OK'))
        childLayout.addWidget(QPushButton('Cancel'))
        layout.addLayout(childLayout)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
