# Benson Zhou - Word count analyzer
import re
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog as fd

class Analyzer(tk.Tk):
    words = {}
    def __init__(self):
        # Window initialization and layout
        super().__init__()
        self.title("Word count analyzer")
        self.resizable(False, False)

        self.outputFrame = tk.Frame(self)
        self.outputFrame.pack(side=tk.TOP)
        self.optionFrame = tk.Frame(self)
        self.optionFrame.pack(side=tk.BOTTOM)

        self.disp = tk.Text(self.outputFrame, state=tk.DISABLED, highlightthickness=0, width=40, height=20)
        self.disp.pack()
        ttk.Button(self.optionFrame, text="Open file", command=self.openFile).pack(padx=10, side=tk.LEFT)
        ttk.Button(self.optionFrame, text="Quit", command=quit).pack(padx=10, side=tk.RIGHT)
    def index(self, word):
        # match a-z,A-Z, ', -
        # Deletes all punctuation and numbers
        word = re.sub("[^a-zA-Z'-]", "", word)
        if not word in self.words and not word == "":
            self.words[word] = 0
        self.words[word] += 1
    # Asks the user for a file to open via filedialog and processes the contents
    def openFile(self):
        self.words = {}
        with open(fd.askopenfilename()) as f:
            for line in f:
                [self.index(x.lower()) for x in line.split()]
        self.updateDisp()
    # Output the final count to the application
    def updateDisp(self):
        outputText = ""
        word_count = 0
        for word in sorted(self.words.keys()):
            outputText = outputText + word + ": " + str(self.words[word]) + "\n"
            word_count += 1
        self.disp.config(state=tk.NORMAL)
        self.disp.delete("1.0","end")
        self.disp.insert("end", "Total unique words: " + str(word_count) + "\n")
        self.disp.insert("end", outputText)
        self.disp.config(state=tk.DISABLED)

# Make application instance
app = Analyzer()
app.mainloop()