import tkinter as tk
from decimal import Decimal

# Window setup
root = tk.Tk()
frame = tk.Frame(root)
root.title("Calculator")

s_number = '0'
firstnum = ''
op = ''
mul= False


secondnum = '0'
state = 0

# Number input
def nbutton(number, pi = False):
	global s_number
	global firstnum
	global mul
	
	if number == '.':
		if '.' in s_number:
			number = ''
	if mul == True:
		firstnum = s_number
		s_number = '0'
		screen.delete('1.0', tk.END)
		screen.insert(tk.INSERT, s_number)
		mul = False
	if pi == True:
		s_number = '0'
	if s_number == '0':
		s_number = str(number)
	else:
		s_number = s_number+str(number)
	screen.delete('1.0', tk.END)
	screen.insert(tk.INSERT, s_number)

# Operator pressed
def operate(a):
	global s_number
	global firstnum
	global secondnum
	global op
	global state
	global mul
	if state == 0:
		firstnum = s_number
		state =1
		if a!= '=':
			s_number = '0'
			op = a
		elif a == '=':
			s_number = s_number
			firstnum = secondnum = op = ''
			state = 0
	
	elif  state ==1:
		secondnum = s_number
		if a != '=':
			s_number = str(eval(firstnum+op+secondnum))
			firstnum = secondnum = ''
			op = a
			state = 1
			mul = True
		elif a == '=':
			s_number = str(eval(firstnum+op+secondnum))
			firstnum = secondnum = op = ''
			state = 0
	#reset screen
	screen.delete('1.0', tk.END)
	screen.insert(tk.INSERT, s_number)

# Changes current number to negative and back
def negative():
	global s_number
	s_number = str(Decimal(s_number)*-1)
	screen.delete('1.0', tk.END)
	screen.insert(tk.INSERT, s_number)

# CE function: resets all variables to initial
def clear_text ():
	global s_number
	global firstnum
	global secondnum
	global op
	global state
	global mul
	s_number = '0'
	firstnum = secondnum = op = ''
	state = 0
	mul = False
	screen.delete('1.0', tk.END)
	screen.insert(tk.INSERT, s_number)

# Key press
def key_input(event):
	if (event.char in "+-*/=") :
		operate(event.char)
	elif event.char == '\r':
		operate("=")
	else :
		nbutton(event.char)
	
# Create on screen elements
screen = tk.Text(root, height = 4, font = ('', 20), width = 35)
screen.insert(tk.INSERT, s_number)
one = tk.Button(root, text = '1', height = 3, font = ('', 20), command = lambda: nbutton('1') )
two = tk.Button(root, text = '2', height = 3, font = ('', 20), command = lambda: nbutton('2'))
three = tk.Button(root, text = '3', height = 3, font = ('', 20), command = lambda: nbutton('3'))
four = tk.Button(root, text = '4', height = 3, font = ('', 20), command = lambda: nbutton('4'))
five = tk.Button(root, text = '5', height = 3, font = ('', 20), command = lambda: nbutton('5'))
six = tk.Button(root, text = '6', height = 3, font = ('', 20), command = lambda: nbutton('6'))
seven = tk.Button(root, text = '7', height = 3, font = ('', 20), command = lambda: nbutton('7'))
eight = tk.Button(root, text = '8', height = 3, font = ('', 20), command = lambda: nbutton('8'))
nine = tk.Button(root, text = '9', height = 3, font = ('', 20), command = lambda: nbutton('9'))
zero = tk.Button(root, text = '0', height = 3, font = ('', 20), command = lambda: nbutton('0'))
equal = tk.Button(root, text = '=', height = 3, font = ('', 20), command = lambda: operate('='))
plus = tk.Button(root, text = '+', height = 3, font = ('', 20), command = lambda: operate('+'))
minus = tk.Button(root, text = '-', height = 3, font = ('', 20), command = lambda: operate('-'))
times = tk.Button(root, text = '×', height = 3, font = ('', 20), command = lambda: operate('*'))
divide = tk.Button(root, text = '÷', height = 3, font = ('', 20), command = lambda: operate('/'))
decimal = tk.Button(root, text = '.', height = 3, font = ('', 20), command = lambda: nbutton('.'))
sign = tk.Button(root, text= '+/-', height = 3, font = ('', 18), command = negative)
ce = tk.Button(root, text= 'CE', height = 3, font = ('', 18), command = clear_text)
pi = tk.Button(root, text= 'π', height = 3, font = ('', 18), command = lambda: nbutton('3.14159265358979323846264338327', True))

# Window arrangement
screen.grid(row=0, sticky = 'nsew', columnspan = 5)

one.grid(row = 1, sticky = 'nsew')
two.grid(row = 1, column = 1, sticky = 'nsew')
four.grid(row = 2, sticky = 'nsew')
five.grid(row = 2, column = 1, sticky = 'nsew')
three.grid(row = 1, column = 2, sticky = 'nsew')
divide.grid(row = 4, column = 3, sticky = 'nswe')
six.grid(row = 2, column = 2, sticky = 'nsew')
times.grid(row = 3, column = 3, sticky = 'nesw')
seven.grid(row = 3, sticky = 'nsew')
eight.grid(row = 3, column = 1, sticky = 'nsew')
nine.grid(row = 3, column = 2, sticky = 'nsew')
minus.grid(row = 2, column = 3, sticky = 'nwse')
plus.grid(row = 1, column = 3, sticky = 'nswe')
equal.grid(row = 3, column = 4, rowspan = 2, sticky = 'nswe')
zero.grid(row = 4, column = 1, sticky = 'nsew')
decimal.grid(row = 4, column = 2, sticky = 'nesw')
sign.grid(row = 4, column = 0, sticky = 'nsew')
ce.grid(row = 2, column = 4, sticky = 'nsew')
pi.grid(row = 1, column = 4, sticky = 'nsew')

# Keyboard input (bind keyboard keys to calculator functions)
root.bind("0", key_input)
root.bind("1", key_input)
root.bind("2", key_input)
root.bind("3", key_input)
root.bind("4", key_input)
root.bind("5", key_input)
root.bind("6", key_input)
root.bind("7", key_input)
root.bind("8", key_input)
root.bind("9", key_input)
root.bind("+", key_input)
root.bind("-", key_input)
root.bind("*", key_input)
root.bind("/", key_input)
root.bind("=", key_input)

root.bind("<Return>", key_input)

# Make window freely resizable
root.rowconfigure(0,weight = 1)
root.rowconfigure(1,weight = 1)
root.rowconfigure(2,weight = 1)
root.rowconfigure(3,weight = 1)
root.rowconfigure(4,weight = 1)
root.columnconfigure(0,weight = 1)
root.columnconfigure(1,weight = 1)
root.columnconfigure(2,weight = 1)
root.columnconfigure(3,weight = 1)
root.columnconfigure(4, weight = 1)

root.mainloop()
