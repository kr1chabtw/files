with open('part1.txt', 'r') as f, open('part2.txt', 'r')as f2, open('full_text.txt', 'w') as new:
    content1 = f.read().strip()
    content2 = f2.read().strip()
    print(content1, content2)
    new.write(content1 + " ")
    new.write(content2)