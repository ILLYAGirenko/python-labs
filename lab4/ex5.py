def check():
    a = input("Введіть текст: ").lower()
    letters = set(i for i in a if i.isalpha())
    v_count  = letters & set("aeiouy")
    c_count = letters - v_count
    if len(v_count)>len(c_count):
        print("У тексті більше голосних букв")
    elif len(v_count)==len(c_count):
        print("У тексті однакова кількість голосних та приголосних букв")
    else:
        print("У тексті більше приголосних букв")
check()