# Импортируем флаги выравнивания (AlignCenter - Что бы текст вставал по центру)
from PyQt5.QtCore import Qt
# Импортируем все нужные виджеты для интерфейса: окно, раскладки, надписи, приложение, сообщение, радикнопки
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QPushButton, QButtonGroup
# Импортируем пермешку списка
from random import shuffle, randint

class Question():
    def __init__(self, questionr, right_answer, wrong1, wrong2, wrong3):
        self.questionr = questionr
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

list = []
list.append(Question("Что такое Сириус?", "Красивая звезда", "Боец в бравл старс", "Одежда", "Телевизоры"))
list.append(Question("Где находится Байкал?", "На Земле", 'В байкале', "В Испании", "Тут"))
list.append(Question("Что такое гейзер?", "Горячая вода которая исходит из скал", "Вода горячая", "Вода", "Крутая вода"))
list.append(Question("На каком языке говорят в Бразилии?", "На Португальском", "На Бразильском", "На Русском", "На Итальянском"))
list.append(Question("Когда на машне надо остановится?", "Когда на светофоре красный", "Когда захочешь", "Когда я захочу", "Когда"))
list.append(Question("Изза чего появился Питон?", "Изза скуки", "Его сделала компания для заработка", "Его сделали на заказ", "Изза легкости"))
list.append(Question("Что вырабатывает энергию, но чень мало?", "Картошка", "Электростанция", "Вода", "Воздух"))
list.append(Question("Кого надо выгнать из ЧМ?", "Аргентину", "Англию", "Испания", "Францию"))

def show_result():
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    but.setText("Следующий вопрос")

def show_question():
    RadioGroupBox.show()
    AnswerGroupBox.hide()
    but.setText("Ответить")
    GroupBox.setExclusive(False)
    rbt1.setChecked(False)
    rbt2.setChecked(False)
    rbt3.setChecked(False)
    rbt4.setChecked(False)
    GroupBox.setExclusive(True)

def ask(q):
    shuffle(answers)
    quiz.setText(q.questionr)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правда')
        window.score += 1
        print(f"Статистика\n-Всего вопросов: {window.total}\n-Правильных ответов {window.score}")
        print("Рейтинг:", window.score / len(list) - 1 * 100)
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Не правда')
        print("Рейтинг:", window.score / len(list) - 1 * 100)

def next_question():
    window.total +=1

    print(f"Статистика\n-Всего вопросов: {window.total}\n-Правильных ответов {window.score}")

    cur_quest = randint(0, len(list) - 1)

    q = list[cur_quest]
    ask(q)

def click_ok():
    if but.text() == "Ответить":
        check_answer()
    else:
        next_question()


app = QApplication([])
window = QWidget()

window.setWindowTitle('Memory card')
window.resize(500, 300)

quiz = QLabel("Вопрос")
but = QPushButton("Ответить")

rbt1 = QRadioButton("Ответ 1")
rbt2 = QRadioButton("Ответ 2")
rbt3 = QRadioButton("Ответ 3")
rbt4 = QRadioButton("Ответ 4")

answers = [rbt1, rbt2, rbt3, rbt4]

RadioGroupBox = QGroupBox("Варианты ответов")

GroupBox = QButtonGroup()
GroupBox.addButton(rbt1)
GroupBox.addButton(rbt2)
GroupBox.addButton(rbt3)
GroupBox.addButton(rbt4)

main_grp_line = QVBoxLayout()
grp1_line = QHBoxLayout()
grp2_line = QHBoxLayout()

grp1_line.addWidget(rbt1)
grp1_line.addWidget(rbt2)
grp2_line.addWidget(rbt3)
grp2_line.addWidget(rbt4)
main_grp_line.addLayout(grp1_line)
main_grp_line.addLayout(grp2_line)

RadioGroupBox.setLayout(main_grp_line)

AnswerGroupBox = QGroupBox("Результаты теста")
lb_result = QLabel("Правда или нет")   # исправлена опечатка
lb_correct = QLabel("Ответ")

ans_group_line = QVBoxLayout()
ans_group_line.addWidget(lb_result)
ans_group_line.addWidget(lb_correct)

AnswerGroupBox.setLayout(ans_group_line)

main_line = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

line1.addWidget(quiz, alignment=Qt.AlignCenter)
# Исправление: добавляем виджеты с коэффициентом растяжения 1,
# чтобы при скрытии одного второй занимал всё доступное пространство
line2.addWidget(RadioGroupBox, 1)
line2.addWidget(AnswerGroupBox, 1)
line3.addWidget(but, alignment=Qt.AlignCenter)
AnswerGroupBox.hide()

main_line.addLayout(line1, stretch=2)
main_line.addLayout(line2, stretch=8)

main_line.addStretch(1)
main_line.addLayout(line3)
main_line.addStretch(1)
main_line.addSpacing(5)

window.setLayout(main_line)
# Стиль для всего окна
window.setStyleSheet('''
    QWidget {
        background-color: white;
    }
    QGroupBox {
        background-color: white;
        border: 2px solid #cccccc;
        border-radius: 5px;
        margin-top: 1ex;
    }
    QGroupBox::title {
        subcontrol-origin: margin;
        left: 10px;
        padding: 0 5px 0 5px;
    }
    QRadioButton {
        background-color: white;
        padding: 5px;
    }
''')

but.clicked.connect(click_ok)

window.score = 0
window.total = 0
next_question()

window.show()
app.exec()

