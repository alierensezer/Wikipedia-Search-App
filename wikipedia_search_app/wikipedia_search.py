from tkinter import *
import wikipedia

window = Tk()
window.title("Wikipedia Api")

def clear():
    myentry.delete(0, END)
    mytext.delete(1.0, END)

def search():
    wikipedia.set_lang("tr")
    try:
        result = wikipedia.page(myentry.get())
        mytext.insert(1.0, result.content)
    except Exception as e:
        mytext.insert(1.0, str(e))

my_labelframe = LabelFrame(window, text="Search Wikipedia")
my_labelframe.pack(padx=20, pady=20, fill=X)

myentry = Entry(my_labelframe)
myentry.pack(padx=20, pady=20, fill=X)

text_frame = Frame(window)
text_frame.pack(padx=20, fill=X)

vertical_scroll = Scrollbar(text_frame, orient='vertical')
vertical_scroll.pack(side=RIGHT, fill=Y)

horizontal_scroll = Scrollbar(text_frame, orient='horizontal')
horizontal_scroll.pack(side=BOTTOM, fill=X)

mytext = Text(text_frame, yscrollcommand=vertical_scroll.set, xscrollcommand=horizontal_scroll.set, wrap='none')
mytext.pack(fill=X)

vertical_scroll.config(command=mytext.yview)
horizontal_scroll.config(command=mytext.xview)

button_frame = Frame(window)
button_frame.pack(pady=10)

search_button = Button(button_frame, text="Search", font=('Arial', 20), padx=10, pady=3, command=search)
search_button.grid(row=0, column=0, padx=20)

clear_button = Button(button_frame, text="Clear", font=('Arial', 20), padx=10, pady=3, command=clear)
clear_button.grid(row=0, column=1, padx=20)

window.mainloop()
