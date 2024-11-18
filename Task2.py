with open('data.txt', 'r') as f, open('even.numbers.txt', 'w') as num:
    list_ = f.read().strip()
    a = list_.split(" ")
    print(a)
    for i in range(len(a)):
        x = int(a[i])
        if x % 2 == 0:
            num.write(f'{x} ')





