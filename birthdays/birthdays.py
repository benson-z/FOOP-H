import tkinter as tk
import tkinter.ttk as ttk
import filewriter

fileName = "data.json"

class Birthdays(tk.Tk):
    state = "n" # n: Normal, a = Add Contact
    def __init__(self):
        super().__init__()
        self.tk.call("source", "Azure-ttk-theme-main/azure.tcl")
        self.title("Birthdays")
        self.geometry("600x400")
        self.minsize(500, 370)
        self.tk.call("set_theme", "dark")

        self.data = filewriter.importData(fileName)
        self.name = tk.StringVar()
        self.birthday = tk.StringVar()
        self.searchterm = tk.StringVar()
        self.searchterm.set("")
        self.lastsearch = ""

        self.sidebar = ttk.Frame(self)
        self.nameselector = ttk.Frame(self.sidebar)
        self.infoframe = ttk.Frame(self)
        self.sidebar.pack(side=tk.LEFT, fill="y", )
        self.infoframe.pack(side=tk.RIGHT, fill="both", anchor="nw", expand=True)

        # Search Bar
        ttk.Entry(self.sidebar, textvariable=self.searchterm).pack(fill="both", padx=5, pady=7)

        self.nameselector.pack(fill="both", expand=True, padx=5)
        #self.selector = tk.Listbox(self.nameselector, font=("", 15))
        self.selector = ttk.Treeview(self.nameselector, columns=("name",), show="headings")
        self.selector.heading("name", text="Name")
        self.importPeople()
        self.selector.pack(side=tk.LEFT, fill="y")
        #self.scrollbar = ttk.Scrollbar(self.nameselector)
        #self.scrollbar.pack(side=tk.RIGHT, fill = tk.BOTH)
        #self.selector.config(yscrollcommand=self.scrollbar.set)
        #self.scrollbar.config(command = self.selector.yview)

        self.switchstate = ttk.Button(self.sidebar, text="Add Contact", command=self.switchState, style="Accent.TButton")
        self.switchstate.pack(fill="x", padx=5, pady=7)

        # Person Info
        ttk.Label(self.infoframe, textvariable=self.name, justify="left", font=("", 40)).pack(anchor="w", padx=20, pady=(20, 10))
        ttk.Label(self.infoframe, textvariable=self.birthday, justify="left", font=("", 20)).pack(anchor="w", padx=20, pady=10)
        self.delbutton = ttk.Button(self.infoframe, text="Delete Contact", command=self.delete)

        # Start update function
        self.update()
    def importPeople(self, query = ""):
        for person in self.data["people"]:
            if person.startswith(query):
                self.selector.insert("", tk.END, values=(person.title(),))
    def update(self):
        if self.searchterm.get() != self.lastsearch:
            self.search(self.searchterm.get())
            self.lastsearch = self.searchterm.get()
        try:
            selected = self.selector.item(self.selector.focus())["values"][0]
            self.name.set(selected.title())
            self.birthday.set("Birthday: " + self.formatDate(self.data["people"][selected.lower()]["birthday"]))
            if not self.delbutton.winfo_ismapped():
                self.delbutton.pack(padx = 40, pady = (60, 0), anchor="w")
        except:
            pass
        finally:
            self.selector.after(100, self.update)
    def search(self, term):
        for item in self.selector.get_children():
            self.selector.delete(item)
        self.importPeople(term.lower())
    def switchState(self):
        if self.state == "n":
            self.state = "a"
            self.infoframe.pack_forget()
            self.switchstate.config(text="Cancel")
            self.newframe = ttk.Frame(self)
            self.newframe.pack(side=tk.RIGHT, fill="both", anchor="nw", expand=True)
            ttk.Label(self.newframe, text="Add Contact", font=("", 40)).pack(anchor="w", padx=20, pady=10)
            ttk.Label(self.newframe, text="Name", font=("", 20)).pack(anchor="w", padx=20, pady=(10, 5))
            name = ttk.Entry(self.newframe)
            name.pack(anchor="w", padx=20)
            ttk.Label(self.newframe, text="Birthday (mmddyyyy)", font=("", 20)).pack(anchor="w", padx=20, pady=(10, 5))
            birthday = ttk.Entry(self.newframe)
            birthday.pack(anchor="w", padx=20)
            alerts = ttk.Label(self.newframe, foreground="red")
            alerts.pack(anchor="w", padx=20, pady=20)
            ttk.Button(self.newframe, text="Confirm", command=lambda: self.confirm(name, birthday, alerts)).pack(side=tk.BOTTOM, padx = 40, pady = (60, 0))
        elif self.state == "a":
            self.state = "n"
            self.newframe.pack_forget()
            self.switchstate.config(text="Add Contact")
            self.infoframe.pack(side=tk.RIGHT, fill="both", anchor="nw", expand=True)
            for widgets in self.newframe.winfo_children():
                widgets.destroy()
    def confirm(self, name, birthday, alerts):
        if name.get().lower() in self.data["people"]:
            alerts.config(text="Error: Name already exits")
        elif len(name.get().strip()) == 0 or len(birthday.get().strip()) == 0:
            alerts.config(text="Error: Missing name/birthday")
        elif len(birthday.get()) != 8 or not birthday.get().isdigit():
            alerts.config(text="Error: Birthday Invalid")
        else:
            self.data["people"][name.get().lower()] = {"birthday": birthday.get()}
            filewriter.saveData(fileName, self.data)
            self.switchState()
            self.lastsearch = "⇉" # If it works, it works
    def delete(self):
        del self.data["people"][self.selector.item(self.selector.focus())["values"][0].lower()]
        self.lastsearch = ""
        filewriter.saveData(fileName, self.data)
        self.lastsearch = "⇉"
    def formatDate(self, unformatted):
        return "/".join([unformatted[:2], unformatted[2:4], unformatted[4:]])

app = Birthdays()
app.mainloop()
