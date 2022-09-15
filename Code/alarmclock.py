clock_times = {
	"monday": 8, 
	"tuesday": 8,
	"wednesday": 8,
	"thursday": 8, 
	"friday": 8, 
	"saturday": 10,
	"sunday": 10
}

try:
	print("Your alarm is set for", clock_times[input("What day is it?\n").lower()], "AM")
except:
	print("Date is invalid")