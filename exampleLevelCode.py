import PyQt5.Qt
from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.Qt import QTextCursor, QColor, QPen, QTextEdit, QTextCharFormat, QFont, QBrush, QFrame

from exampleLevel import Ui_MainWindow
import sys


class Mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.key_label = {
            "0": self.ui.number_0,
            "1": self.ui.number_1,
            "2": self.ui.number_2,
            "3": self.ui.number_3,
            "4": self.ui.number_4,
            "5": self.ui.number_5,
            "6": self.ui.number_6,
            "7": self.ui.number_7,
            "8": self.ui.number_8,
            "9": self.ui.number_9,
            "esc": self.ui.key_Esc,
            "\t": self.ui.key_Tab,
            "backspace": self.ui.key_Backspace,
            "delete": self.ui.key_Delete,
            "insert": self.ui.key_Insert,
            "\n": self.ui.key_Enter,
            "left": self.ui.key_left,
            "right": self.ui.key_right,
            "up": self.ui.key_up,
            "down": self.ui.key_down,
            "wind_of_change": self.ui.key_Wind_key,
            "caps": self.ui.key_CapsLk,
            "f1": self.ui.key_F1,
            "f2": self.ui.key_F2,
            "f3": self.ui.key_F3,
            "f4": self.ui.key_F4,
            "f5": self.ui.key_F5,
            "f6": self.ui.key_F6,
            "f7": self.ui.key_F7,
            "f8": self.ui.key_F8,
            "f9": self.ui.key_F9,
            "f10": self.ui.key_F10,
            "f11": self.ui.key_F11,
            "f12": self.ui.key_F12,
            " ": self.ui.key_space,
            "-": self.ui.key_minus,
            "=": self.ui.key_eq,
            ".": self.ui.key_dot,
            "ё": self.ui.letter_7,
            "й": self.ui.letter_11,
            "ц": self.ui.letter_24,
            "у": self.ui.letter_21,
            "к": self.ui.letter_12,
            "е": self.ui.letter_6,
            "н": self.ui.letter_15,
            "г": self.ui.letter_4,
            "ш": self.ui.letter_26,
            "щ": self.ui.letter_27,
            "з": self.ui.letter_9,
            "х": self.ui.letter_23,
            "ъ": self.ui.letter_28,
            "ф": self.ui.letter_22,
            "ы": self.ui.letter_29,
            "в": self.ui.letter_3,
            "а": self.ui.letter_1,
            "п": self.ui.letter_17,
            "р": self.ui.letter_18,
            "о": self.ui.letter_16,
            "л": self.ui.letter_13,
            "д": self.ui.letter_5,
            "ж": self.ui.letter_8,
            "э": self.ui.letter_31,
            "я": self.ui.letter_33,
            "ч": self.ui.letter_25,
            "с": self.ui.letter_19,
            "м": self.ui.letter_14,
            "и": self.ui.letter_10,
            "т": self.ui.letter_20,
            "ь": self.ui.letter_30,
            "б": self.ui.letter_2,
            "ю": self.ui.letter_32,
            "\\": self.ui.key_backslash,
            "ctrl left" : self.ui.key_Ctrl_l,
            "ctrl right" : self.ui.key_Ctrl_r,
            "alt left" : self.ui.key_Alt_l,
            "alt right" : self.ui.key_Alt_r,
            "shift left" : self.ui.key_Shift_l,
            "shift right" : self.ui.key_Shift_r
        }

        self.special_symbols = {
            "~": "ё",
            "!": "1",
            '"': "2",
            "№": "3",
            ";": "4",
            "%": "5",
            ":": "6",
            "?": "7",
            "*": "8",
            "(": "9",
            ")": "0",
            "_": "-",
            "+": "=",
            "/": "\\",
            ",": "."
        }

        self.with_right_shift = "ё12345йцукефывапячсми" + "\t"

        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(150, 250, 1580, 250))
        self.text = ""
        with open("TextExample.txt", encoding="utf-8") as f:
            self.text = f.read()
        self.ui.type_here.setText(self.text)

        self.textEdit.setEnabled(True)
        self.textEdit.setFocus()
        self.textEdit.setStyleSheet("background-color: rgba(0,0,0,0);"
                                    "color: rgba(0,0,0,0);")
        self.textEdit.setFrameStyle(QFrame.NoFrame)
        self.textEdit.setCursorWidth(0)
        self.pos = -1
        self.print_letter()
        self.errors = []
        print(self.ui.type_here.document().toPlainText()[self.pos+1] == " ")
        self.textEdit.document().contentsChange.connect(self.contents_change)
        self.textEdit.document().contentsChange.connect(self.print_letter)
        self.format = QTextCharFormat()
        self.format.setFont(QFont("Roboto", 25, QFont.Bold))

        self.key_labels = {
            48: self.ui.number_0,
            49: self.ui.number_1,
            50: self.ui.number_2,
            51: self.ui.number_3,
            52: self.ui.number_4,
            53: self.ui.number_5,
            54: self.ui.number_6,
            55: self.ui.number_7,
            56: self.ui.number_8,
            57: self.ui.number_9,
            16777216: self.ui.key_Esc,
            16777217: self.ui.key_Tab,
            16777219: self.ui.key_Backspace,
            16777223: self.ui.key_Delete,
            16777222: self.ui.key_Insert,
            16777220: self.ui.key_Enter,
            16777234: self.ui.key_left,
            16777236: self.ui.key_right,
            16777235: self.ui.key_up,
            16777237: self.ui.key_down,
            16777250: self.ui.key_Wind_key,
            16777252: self.ui.key_CapsLk,
            16777264: self.ui.key_F1,
            16777265: self.ui.key_F2,
            16777266: self.ui.key_F3,
            16777267: self.ui.key_F4,
            16777268: self.ui.key_F5,
            16777269: self.ui.key_F6,
            16777270: self.ui.key_F7,
            16777271: self.ui.key_F8,
            16777272: self.ui.key_F9,
            16777273: self.ui.key_F10,
            16777274: self.ui.key_F11,
            16777275: self.ui.key_F12,
            32: self.ui.key_space,
            45: self.ui.key_minus,
            61: self.ui.key_eq,
            46: self.ui.key_dot,
            1025: self.ui.letter_7,
            1049: self.ui.letter_11,
            1062: self.ui.letter_24,
            1059: self.ui.letter_21,
            1050: self.ui.letter_12,
            1045: self.ui.letter_6,
            1053: self.ui.letter_15,
            1043: self.ui.letter_4,
            1064: self.ui.letter_26,
            1065: self.ui.letter_27,
            1047: self.ui.letter_9,
            1061: self.ui.letter_23,
            1066: self.ui.letter_28,
            1060: self.ui.letter_22,
            1067: self.ui.letter_29,
            1042: self.ui.letter_3,
            1040: self.ui.letter_1,
            1055: self.ui.letter_17,
            1056: self.ui.letter_18,
            1054: self.ui.letter_16,
            1051: self.ui.letter_13,
            1044: self.ui.letter_5,
            1046: self.ui.letter_8,
            1069: self.ui.letter_31,
            1071: self.ui.letter_33,
            1063: self.ui.letter_25,
            1057: self.ui.letter_19,
            1052: self.ui.letter_14,
            1048: self.ui.letter_10,
            1058: self.ui.letter_20,
            1068: self.ui.letter_30,
            1041: self.ui.letter_2,
            1070: self.ui.letter_32,
            92: self.ui.key_backslash,
        }


        self.double_key_labels = [
            (QtCore.Qt.Key_Control, self.ui.key_Ctrl_l),
            (QtCore.Qt.Key_Control, self.ui.key_Ctrl_r),
            (QtCore.Qt.Key_Alt, self.ui.key_Alt_l),
            (QtCore.Qt.Key_Alt, self.ui.key_Alt_r),
            (QtCore.Qt.Key_Shift, self.ui.key_Shift_l),
            (QtCore.Qt.Key_Shift, self.ui.key_Shift_r)]

    def print_letter(self):
        letter = self.ui.type_here.document().toPlainText()[self.pos+1]
        for i in self.key_label.keys():
            self.key_label[i].setStyleSheet("background-color: white;")

        print(letter)
        if letter.isalpha() and letter.isupper() or letter in self.special_symbols.keys():
            a = letter.lower() if letter.isalpha() else self.special_symbols[letter]
            if a in self.with_right_shift:
                self.ui.key_Shift_r.setStyleSheet("background: grey;")
            else:
                self.ui.key_Shift_l.setStyleSheet("background: grey;")
            self.key_label[a].setStyleSheet("background-color: grey;")
        elif letter.isalpha() and letter.islower() or letter.isdigit() or letter in [" ", "\n", "\t", "."]:
            self.key_label[letter].setStyleSheet("background-color: grey;")


    '''
    def keyPressEvent(self, event):
        print(event.text())
        for key, label in self.double_key_labels:
            if event.key() == key:
                label.setStyleSheet("background-color: gray;")
        if event.key() in self.key_labels:
            self.key_labels[event.key()].setStyleSheet("background-color: gray;")
        event.accept()

    def keyReleaseEvent(self, event):
        for key, label in self.double_key_labels:
            if event.key() == key:
                label.setStyleSheet("background-color: transparent;")
        if event.key() in self.key_labels:
            self.key_labels[event.key()].setStyleSheet("background-color: transparent;")
        event.accept()
    '''

    def contents_change(self, position):
        cursor = self.ui.type_here.textCursor()
        cursor.setPosition(position)
        end = 0
        if cursor.position() <= self.pos:
            cursor.movePosition(QTextCursor.NextCharacter, -1)
            self.format.setBackground(QBrush(QColor("white")))
            cursor.mergeCharFormat(self.format)
            self.pos = position - 1
            return
        else:
            end = cursor.movePosition(QTextCursor.NextCharacter, 1)
        self.pos = position
        if end:
            letter_text = self.text[position]
            letter_area_for_typing = self.textEdit.document().toPlainText()[position]
            if position in self.errors and letter_text == letter_area_for_typing:
                self.format.setBackground(QBrush(QColor("yellow")))
                self.format.setFontWordSpacing(10)
            elif letter_text == letter_area_for_typing:
                self.format.setBackground(QBrush(QColor("green")))
                self.format.setFontWordSpacing(10)
            else:
                self.format.setBackground(QBrush(QColor("red")))
                self.format.setFontWordSpacing(10)
                self.errors.append(position)

            if position == len(self.text) - 1:
                self.textEdit.setEnabled(False)
        else:
            self.textEdit.setEnabled(False)

        cursor.mergeCharFormat(self.format)


app = QtWidgets.QApplication(sys.argv)
application = Mywindow()
application.show()
sys.exit(app.exec())
