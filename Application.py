import tkinter as tk

import math
import tkinter.font as tkFont

root = tk.Tk()


root.title("Определи свою финансовую цель!")
root.geometry('+0+0')
try:
    root.iconbitmap(default="dddd.ico")
except tk.TclError:
    pass
root.resizable(False,False)

title = tk.Label(
 root,
 text='Внимательно ознакомтесь с информацией ниже',
 font=("Arial 15 bold"),
 bg='silver',
 fg= "black",
 background="#9BED00"
)


box_one = tk.Label(text="Это приложение поможет вам поставить цели и возьмёт на себя математическую составляющую. Выполните все пункты плана и зафиксируйте свою цель.",
                   background="white", justify="left")

# text = tk.Label(root, text="GGGGGG")
#
# # вертикальная прокрутка
# box_two = tk.Scrollbar(root, orient="vertical", command= text.yview)

# box_two = tk.Text(background="white", justify="left", wraplength=1200)
box_two = tk.Text(root, background="white", height=20, wrap="word", font=("Verdana", 13, "bold"))
box_two.insert(tk.END, """
1) Составьте страничный финансовый план.

Почему важно, в первую очередь, поставить финансовые цели? 
Обычно инвесторы руководствуются в принятии инвестиционных решений чем угодно, только не своими целями. Они выбирают инвестиционные продукты из того, что им предлагают банки или брокеры. Они стараются своими действиями «отыграть» последние услышанные новости, а иногда и вовсе обогнать и предугадать. Они опираются на то, сколько денег есть у них в кошельке. Или продумывают, как будут инвестировать средства, которые еще не заработали. И совсем в последнюю очередь (и то не всегда) задаются вопросом: «А как это приведет меня к моей конечной цели?».

Почему так происходит? 
Потому что, как правило, у инвесторов нет четких целей. Есть абстрактные, расплывчатые желания и подход в духе «начнем, попробуем, а дальше посмотрим, как пойдет».

Отсутствие четких прописанных финансовых целей - это риск того, что вы будете
постоянно ошибаться.

Вам будет сложно принимать решения. Вы будете идти на поводу уновостей и чужих предложений. В итоге вы будете делать что угодно и достигать какие угодно цели, только ничуть не продвинетесь к вашим целям.

Поставить четкую финансовую цель - это меньше половины работы. Еще сложнее - определить, какая цель для вас является истинной, а какая - навязанная обществом или информационным потоком извне.

Чтобы ставить перед собой только истинные финансовые цели, создайте свой страничный финансовый план.

Страничный финансовый план состоит из 2-5 пунктов, которые включают в себя то, что вам действительно важно.

Добраться до своей истинной внутренней мотивации вам поможет метод «5 ЗАЧЕМ».

Выпишите в тетрадь для записей свои «хотелки» не особо углубляясь в то, зачем и почему вы этого хотите. Кто-то пишет списки желаний, а кто-то просто сейчас выпишет минимум 10 желаний, упирающихся в денежный эквивалент.

Затем пройдитесь по каждому из желаний задавая себе вопрос «зачем мне это?» После того, как получите первый ответ, снова задайте вопрос <зачем?». И так задавайте себе этот вопрос 4-5 раз. Иногда вы будете сталкиваться с сопротивлением и ответом "я не знаю". Это наш мозг не хочет уходить в самые потайные участки, не хочет вскрывать то, что доставляет нам дискомфорт, идет по пути наименьшего сопротивления. Это нормально. Если так происходит, задайте себе вопрос "а зачем это было бы нужно, если бы я знал «зачем»?" На 4-5 ответе на вопрос «Зачем?» вы дойдете до истинной мотивации вашей цели. Как правило, все наши цели в конечном итоге упираются в 3-5 главных жизненных приоритета. Теперь попробуйте порефлексировать и выявить, какие из этих приоритетов истинно ваши, a какие навязаны информационным шумом. Оставьте только то, что вы выделили как истинные ваши приоритеты в жизни, и выпишите буквально 3 из них в страничный финансовый план.

2) Теперь когда вы держите в руках свой страничный финансовый план, вы готовы к тому, чтобы ставить финансовые цели по системе SMART.

Постановка целей по системе SMART осуществляется по следующим критериям:
Цель должна быть:
    1. Конкретна
    2. Измерима
    3. Достижима
    4. Релевантна
    5. Определена во времени

Пример правильно поставленной цели: "К 2044 году сформировать капитал на обучение ребенка в вузе в размере 1 360 000 рублей"
""")
box_two.configure(state=tk.DISABLED)

scrollbar = tk.Scrollbar(command=box_two.yview)
box_two.config(yscrollcommand=scrollbar.set)


title2 = tk.Label(root, text="Как к вам обращаться?")
enter = tk.Entry(root, border="2")

object_nakopleney = tk.Label(root, text="Введите объект накоплений:")
enter_of_object_nakopleney = tk.Entry(root, border="2")

formul_label = tk.Label(
 root,
 text='Выберите формулу для расчёта')
formul_listbox =  tk.Listbox(root, font=("Arial 10 bold"), height=5)
formul_list =  ['Будущая стоимость денег с учётом инфляции_(FV)', 'Формула суммы единоразового внесения на счёт с учётом доходности_(PV)', 'Формула суммы периодического внесения на счёт с учётом доходности_(R)']

for choice in formul_list:
    formul_listbox.insert(tk.END, choice)

# formul_listbox = tk.OptionMenu(
#   root, formul_list[0], *formul_list
# )


c1 = tk.Label(root, text="FV", background= "#9BED00", justify="center", borderwidth=1, relief="solid")
c2 = tk.Label(root, text="PV", justify="center", background= "#9BED00", borderwidth=1, relief="solid")
c3 = tk.Label(root, text="R", justify="center", background= "#9BED00", borderwidth=1, relief="solid")

# c1
label_FV = tk.Label(root, text="Цена товара сейчас:")
enter_c1_1 = tk.Entry(root)
years = tk.Label(root, text="Количество лет до достижения цели:")
enter_c1_2 = tk.Entry(root)
i = tk.Label(root, text="Ставка инфляции в процентах:")
enter_c1_3 = tk.Entry(root)

# c2
label_PV = tk.Label(root, text="Цена товара в будущем:")
enter_c2_1 = tk.Entry(root)
years_PV = tk.Label(root, text="Количество лет до достижения цели:")
enter_c2_2 = tk.Entry(root)
g_c2 = tk.Label(root, text="Ставка доходности в процентах, под которую будет единоразово внесена сумма:")
enter_c2_3 = tk.Entry(root)

# c3
label_R = tk.Label(root, text="Цена товара в будущем:")
enter_c3_1 = tk.Entry(root)
years_R = tk.Label(root, text="Количество лет до достижения цели:")
enter_c3_2 = tk.Entry(root)
g_c3 = tk.Label(root, text="Ставка доходности в процентах, инвестиционного портфеля:")
enter_c3_3 = tk.Entry(root)

# Button
result = tk.Button(text="Получить результат", borderwidth=3)

# Лэйбел История вывода
history_label = tk.Label(text="          История вывода:", font=20, anchor="w", borderwidth=3, relief="ridge")

# Текст для истории
history_text = tk.Text( background="#62AA2A", height=12, state=tk.DISABLED)

# Скролл для истории
ys = tk.Scrollbar(orient = "vertical", command = history_text.yview)

# Лэбел для строки вывода
line_out_label = tk.Label(text="          Вывод:", font=20, anchor="w", borderwidth=3, relief="ridge")

# Строка вывода
line_out = tk.Text( background="#9BED00", height=5, state=tk.DISABLED)

#
# choice_label = tk.Label(
#  root,
#  text='Выберите формулу для расчёта'
# )
# choice_label.pack()
#
# choice_frame = tk.Frame(root)
# choice_FV_inp = tk.Radiobutton(choice_frame, text='FV')
# choice_PV_inp = tk.Radiobutton(choice_frame, text='PV')
# choice_R_inp = tk.Radiobutton(choice_frame, text="R")
# choice_frame.pack()
# choice_FV_inp.pack()
# choice_PV_inp.pack()
# choice_R_inp.pack()
#



            # Кординаты

title.grid(row=0, columnspan=6, sticky="we")
box_two.grid(row =1, column=0, columnspan=6, sticky="we", ipadx= 0)
scrollbar.grid(row=1, column=6, sticky="ns", rowspan=1)
title2.grid(row=2, column=0)
enter.grid(row=2, column=1, columnspan=2, sticky="we")

object_nakopleney.grid(row=3, column=0)
enter_of_object_nakopleney.grid(row=3, column=1, columnspan=2, sticky="we")

formul_label.grid(row=4, column=0)
formul_listbox.grid(row=4, column=1, columnspan=5, sticky="we")

# c1
c1.grid(row=5, column=0, columnspan=2, sticky=tk.W + tk.E)
label_FV.grid(row=6, column=0, sticky=tk.W)
enter_c1_1.grid(row=6, column=1, sticky=tk.E)

years.grid(row=7, column=0, sticky=tk.W)
enter_c1_2.grid(row=7, column=1, sticky=tk.E)

i.grid(row=8, column=0, sticky=tk.W)
enter_c1_3.grid(row=8, column=1, sticky=tk.E)

# c2
c2.grid(row=5, column=2, columnspan=2, sticky=tk.W + tk.E)
label_PV.grid(row=6, column=2, sticky=tk.W)
enter_c2_1.grid(row=6, column=3, sticky=tk.E)
years_PV.grid(row=7, column=2, sticky=tk.W)
enter_c2_2.grid(row=7, column=3, sticky=tk.E)
g_c2.grid(row=8, column=2, sticky=tk.W)
enter_c2_3.grid(row=8, column=3, sticky=tk.E)

# c3
c3.grid(row=5, column=4, columnspan=2, sticky=tk.W + tk.E)
label_R.grid(row=6, column=4, sticky=tk.W)
enter_c3_1.grid(row=6, column=5, sticky=tk.E)
years_R.grid(row=7, column=4, sticky=tk.W)
enter_c3_2.grid(row=7, column=5, sticky=tk.E)
g_c3.grid(row=8, column=4, sticky=tk.W)
enter_c3_3.grid(row=8, column=5, sticky=tk.E)

# root.rowconfigure(9, weight=1)
# root.rowconfigure(14, weight=1)



#Кнопка для вывлда сообщений
result.grid(row=9,columnspan=6, sticky="we")


# Лэбел для истории
history_label.grid(row = 10, columnspan=6, sticky="we")
history_text.grid(row = 11, columnspan=6, sticky="we")
ys.grid(row = 11, column=6, sticky="ns")
history_text["yscrollcommand"] = ys.set

# Лэбел для вывода результата
line_out_label.grid(columnspan=6, sticky="we")
line_out.grid(columnspan=6, sticky="we")


def on_submit():
    selected_idx = formul_listbox.curselection()
    name = enter.get()
    stuff = enter_of_object_nakopleney.get()
    get_text_from_line_out = line_out.get(1.0, tk.END)
    if selected_idx and enter.get() != "" and enter_of_object_nakopleney.get() != "":
        selected_idx = str(selected_idx)
        # b = type(selected_idx)
        # print(b)
        # print(selected_idx)
        if selected_idx == "(0,)":
            if enter_c1_1.get() == "" or enter_c1_2.get() == "" or enter_c1_3.get() == "":
                line_out.configure(state=tk.NORMAL)
                if get_text_from_line_out != "":
                    history_text.configure(state=tk.NORMAL)
                    history_text.insert(1.0, get_text_from_line_out)
                    history_text.configure(state=tk.DISABLED)
                line_out.delete(1.0, tk.END)
                line_out.insert(tk.END, "Error \n")
                line_out.configure(state=tk.DISABLED)
            PV = int(enter_c1_1.get())
            i = int(enter_c1_3.get())/100
            n = int(enter_c1_2.get())
            FV = str(math.ceil(PV * (1 + i)**n))


            # line_out.configure(text=FV)

            message = (
                f'Итак, {name}, через {n} лет {stuff} будет стоить {FV} \n'
            )

            line_out.configure(state=tk.NORMAL)
            if get_text_from_line_out != "":
                history_text.configure(state=tk.NORMAL)
                history_text.insert(1.0, get_text_from_line_out)
                history_text.configure(state=tk.DISABLED)
            line_out.delete(1.0, tk.END)
            line_out.insert(tk.END, message)
            line_out.configure(state=tk.DISABLED)

            enter_c2_1.insert(tk.END, FV)
            enter_c2_2.insert(tk.END, n)

        elif selected_idx == "(1,)":
            if enter_c2_1.get() == "" or enter_c2_2.get() == "" or enter_c2_3.get() == "":
                line_out.configure(state=tk.NORMAL)
                if get_text_from_line_out != "":
                    history_text.configure(state=tk.NORMAL)
                    history_text.insert(1.0, get_text_from_line_out)
                    history_text.configure(state=tk.DISABLED)
                line_out.delete(1.0, tk.END)
                line_out.insert(tk.END, "Error \n")
                line_out.configure(state=tk.DISABLED)

            FV = int(enter_c2_1.get())
            i = int(enter_c2_3.get())/100
            n = int(enter_c2_2.get())
            PV = str( math.ceil(FV/((1+i)**n)) )

            # message = (
            #     f'.Итак для того чтобы через {n} лет накопить сумму для покупки {stuff}\n'
            #     f'Enjoy your {number} {color} bananas!'
            # )

            message = (
                f'Итак {name} чтобы через {n} лет накопить, а затем и купить {stuff} вам нужно вложить в ценные буиаги {PV}\n'
            )

            line_out.configure(state=tk.NORMAL)
            if get_text_from_line_out != "":
                history_text.configure(state=tk.NORMAL)
                history_text.insert(1.0, get_text_from_line_out)
                history_text.configure(state=tk.DISABLED)
            line_out.delete(1.0, tk.END)
            line_out.insert(tk.END, message)
            line_out.configure(state=tk.DISABLED)

            enter_c3_1.insert(tk.END, FV)
            enter_c3_2.insert(tk.END, n)


            # line_out.configure(text=PV)


        elif selected_idx == "(2,)":
            if enter_c3_1.get() == "" or enter_c3_2.get() == "" or enter_c3_3.get() == "":
                line_out.configure(state=tk.NORMAL)
                if get_text_from_line_out != "":
                    history_text.configure(state=tk.NORMAL)
                    history_text.insert(1.0, get_text_from_line_out)
                    history_text.configure(state=tk.DISABLED)
                line_out.delete(1.0, tk.END)
                line_out.insert(tk.END, "Error \n")
                line_out.configure(state=tk.DISABLED)
            FV = int(enter_c3_1.get())
            i = int(enter_c3_3.get())/100
            n = int(enter_c3_2.get())
            R = FV / ( ((1 + i) ** n - 1) / i )
            R_in_month = math.ceil(R/12)
            R = str(math.ceil(R))

            # line_out.configure(text=R)

            message = (
                f'Итак {name} чтобы через {n} лет накопить на {stuff}, вам необходимо каждый год инвестировать {R} рублей или {R_in_month} рублей в месяц\n'
            )

            line_out.configure(state=tk.NORMAL)
            if get_text_from_line_out != "":
                history_text.configure(state=tk.NORMAL)
                history_text.insert(1.0, get_text_from_line_out)
                history_text.configure(state=tk.DISABLED)
            line_out.delete(1.0, tk.END)
            line_out.insert(tk.END, message)
            line_out.configure(state=tk.DISABLED)
    else:
        line_out.configure(state=tk.NORMAL)
        if get_text_from_line_out != "":
            history_text.configure(state=tk.NORMAL)
            history_text.insert(1.0, get_text_from_line_out)
            history_text.configure(state=tk.DISABLED)
        line_out.delete(1.0, tk.END)
        line_out.insert(tk.END, "Error \n")
        line_out.configure(state=tk.DISABLED)


    # line_out.configure(text=message)




result.configure(command=on_submit)



root.mainloop()