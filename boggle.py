filename = "dict.txt"
with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content] 