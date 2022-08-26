import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()

window.title("Temperature Converter")

conversions = ["Fahrenheit to Celcius", "Celsius to Fahrenheit"]

default = tk.StringVar()
default.set("Fahrenheit to Celcius")

selector = tk.OptionMenu(window, default, *conversions)
selector.pack()

outputText = tk.StringVar()

output = ttk.Label(master=window, textvariable = outputText)

inputText = tk.StringVar()
inputBox = ttk.Entry(master=window, textvariable = inputText)
inputBox.pack(fill = "x")

output.pack(fill = "x")

def calculate():
	try:
		a = float(inputText.get())
	except:
		outputText.set("Invalid Input")
		return
	if default.get().startswith("F"):
		if a < -459.67:
			outputText.set("Invalid Input: Temperature below absolute zero")
			return
		outputText.set(str(round((a-32)*5/9))+"˚ Celcius")
		return
	else:
		if a < -273.15:
			outputText.set("Invalid Input: Temperature below absolute zero")
			return
		outputText.set(str(round((a*9/5)+32)) + "˚ Fahrenheit")
# Calculate button
enter = ttk.Button(master=window, command=calculate, text="Calculate")
enter.pack()

window.mainloop()