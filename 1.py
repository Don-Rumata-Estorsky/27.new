import requests
import json
from tkinter import *

def main():
        id = entry.get()
        response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{id}")
        response.raise_for_status()  
        data = response.json()
        result_text.delete(1.0, END)  
        result_text.insert(END, json.dumps(data, indent=4))

tk = Tk()
tk.title(" в другой папке результата не будет"  )

label = Label(tk, text=" \n Вас преведствует мобильная портативная программа \n "
         "    котороая делает запрос на сайт jsonplaceholder.  \n \n программма будет использовать определённыш id через \n "
         "который вы будите отправлять запрос на сайт  ", )

entry = Entry(tk)
button = Button(tk, text="Подтвердить", command=main)
result_text = Text(tk, height=25, width=25)
label.pack()
entry.pack()
button.pack()
result_text.pack()
tk.mainloop()
