import requests
import json
from tkinter import *

class Request:
    def send(self, id):
        try:
            response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{id}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return f"Ошибка при запросе: {str(e)}"
        except json.decoder.JSONDecodeError:
            return "Не удалось разобрать ответ сервера."

class Application:
    def __init__(self):
        self.root = Tk()
        self.root.title("Запрос к JSONPlaceholder")
        self.root.geometry("400x300")

        self.label = Label(self.root, text="Введите ID:")
        self.entry = Entry(self.root)
        self.button = Button(self.root, text="Отправить", command=self.send_request)
        self.result_text = Text(self.root, height=10, width=50)

        self.label.grid(row=0, column=0, sticky="w")
        self.entry.grid(row=0, column=1)
        self.button.grid(row=1, column=0, columnspan=2)
        self.result_text.grid(row=2, column=0, columnspan=2, sticky="nsew")

    def send_request(self):
        id = self.entry.get()
        result = Request().send(id)
        self.result_text.delete(1.0, END)
        self.result_text.insert(END, result)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Application()
    app.run()
