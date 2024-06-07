from docx import Document

# Открытие файла .docx
doc = Document('C:/Users/ximik/OneDrive/Рабочий стол/voina-i-mir.docx')
a = []

def check(a, word):
    k = 0
    for i in range(len(a)):
        if a[i][1] == word:
            a[i][0] += 1
            k = 1
            break
    if k == 0:
        b = [1, word]
        a.append(b)
    return a

word = input("Введите слово: ")

if len(word) >= 3:
    # Чтение и вывод содержимого документа
    for paragraph in doc.paragraphs:
        arr = paragraph.text.split()
        for i in arr:
            if word in i:
                check(a, i)
                if len(a) == 20:
                    break
        if len(a) == 20:
            break
    
    # Сортировка списка по убыванию первого элемента
    a.sort(key=lambda x: x[0], reverse=True)
    
    print(a)
else:
    print("Введите слово длиннее 2 символов")
