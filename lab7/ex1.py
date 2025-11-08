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








if (file1_r != None and file2_w != None):
    text = file1_r.read()
    words = re.findall(r"\b[а-яА-Яa-zA-Z]+\b", text)
    length_dict = {}
    for word in words:
        l = len(word)
        length_dict[l] = length_dict.get(l, 0) + 1

    for length in sorted(length_dict):
        file2_w.write(f"Слова довжиною {length}: {length_dict[length]}\n")
    print("Результати успішно записано у файл TF4_2.txt")
    file1_r.close()
    file2_w.close()
