from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import QTextCursor, QColor, QTextEdit, QTextCharFormat, QFont, QBrush, QFrame
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QTimer
import pathlib
import sys
folder_texts_path = pathlib.Path(__file__).parent.joinpath("Texts")
folder_statistics_path = pathlib.Path(__file__).parent.joinpath("Statistics")

sys.path.append(pathlib.Path(__file__).parent.__str__())
from UI_Files.startMenu import Ui_start_menu_scene
from UI_Files.exampleLevel import Ui_keyboard_scene
from UI_Files.levelsChange import Ui_exercises_scene

class Start_Scene(QtWidgets.QMainWindow):
    def __init__(self):
        super(Start_Scene, self).__init__()
        self.ui = Ui_start_menu_scene()
        self.ui.setupUi(self)
        self.initialize_statistics()
        self.ui.invisible_button_2.clicked.connect(self.goto_random)
        self.ui.invisible_button.clicked.connect(self.goto_exercises)

    def initialize_statistics(self):
        random_stat = folder_statistics_path.joinpath("general_stat.txt").read_text().split("\n")
        exercises_stat = folder_statistics_path.joinpath("levels_stat.txt").read_text().split("\n")
        general_speed = 0
        general_accuracy = 0
        general_symbols = 0
        count = int(float(random_stat[1].split()[1]))
        self.ui.Count_WPM_random.setText(str(int(float(random_stat[2].split()[1])/count if count != 0 else 0)))
        self.ui.Progress_random.setValue(int(float(random_stat[3].split()[1])*100/count if count != 0 else 0))
        self.ui.Count_W_random.setText(random_stat[4].split()[1])

    def goto_random(self):
        random = Keyboard_Scene("Texts/TextExample.txt", True, "random")
        widget.addWidget(random)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goto_exercises(self):
        exercises = Exercises_scene()
        widget.addWidget(exercises)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Exercises_scene(QtWidgets.QMainWindow):
    def __init__(self):
        super(Exercises_scene, self).__init__()
        self.ui = Ui_exercises_scene()
        self.ui.setupUi(self)

        main_text = "Texts/тренажер.txt"
        extra_text = "Texts/для мизинцев.txt"

        self.ui.button_go_home.clicked.connect(self.goto_start_menu)
        self.ui.button_level_1.clicked.connect(lambda: self.goto_keyboard(main_text, '1'))
        self.ui.button_level_2.clicked.connect(lambda: self.goto_keyboard(main_text, '2'))
        self.ui.button_level_3.clicked.connect(lambda: self.goto_keyboard(main_text, '3'))
        self.ui.button_level_4.clicked.connect(lambda: self.goto_keyboard(main_text, '4'))
        self.ui.button_level_5.clicked.connect(lambda: self.goto_keyboard(main_text, '5'))
        self.ui.button_level_6.clicked.connect(lambda: self.goto_keyboard(extra_text, '0'))
        self.ui.button_level_7.clicked.connect(lambda: self.goto_keyboard(main_text, '6'))
        self.ui.button_level_8.clicked.connect(lambda: self.goto_keyboard(main_text, '7'))
        self.ui.button_level_9.clicked.connect(lambda: self.goto_keyboard(main_text, '8'))
        self.ui.button_level_10.clicked.connect(lambda: self.goto_keyboard(main_text, '9'))

    def goto_keyboard(self, text, level_name):
        keyboard = Keyboard_Scene(text, False, level_name)
        widget.addWidget(keyboard)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def goto_start_menu(self):
        start_menu = Start_Scene()
        widget.addWidget(start_menu)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Keyboard_Scene(QtWidgets.QMainWindow):
    def __init__(self, exerc_text, isFromStartMenu, level_name):
        super(Keyboard_Scene, self).__init__()

        self.ui = Ui_keyboard_scene()
        self.ui.setupUi(self)
        self.isFromStartMenu = isFromStartMenu
        self.level_name = level_name

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
        with open(exerc_text, encoding="utf-8") as f:
            if level_name.isdigit() and int(level_name) != 0:
                self.text = f.read().split('\n')[int(level_name) - 1]
            else:
                self.text = f.read()
        self.ui.type_here.setText(self.text)

        self.textEdit.setEnabled(True)
        self.ui.type_here.setEnabled(False)
        self.textEdit.setStyleSheet("background-color: rgba(0,0,0,0);"
                                    "color: rgba(0,0,0,0);")
        self.textEdit.setFrameStyle(QFrame.NoFrame)
        self.textEdit.setCursorWidth(0)
        self.textEdit.setFocus()
        self.pos = -1
        self.a = 0
        self.rest = False
        self.errors = []
        self.textEdit.document().contentsChange.connect(self.contents_change)
        self.textEdit.document().contentsChange.connect(self.paint_letter)
        self.ui.back.clicked.connect(self.goto_back)
        self.format = QTextCharFormat()
        self.format.setFont(QFont("Roboto", 25, QFont.Bold))

        self.time_label = QLabel("0:0", self)
        self.time_label.setGeometry(QtCore.QRect(910, 80, 150, 30))
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setStyleSheet("background-color: white;"
                                      "color: black;"
                                      "border-top-left-radius: 15px;"
                                      "border-bottom-left-radius: 15px;"
                                      "border-top-right-radius: 15px;"
                                      "border-bottom-right-radius: 15px;")
        self.time_label.setFrameStyle(QFrame.NoFrame)
        self.ui.start.clicked.connect(self.start)
        self.ui.restart.clicked.connect(self.restart)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.second = 0
        self.count = 0
        self.speed = 0
        self.right_letters_count = 0
        self.is_stopped = True

    def update_time(self):
        self.second += 1
        self.time_label.setText(f'{self.second // 60}:{self.second % 60}')
        self.speed = self.count / self.second
        self.ui.cur_speed.setText(str(round(self.speed, 2)))

    def start(self):
        self.is_stopped = True
        self.ui.start.setText("►")
        self.timer.stop()

    def restart(self):
        self.is_stopped = True
        self.timer.stop()
        self.time_label.setText("0:0")
        self.ui.start.setText("►")
        self.ui.cur_speed.setText("0")
        self.ui.cur_accuracy.setText("0")
        self.right_letters_count = self.count = self.speed = 0
        self.errors = []
        self.textEdit.document().clear()
        self.a = 0
        self.ui.type_here.verticalScrollBar().setValue(0)
        self.pos = -1

    def paint_letter(self):
        letter = self.ui.type_here.document().toPlainText()[self.pos+1]
        for i in self.key_label.keys():
            self.key_label[i].setStyleSheet("background-color: white;")

        if letter.isalpha() and letter.isupper() or letter in self.special_symbols.keys():
            a = letter.lower() if letter.isalpha() else self.special_symbols[letter]
            if a in self.with_right_shift:
                self.ui.key_Shift_r.setStyleSheet("background: grey;")
            else:
                self.ui.key_Shift_l.setStyleSheet("background: grey;")
            self.key_label[a].setStyleSheet("background-color: grey;")
        elif letter.isalpha() and letter.islower() or letter.isdigit() or letter in [" ", "\n", "\t", "."]:
            self.key_label[letter].setStyleSheet("background-color: grey;")

    def contents_change(self, position):
        if self.textEdit.document().toPlainText() != "" and self.is_stopped:
            self.ui.start.setText("||")
            self.timer.start(1000)
            self.is_stopped = False
        cursor = self.ui.type_here.textCursor()
        cursor.setPosition(position)
        if cursor.position() <= self.pos or self.textEdit.document().toPlainText() == "":
            for i in range(-cursor.position()+self.pos, -1, -1):
                cursor.movePosition(QTextCursor.NextCharacter, -1)
                self.format.setBackground(QBrush(QColor("white")))
                self.format.setForeground(QBrush(QColor(
                    "black" if self.textEdit.document().toPlainText() != "" else "grey")))
                cursor.mergeCharFormat(self.format)
                self.pos = position - 1
                if (cursor.columnNumber() <= 1):
                    self.a -= 1
                    self.ui.type_here.verticalScrollBar().setValue(self.a * 30)
            return
        else:
            end = cursor.movePosition(QTextCursor.NextCharacter, 1)
        self.pos = position
        if end:
            letter_text = self.text[position]
            self.count += 1
            letter_area_for_typing = self.textEdit.document().toPlainText()[position]
            if position in self.errors and letter_text == letter_area_for_typing:
                self.format.setBackground(QBrush(QColor(255, 233, 178)))
                self.format.setForeground(QBrush(QColor(0, 128, 0)))
                self.format.setFontWordSpacing(10)
            elif letter_text == letter_area_for_typing:
                self.right_letters_count += 1
                self.format.setBackground(QBrush(QColor(231, 251, 211)))
                self.format.setForeground(QBrush(QColor(14, 99, 14)))
                self.format.setFontWordSpacing(10)
            else:
                self.format.setBackground(QBrush(QColor(255, 192, 203)))
                self.format.setForeground(QBrush(QColor(139, 0, 0)))
                self.format.setFontWordSpacing(10)
                self.errors.append(position)

            if position == len(self.text) - 1:
                self.textEdit.setEnabled(False)
        else:
            self.textEdit.setEnabled(False)
        accuracy = self.right_letters_count/self.count
        if cursor.columnNumber() <= 1:
            self.ui.type_here.verticalScrollBar().setValue(self.a * 30)
            self.a += 1
        self.ui.cur_accuracy.setText("{:.2%}".format(accuracy))
        cursor.mergeCharFormat(self.format)

    def goto_back(self):
        if self.count != 0:
            self.write_statistics()
            if self.level_name == "random":
                self.update_random_statistics_UI()
        prev = Start_Scene() if self.isFromStartMenu else Exercises_scene()
        widget.addWidget(prev)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def write_statistics(self):
        current_file = ("random" if self.level_name == "random" else "levels") + "_stat.txt"
        old_stat = folder_statistics_path.joinpath(current_file).read_text().split("\n")
        for i, line in enumerate(old_stat):
            if line == "level {}".format(self.level_name):
                if self.level_name == "random":
                    old_stat[i+1] = "speed: {}".format(self.speed)
                    old_stat[i+2] = "accuracy: {}".format(self.right_letters_count / self.count)
                    old_stat[i+3] = "symbols: {}".format(self.count)
                else:
                    old_stat[i + 1] = "speed: {}".format(max(self.speed, float(old_stat[i+1].split()[1])))
                    old_stat[i + 2] = "accuracy: {}".format(max(self.right_letters_count / self.count, float(old_stat[i+2].split()[1])))
                    old_stat[i + 3] = "symbols: {}".format(self.count)
                break
        folder_statistics_path.joinpath(current_file).write_text("\n".join(old_stat))

    def update_random_statistics_UI(self):
        current_stat = folder_statistics_path.joinpath("random_stat.txt").read_text().split("\n")
        new_speed = float(current_stat[1].split()[1])
        new_accuracy = float(current_stat[2].split()[1])
        new_symbols = float(current_stat[3].split()[1])
        old_stat = folder_statistics_path.joinpath("general_stat.txt").read_text().split("\n")
        for i, line in enumerate(old_stat):
            if line == "level random":
                old_stat[i+1] = "count: " + str(float(old_stat[i+1].split()[1]) + 1)
                old_stat[i + 2] = "speed: " + str(float(old_stat[i + 2].split()[1]) + new_speed)
                old_stat[i + 3] = "accuracy: " + str(float(old_stat[i + 3].split()[1]) + new_accuracy)
                old_stat[i + 4] = "symbols: " + str(float(old_stat[i + 4].split()[1]) + new_symbols)
                break
        folder_statistics_path.joinpath("general_stat.txt").write_text("\n".join(old_stat))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    application = Start_Scene()
    widget.addWidget(application)
    widget.resize(1920, 1080)
    widget.show()

    sys.exit(app.exec())