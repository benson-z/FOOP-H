# Benson Zhou - Seconds to Hours, minutes, and seconds

a = int(input("How many seconds: "))

if a >= 3600:
	print(a//3600, "Hours,", end=" ")
if a >= 60:
	print((a%3600)//60, "Minutes,", end=" ")
print((a%60), "Seconds")