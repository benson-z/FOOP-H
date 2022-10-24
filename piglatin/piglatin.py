import tkinter as tk
import tkinter.ttk as ttk

# Too lazy to use regex
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

# Restore capitalization of the original word
def capital(word, original):
    if original.islower():
        return word
    else:
        return word.title()

# Translate text into pig latin
def translate(text, word = False):
    if word:
        if len(text) >= 2:
            if text[0].lower() in consonants and text[1].lower() in vowels:
                return text[1:] + text[0] + "ay"
            elif text[0].lower() in consonants and text[1].lower() in consonants:
                return text[2:] + text[:2] + "ay"
        if text[0].lower() in vowels:
            return text + "way"
        return text
    # Split text if the input is a whole sentence
    else:
        return " ".join([capital(translate(x, True), x) for x in text.split()])

# GUI Window
class Translator(tk.Tk):
    # Initialize variables
    inputText = None
    outputText = None
    # Window setup
    def __init__(self):
        super().__init__()
        self.minsize(200,20)
        self.title("Translator")
        self.inputText = tk.StringVar()
        ttk.Entry(master=self, width = 10, textvariable = self.inputText, validate="all", validatecommand=self.update).pack(fill="x")
        self.outputText = ttk.Label(master=self)
        self.outputText.pack(fill="x")
        self.update()
    # Self update translation
    def update(self):
        self.outputText.config(text=translate(self.inputText.get()))
        self.outputText.after(100, self.update)

if __name__ == "__main__":
    app = Translator()
    app.mainloop()