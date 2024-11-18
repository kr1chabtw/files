with open("story.txt", "r") as f, open('new_story.txt', 'w') as new:
    content = f.read().strip()
    a = list(content.split(" "))
    for i in a:
        if i == "python":
            new.write(f'java ')
        else:
            new.write(f'{i} ')



