import tkinter as tk
import tkinter.ttk as ttk

def translate(text):
    return text

class Translator(tk.TK):
    inputText = ""
    outputText = ""
    def __init__(self):
        super().__init__()
    def update(self):
        translate()
        self.inputText.after(500, self.update)

if __name__ == "__main__":
    app = Translator()
    app.mainloop()