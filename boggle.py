filename = "dict.txt"

with open(filename) as f:
    dictionary = f.readlines()
print(len(dictionary))