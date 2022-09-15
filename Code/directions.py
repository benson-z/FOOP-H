# Benson Zhou - Directions to Class

classes = {
	"english": "200s building", 
	"math": "second floor of the 800s building", 
	"history": "first floor of the 800s building", 
	"pe": "gym", 
	"science": "1700s building"
}

name = input("Hi, what's your name?\n")
subject = input("What class are you heading to?\n")

if (subject.lower() in ["biology", "bio", "chemistry", "chem", "physics"]):
	subject = "science"
elif (subject.lower() in ["algebra", "geometry", "analysis", "calculus"]):
	subject = "math"

print(subject.capitalize(), "is at the", classes[subject.lower()], ".")