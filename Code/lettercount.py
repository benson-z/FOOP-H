c = 0
b = 0
def count(letter):
    global b, c
    if letter == 'c':
        c += 1
    elif letter == 'b':
        b += 1
[count(x) for x in input()]
print("{d} b's and {e} c's".format(d=b, e=c))