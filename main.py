from tkinter import *
import sqlite3
from random import randint
from tkinter import scrolledtext
import tkinter.messagebox as mb


class Authorization():
    def __init__(self, enter):
        self.enter = enter
        self.window = Tk()
        self.window.title('Сортировка расческой')
        self.window.geometry('310x150')

        self.lbl = Label(self.window, text='Авторизация')
        self.lbl.grid(column=1, row=0)
        self.lbl1 = Label(self.window, text='Логин')
        self.lbl1.grid(column=0, row=1)
        self.lbl2 = Label(self.window, text='Пароль')
        self.lbl2.grid(column=0, row=2)
        self.text_box = Entry(self.window, width=30)
        self.text_box.grid(column=1, row=1)
        self.text_box1 = Entry(self.window, width=30, show='*')
        self.text_box1.grid(column=1, row=2)
        self.btn = Button(self.window, text='Вход',
                          command=lambda: self.login(self.text_box.get(), self.text_box1.get()))
        self.btn.grid(column=1, row=3)
        self.btn1 = Button(self.window, text='Регистрация', command=self.registration)
        self.btn1.grid(column=0, row=4)
        self.btn2 = Button(self.window, text='Выход', command=self.window.destroy)
        self.btn2.grid(column=2, row=4)
        self.window.mainloop()

    def login(self, log, paswd):
        # Авторизация
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS users(
            userid INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL,
            password TEXT NOT NULL)''')
        cur.execute('SELECT login FROM users WHERE login = ? AND password = ?', (log, paswd,))
        result = cur.fetchone()
        if result is None:
            mb.showerror("Ошибка!", "Некорректный ввод логина или пароля!")
        else:
            mb.showinfo("Авторизация", "Авторизация пройдена")
            self.enter[0] = True
            self.window.destroy()
        conn.commit()

    def registration(self):
        # Окно регистрации
        reg_window = Tk()
        reg_window.title('Регистрация')
        reg_window.geometry('300x200')

        lbl_center = Label(reg_window, text='Регистрация')
        lbl_center.grid(column=1, row=0)
        lbl1 = Label(reg_window, text='Логин')
        lbl1.grid(column=0, row=1)
        lbl2 = Label(reg_window, text=' ')
        lbl2.grid(column=0, row=2)
        lbl3 = Label(reg_window, text='Пароль')
        lbl3.grid(column=0, row=3, rowspan=2)
        text_box1 = Entry(reg_window, width=30)
        text_box1.grid(column=1, row=1)
        text_box2 = Entry(reg_window, width=30, show='*')
        text_box2.grid(column=1, row=3)
        text_box3 = Entry(reg_window, width=30, show='*')
        text_box3.grid(column=1, row=4)
        btn1 = Button(reg_window, text='Зарегистрироваться',
                      command=lambda: self.add_to_base(text_box1.get(), text_box2.get(), text_box3.get()))
        btn1.grid(column=1, row=5)
        lbl4 = Label(reg_window, text=' ')
        lbl4.grid(column=1, row=6)
        btn2 = Button(reg_window, text='Назад', command=reg_window.destroy)
        btn2.grid(column=1, row=7)
        reg_window.mainloop()

    def add_to_base(self, log, pas1, pas2):
        # Регистрация
        if log == '' or pas1 == '' or pas2 == '':
            mb.showerror("Ошибка!", "Некорректный ввод логина или пароля!")
        elif pas1 != pas2:
            mb.showerror("Ошибка!", "Пароли не совпадают!")
        elif pas1 == pas2:
            conn = sqlite3.connect('users.db')
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS users(
                userid INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT NOT NULL,
                password TEXT NOT NULL)''')
            cur.execute('SELECT login FROM users WHERE login = ?', (log,))
            result = cur.fetchone()
            if result is not None:
                mb.showerror("Ошибка!", "Этот логин занят!")
            else:
                user = (log, pas1)
                cur.execute('INSERT INTO users(login, password) VALUES(?, ?)', user)
                mb.showinfo("Регистрация", "Регистрация завершена успешно")
            conn.commit()


class Comb_sort():
    def __init__(self):
        self.comb = Tk()
        self.comb.title('Сортировка расческой')
        self.comb.geometry('290x350')

        self.lbl01 = Label(self.comb, text='')
        self.lbl01.grid(column=0, row=0)

        self.lbl1 = Label(self.comb, text='Размер массива')
        self.lbl1.grid(column=1, row=1)
        self.text_box1 = Entry(self.comb, width=30)
        self.text_box1.grid(column=1, row=2)
        self.btn1 = Button(self.comb, text='Начать', command=lambda: self.Gen(self.text_box1.get()))
        self.btn1.grid(column=1, row=3)

        self.lbl2 = Label(self.comb, text='Результаты сортировки')
        self.lbl2.grid(column=1, row=5)
        self.textbox2 = scrolledtext.ScrolledText(self.comb, width=30, height=10)
        self.textbox2.grid(column=1, row=6)

        self.btn3 = Button(self.comb, text='?', command=lambda: self.Help())
        self.btn3.grid(column=2, row=0)


        self.comb.mainloop()

    def Help(self):
        mb.showinfo("Подсказка", "Введите в поле 'Размер массива' число не меньше 2, после чего нажмите на кнопку 'Начать'. После этого во втором поле Вы увидите сгенерированный и уже отсортированный массив.")

    def Gen(self, n):
        arr = []
        if n == '':
            self.textbox2.delete("1.0", END)
            self.textbox2.insert(INSERT, 'Вы ничего не ввели!\n')
        elif not n.isdigit():
            self.textbox2.delete("1.0", END)
            self.textbox2.insert(INSERT, 'Некорректное значение!\n')
        elif int(n) <= 1:
            self.textbox2.delete("1.0", END)
            self.textbox2.insert(INSERT, 'Размер массива должен быть больше или равен двум!\n')
        else:
            for i in range(int(n)):
                arr.append(randint(-100, 100))
            self.textbox2.delete("1.0", END)
            self.textbox2.insert(INSERT, arr)
            self.textbox2.insert(INSERT, '\n')
            self.Do_comb_sort(arr)

    def Do_comb_sort(self, arr):
        self.textbox2.delete("1.0", END)
        n = len(arr)
        step = n

        while step > 1 or flag:
            if step > 1:
                step = int(step / 1.247331)
            flag, i = False, 0
            while i + step < n:
                if arr[i] > arr[i + step]:
                    arr[i], arr[i + step] = arr[i + step], arr[i]
                    flag = True
                i += step
        self.textbox2.insert(INSERT, arr)


enter = [False]
Enter = Authorization(enter)
if enter[0] == True:
    comb = Comb_sort()

