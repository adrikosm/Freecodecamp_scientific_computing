counts = dict()

filename = input("Give a file name: ")
if '.txt' not in filename:
    filename = filename + '.txt'

try:
    file = open(filename)
except FileNotFoundError:
    print(f'Did not find any file with the name: {filename}')
    quit()

for line in file:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

for key, value in counts.items():
    print(f' Words: ({key}) Number of times we found it: ({value}) \n')