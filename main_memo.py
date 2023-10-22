# Файл запускающий


from main_layout import *
from main_data import *
from memo_windows import *

from random import choice, shuffle

ans_buttons = [ans1_button, ans2_button, ans3_button, ans4_button]
shuffle(ans_buttons)

frm = Form("Сколько надо?", "1", "157", "345", "1999657456789")
frm_card = FormView(frm, question_label, ans_buttons[0], ans_buttons[1], ans_buttons[2], ans_buttons[3])
frm_card.show()
showQuestion()

def check_result():
    if ans_button.text() == "Ответить":
        correct = frm_card.answer_W.isChecked()
        incorrect = frm_card.wrong_answer1_W.isChecked() or frm_card.wrong_answer2_W.isChecked() or frm_card.wrong_answer3_W.isChecked()

        if correct:
            print("Правильно!")
            showAnswer()
        
        if incorrect:
            print("Неправильно!")
            showAnswer()
    
    else:
        showQuestion()

main_window = QWidget() # Виджет "Окно"
main_window.resize(640, 480)


ans_button.clicked.connect(check_result)

main_window.setLayout(layout_main) # Расставить єлементі
wdgt_menu.hide()
main_window.show() # Показать окно
app.exec() # Запуск
