f = open("drawings.json", "r")
f_out = open("drawings_2.json", "a")

f_out.write("[")

for line in f.readlines():
    f_out.write(line)
    f_out.write(",")



f_out.write("]")
