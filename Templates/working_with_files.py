# Open a file and read from it line by line
f = open("Exemplu_date.txt", "r")
for line in f.readlines():
    print(line)
f.close()

# Open a file and read from it line by line
with open("Exemplu_date.txt", "r") as file:
    for line in file.readlines():
        print(line)

# Open a file and write in it
f = open("Exemplus_date.txt", "w")
f.write("demo test test")
f.close()

# Open a file and write in it
with open("Exemplus_date.txt", "w") as file:
    file.write("demo test test")

# Open a file and append to it
f = open("Exemplus_date.txt", "a")
f.write("demo test test")

# Open a file and append to it
with open("Exemplus_date.txt", "a") as file:
    file.write("demo test test")
