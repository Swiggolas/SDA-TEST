#text file has to be in the same directory as the code file
with open('test.txt') as f:
    contents = f.read()
print(contents)
# this is the same as doing this print(open('test.txt').read())