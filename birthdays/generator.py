import random
import filewriter

data = {
    "people":{}
}

for x in range(100):
    name = ""
    for a in range(15):
        name += random.choice(list("qwertyuiopasdfghjklzxcvbnm"))
    month = str(random.randint(1, 12))
    if len(month) == 1:
        month = "0" + month
    day = str(random.randint(1, 28))
    if len(day) == 1:
        day = "0" + day
    date = month+day+str(random.randint(1960, 2022))
    data["people"][name] = {"birthday": date}

filewriter.saveData("data.json", data)