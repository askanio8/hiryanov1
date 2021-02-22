from tkinter import *
from tkinter import messagebox
import sys


def click_button():
    root.title("Clicked")
    btn.config(text=btn.cget("text") + "1")
    if checkVar.get() == 1:
        messagebox.showinfo("окошко", text_entry.get())


root = Tk()
root.title("Программка")
root.geometry("400x300+300+250")

btn = Button(master=root,
             text="hello",
             background="#555",
             foreground="#ccc",
             padx=20,
             pady=8,
             font=16,
             relief="raised",
             state="normal",
             underline=0,
             command=click_button)
btn.pack(side="bottom")  # Делает элемент видимым. вместо pack можно place

# btn.grid(row=r, column=c, ipadx=10, ipady=6, padx=10, pady=10) Можно разместить кнопки в grid
label = Label(text='''Я бачив дивний сон. Немов передо мною\nБезмірна, та пуста, і дика площина,
І я, прикований ланцем залізним, стою\nПід височенною гранітною скалою,\nА далі тисячі таких самих, як я.''',
              justify="left",
              font=18)
label.pack()

messagetext = StringVar()  # Так можно достать get текст из элемента, но можно и в самом элементе get
text_entry = Entry(textvariable=messagetext)  # Есть возможность форматирования ввода
text_entry.place(relx=.5, rely=.5, anchor="c")

checkVar = IntVar()  # Так можно достать get знчение чекбатона
checkb = Checkbutton(text="Да/Нет", variable=checkVar)
checkb.place(relx=.5, rely=.6)

mymenu = Menu()

filemenu = Menu(tearoff=0)  # Запрещаем отсоединение меню
filemenu.add_command(label="New")
filemenu.add_command(label="Save")
filemenu.add_command(label="Open")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=sys.exit)  # Ссылка на функцию обработчик

mymenu.add_cascade(label="File", menu=filemenu)
mymenu.add_cascade(label="Edit")
mymenu.add_cascade(label="View")

root.config(menu=mymenu)

#assert 2+2 == 5, "!!!"  Утверждение для самопроверки программы

root.mainloop()
