# Benson Zhou - Tip Calculator
import tkinter as tk
import tkinter.ttk as ttk

#Initlal window setup
window = tk.Tk()

window.title("Tip Calculator")

# Position Elements
masterFrame = tk.Frame(window)
masterFrame.pack()
entryFrame = tk.Frame(master=masterFrame)
entryFrame.pack(side=tk.LEFT)

resultFrame = tk.Frame(master=masterFrame)
resultFrame.pack(side=tk.RIGHT)

billFrame = tk.Frame(master=entryFrame)
billFrame.pack()
percentFrame = tk.Frame(master=entryFrame)
percentFrame.pack()
peopleFrame = tk.Frame(master=entryFrame)
peopleFrame.pack()

#Store variables seperate from entries
currentBill = 0.0
currentPercentage = 15.0
currentPeople = 1

# General function for formatting numbers
def formatnum(num, pos):
	global currentBill, currentPeople, currentPercentage
	if num.startswith("-"):
		print(pos, "can't be negative")
		return -1
	try:
		a = float(num)
	except:
		print("Invalid input")
		return -1
	if pos == "bill":
		a = round(a, 2)
		currentBill = a
		return "{:.2f}".format(a)
	elif pos == "percent":
		currentPercentage = a;
	elif pos == "people":
		a = round(a)
		currentPeople = a
	return str(a)

# Bill entry
blabel = tk.Label(master=billFrame, text="Bill ($)", width=8, anchor="e")
blabel.grid(row=0, column=0)
blabel.pack(side=tk.LEFT)

billText = tk.StringVar()
billText.set("{:.2f}".format(0.00))
def checkBill():
	result = formatnum(billText.get(), "bill")
	if result != -1:
		billText.set(result)
		return True
	billText.set("{:.2f}".format(0.00))
	return False
bill = ttk.Entry(master=billFrame, width = 10, textvariable = billText, validate="focusout", validatecommand=checkBill)
bill.pack(side=tk.RIGHT)

# Percentage entry
plabel = tk.Label(master=percentFrame, text="Tip (%)", width=8, anchor="e")
plabel.pack(side=tk.LEFT)

percentText = tk.StringVar()
percentText.set("15.0")
def checkPercentage():
	result = formatnum(percentText.get(), "percent")
	if result != -1:
		percentText.set(result)
		return True
	percentText.set("0.00")
	return False
percent = ttk.Entry(master=percentFrame, width = 10, textvariable = percentText, validate="focusout", validatecommand=checkPercentage)
percent.pack(side=tk.RIGHT)

# Number of People entry
nlabel = tk.Label(master=peopleFrame, text="# of People", width=8, anchor="e")
nlabel.pack(side=tk.LEFT)

peopleText = tk.StringVar()
peopleText.set("1")
def checkPeople():
	result = formatnum(peopleText.get(), "people")
	if result != -1:
		peopleText.set(result)
		return True
	peopleText.set("1")
	return False
people = ttk.Entry(master=peopleFrame, width = 10, textvariable = peopleText, validate="focusout", validatecommand=checkPeople)
people.pack(side=tk.RIGHT)

# Display results
totalLabel = tk.Label(master=resultFrame, text = "Total per person")
total = tk.Label(master=resultFrame, text = "$0.00", anchor = "center")
totalLabel.pack(fill = "x")
total.pack(fill = "x")
tipLabel = tk.Label(master=resultFrame, text = "Total tip per person")
tip = tk.Label(master=resultFrame, text = "$0.00", anchor = "center")
tipLabel.pack(fill = "x")
tip.pack(fill = "x")

# Calculate and update results
def calculate():
	print("Total tip: $", "{:.2f}".format(currentBill*currentPercentage/100))
	total.config(text = "$" + "{:.2f}".format((currentBill*currentPercentage/100+currentBill)/currentPeople))
	tip.config(text = "$" + "{:.2f}".format((currentBill*currentPercentage/100)/currentPeople))
	tip.after(500, calculate)

calculate()
# Calculate button
#enter = ttk.Button(master=window, command=calculate, text="Calculate")
#enter.pack()

window.mainloop()
