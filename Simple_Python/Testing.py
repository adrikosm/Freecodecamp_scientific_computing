for i in [2, 1, 5]:
    print(i)

smallest = None
print("Before:", smallest)

for itervar in [44, 41, 12, 9, 74, 15, 3]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

for n in "banana":
    print(n)

word = "bananana"
i = word.find("na")
print(i, '\n')

for i in range(1, 10, 1):
    if i == 3:
        continue
    print(i)

words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
print(pieces[3])
parts = pieces[3].split('-')

print(parts)

n = parts[1]
print(n)

dict = {"Fri": 20, "Thu": 6, "Sat": 1}
dict["Thu"] = 13
dict["Sat"] = 2
dict["Sun"] = 9
print(dict)

counts = {'quincy': 1, 'mrugesh': 42, 'beau': 100, '0': 10}
print(counts.get('0', 0) + 1)

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])