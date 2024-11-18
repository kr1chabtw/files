with open('message.txt', 'r') as f, open('encrypted_message.txt', 'w') as new:
    alf = list('абвгдеёжзийклмнопрстуфхцчъыьэюя')
    print(alf)
    x = f.read().strip()
    for i in x:
        a = alf[alf.index(i)+3]
        new.write(a)
# Что делать с эюя без понятия


