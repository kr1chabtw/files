with open('input.txt', 'r') as f, open('output.txt', 'w') as out:
    content = f.read()
    a = content.upper()
    out.write(a)