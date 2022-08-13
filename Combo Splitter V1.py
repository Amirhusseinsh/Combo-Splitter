file = input("Enter the file name: ")
l = int(input("Enter the line number: "))
j = 1
with open(f'{file}.txt', 'r', encoding="utf8") as f:
    while(f.readline() != ''):
        with open(f"{file} part{j}.txt", "a", encoding="utf8") as US:
            for i in range(l):
                try:
                    line = f.readline()
                finally:
                    US.writelines(line)
            j = j + 1
