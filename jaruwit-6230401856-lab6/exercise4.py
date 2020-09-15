import shutil
try:
    f = open("kku2.txt", "x", encoding='utf-8')
except FileExistsError:
    print("")
shutil.copyfile('kku.txt', 'kku2.txt')
f = open("kku2.txt", "a+", encoding='utf-8')
f.write("\n")
f.write("Motto: วิทยา จริยา ปัญญา")
f.write("\n")
f.write("Motto in English: Knowledge, Virtues, Wisdom")
f.close()
f_read = open("kku2.txt", "r", encoding='utf-8')
lines = f_read.read()
print(lines)
f_read.close()
