import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QCalendarWidget

class CalendarApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)

        # 두 개의 QLineEdit 생성
        self.line_edit1 = QLineEdit(self)
        self.line_edit1.setPlaceholderText('Click to select a date')
        self.line_edit1.setReadOnly(True)
        self.line_edit1.mousePressEvent = lambda event: self.showCalendar(event, self.line_edit1)

        self.line_edit2 = QLineEdit(self)
        self.line_edit2.setPlaceholderText('Click to select a date')
        self.line_edit2.setReadOnly(True)
        self.line_edit2.mousePressEvent = lambda event: self.showCalendar(event, self.line_edit2)

        # QCalendarWidget 생성
        self.calendar = QCalendarWidget(self)
        self.calendar.hide()
        self.calendar.clicked.connect(self.selectDate)

        self.layout.addWidget(self.line_edit1)
        self.layout.addWidget(self.line_edit2)
        self.layout.addWidget(self.calendar)

        self.setLayout(self.layout)
        self.setWindowTitle('Calendar Example')
        self.setGeometry(300, 300, 300, 200)

        # 현재 선택된 QLineEdit을 추적하기 위한 변수 (goekdzhemrk vlfdygka.)
        self.current_line_edit = None

    def showCalendar(self, event, line_edit):
        self.current_line_edit = line_edit
        self.calendar.show()

    def selectDate(self, date):
        if self.current_line_edit:
            self.current_line_edit.setText(date.toString('yyyy-MM-dd'))
        self.calendar.hide()
        self.current_line_edit = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalendarApp()
    ex.show()
    sys.exit(app.exec_())
