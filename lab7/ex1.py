import re

def file_open (filename,mode,encoding="utf-8-sig"):
    try:
        file=open(filename,mode, encoding=encoding)
    except:
        print("Файл", filename, "не вдалося відкрити")
        return None
    else:
        print("Файл", filename, "вдалося відкрити")
        return file

filename1="TF4_1.txt"
filename2="TF4_2.txt"
file1_w=file_open(filename1,"w")
if (file1_w != None):
    file1_w.write("Текст, що містить символьні рядки різної довжини, розділові знаки та цифри: 12 3132 1")
    print("Інформацію було успішно занесено у файл TF4_1.txt")
    file1_w.close()
    print("Файл TF4_1.txt було успішно закрито")
file1_r=file_open(filename1,"r")
file2_w=file_open(filename2,"w")
if file1_r is not None and file2_w is not None:
    text=file1_r.read()
    words=re.findall(r"[A-Za-zА-Яа-яЇїІіЄєҐґ]+", text)
    length_count = {}
    for w in words:
        l= len(w)
        length_count[l] =length_count.get(l, 0) + 1
    for length in sorted(length_count.keys()):
        file2_w.write(f"Слів із {length} символів: {length_count[length]}\n")
    print("Результати підрахунку записано у файл TF4_2.txt.")
    file1_r.close()
    file2_w.close()
    print("Файли TF4_1.txt та TF4_2.txt закрито.\n")
file2_r =file_open(filename2, "r")
if file2_r is not None:
    print("Вміст файлу TF4_2.txt:")
    for line in file2_r:
        print(line.strip())
    file2_r.close()
    print("\nФайл TF4_2.txt було успішно закрито.")
