# Benson Zhou - Birthdays

import tkinter as tk
import tkinter.ttk as ttk
import filewriter # .json backend
import datetime

# Set location of savedata
fileName = "data.json"

class Birthdays(tk.Tk):
    state = "n" # n: Normal, a: Add Contact
    def __init__(self):
        super().__init__()

        # Window setup
        self.tk.call("source", "Azure-ttk-theme-main/azure.tcl") # Import custom theme (https://github.com/rdbende/Azure-ttk-theme)
        self.title("Birthdays")
        self.geometry("600x400") # Resizable window
        self.minsize(500, 370) # Limits the minimum window size

        # Set theme (light or dark)
        self.tk.call("set_theme", "dark")
        # self.tk.call("set_theme", "light")

        # Variable initialization
        self.data = filewriter.importData(fileName)
        self.name = tk.StringVar()
        self.birthday = tk.StringVar()
        self.age = tk.StringVar()
        self.searchterm = tk.StringVar()
        self.searchterm.set("")
        self.lastsearch = ""

        # Setup Frames
        self.sidebar = ttk.Frame(self)
        self.nameselector = ttk.Frame(self.sidebar)
        self.infoframe = ttk.Frame(self)
        self.sidebar.pack(side=tk.LEFT, fill="y", )
        self.infoframe.pack(side=tk.RIGHT, fill="both", anchor="nw", expand=True)

        # Search Bar
        ttk.Entry(self.sidebar, textvariable=self.searchterm).pack(fill="both", padx=5, pady=7)

        # ttk Treeview for name selection
        self.nameselector.pack(fill="both", expand=True, padx=5)
        self.selector = ttk.Treeview(self.nameselector, columns=("name",), show="headings")
        self.selector.heading("name", text="Name")
        self.importPeople()
        self.selector.pack(side=tk.LEFT, fill="y")

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.nameselector)
        self.scrollbar.pack(side=tk.RIGHT, fill = tk.BOTH)
        self.selector.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command = self.selector.yview)

        # Button for switching between modes
        self.switchstate = ttk.Button(self.sidebar, text="Add Contact", command=self.switchState, style="Accent.TButton")
        self.switchstate.pack(fill="x", padx=5, pady=7)

        # Person Info Displays
        ttk.Label(self.infoframe, textvariable=self.name, justify="left", font=("", 40)).pack(anchor="w", padx=20, pady=10)
        ttk.Label(self.infoframe, textvariable=self.birthday, justify="left", font=("", 20)).pack(anchor="w", padx=20, pady=10)
        ttk.Label(self.infoframe, textvariable=self.age, justify="left", font=("", 20)).pack(anchor="w", padx=20)
        self.delbutton = ttk.Button(self.infoframe, text="Delete Contact", command=self.delete) # I didn't have time to add an edit button

        # Start update function
        self.update()


    def importPeople(self, query = ""):
        for person in self.data["people"]:
            if person.startswith(query):
                self.selector.insert("", tk.END, values=(person.title(),))


    def update(self):
        # Detect changes in the search box
        if self.searchterm.get() != self.lastsearch: 
            self.search(self.searchterm.get())
            self.lastsearch = self.searchterm.get()

        # Avoid errors from not having anything selected
        try: 
            selected = self.selector.item(self.selector.focus())["values"][0]
            self.name.set(selected.title())
            self.birthday.set("Birthday: " + self.formatDate(self.data["people"][selected.lower()]["birthday"]))
            self.age.set("Age:" + str(self.get_age(self.data["people"][selected.lower()]["birthday"])))
            if not self.delbutton.winfo_ismapped():
                self.delbutton.pack(side=tk.BOTTOM, padx = 10, pady = (7), fill="x")
        
        except:
            pass

        finally:
            self.selector.after(100, self.update) # Runs update again with a 100ms delay


    def search(self, term):
        # clear treeview and import filtered list
        for item in self.selector.get_children():
            self.selector.delete(item)
        self.importPeople(term.lower())

    
    # Switches the right pane between show info and add contact
    def switchState(self):
        if self.state == "n":
            self.state = "a"

            self.infoframe.pack_forget() # Unpack infoframe

            self.switchstate.config(text="Cancel") # Change button text

            # Initialize and pack newframe
            self.newframe = ttk.Frame(self)
            self.newframe.pack(side=tk.RIGHT, fill="both", anchor="nw", expand=True)

            ttk.Label(self.newframe, text="Add Contact", font=("", 40)).pack(anchor="w", padx=20, pady=10)

            # Name input
            ttk.Label(self.newframe, text="Name", font=("", 20)).pack(anchor="w", padx=20, pady=(10, 5))
            name = ttk.Entry(self.newframe, font=("", 15))
            name.pack(anchor="w", padx=20)
            
            # Birthday input
            ttk.Label(self.newframe, text="Birthday (mmddyyyy)", font=("", 20)).pack(anchor="w", padx=20, pady=(10, 5))
            birthday = ttk.Entry(self.newframe, font=("", 15))
            birthday.pack(anchor="w", padx=20)
            
            # Allocate space for error messages
            alerts = ttk.Label(self.newframe, foreground="red") 
            alerts.pack(anchor="w", padx=20, pady=20)
            
            ttk.Button(self.newframe, text="Confirm", command=lambda: self.confirm(name, birthday, alerts)).pack(side=tk.BOTTOM, padx = 10, pady = (7), fill="x")

        elif self.state == "a":
            self.state = "n"

            self.newframe.pack_forget() # Unpack newframe
            self.switchstate.config(text="Add Contact") # Change back button label

            self.infoframe.pack(side=tk.RIGHT, fill="both", anchor="nw", expand=True) # Repack infoframe

            # Destruct newframe
            for widgets in self.newframe.winfo_children():
                widgets.destroy()


    def confirm(self, name, birthday, alerts):
        # Name already in database
        if name.get().lower() in self.data["people"]:
            alerts.config(text="Error: Name already exits")
        # One or more fields empty
        elif len(name.get().strip()) == 0 or len(birthday.get().strip()) == 0:
            alerts.config(text="Error: Missing name/birthday")
        
        # Birthday input invalid
        elif len(birthday.get()) != 8 or not birthday.get().isdigit():
            alerts.config(text="Error: Birthday Invalid")

        # No errors
        else:
            self.data["people"][name.get().lower()] = {"birthday": birthday.get()}
            filewriter.saveData(fileName, self.data)
            self.switchState()
            self.lastsearch = "⇉" # If it works, it works

    
    def delete(self):
        del self.data["people"][self.selector.item(self.selector.focus())["values"][0].lower()]
        # Update save file
        filewriter.saveData(fileName, self.data)
        self.lastsearch = "⇉"


    # Convert to datetime for easier computation
    def todatetime(self, date):
        return datetime.datetime(int(date[4:]), int(date[:2]), int(date[2:4])) # yyyy, mm, dd


    def formatDate(self, unformatted):
        return self.todatetime(unformatted).strftime("%x")


    def get_age(self, birthday):
        # Manual calculation because I couldn't find a package
        birthdate = self.todatetime(birthday)
        today = datetime.date.today()
        years = today.year - birthdate.year

        if birthdate.month > today.month or (birthdate.month == today.month and birthdate.day > today.day):
            years -= 1

        return years


# Start app
app = Birthdays()
app.mainloop()
