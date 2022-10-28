# Benson Zhou - Date Formatting Converter

months = {
    "01": "January", 
    "02": "February", 
    "03": "March", 
    "04": "April", 
    "05": "May", 
    "06": "June", 
    "07": "July", 
    "08": "August", 
    "09": "September", 
    "10": "October", 
    "11": "November", 
    "12": "December"
}

dates = input("Input date (mm/dd/yyyy): ").split("/")

print(months[dates[0]], dates[1].strip("0") + ", " + dates[2])