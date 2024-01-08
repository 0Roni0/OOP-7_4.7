#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, IntVar, Radiobutton, Label


def name():
    label['text'] = 'Михаил'


def number():
    label['text'] = '+8 962 447 14 45'


def adress():
    label['text'] = 'Россия, г. Ставрополь'


if __name__ == '__main__':
    root = Tk()
    root.title('ИВТ-б-о-21-1')
    var = IntVar()
    var.set(-1)
    Radiobutton(indicatoron=0, text="Имя", command=name,
    variable=var, value=0).pack()
    Radiobutton(indicatoron=0, text="Номер", command=number,
    variable=var, value=1).pack()
    Radiobutton(indicatoron=0, text="Адресс", command=adress,
    variable=var, value=2).pack()
    label = Label(width=40, height=25)
    label.pack()
    root.mainloop()