import re

counts = {'a': 10, 'b': 1, 'c': 22}

lst = []

for key, val in counts.items():
    new_tuple = (key, val)
    lst.append(new_tuple)

lst = sorted(lst, reverse=True)
print(lst)

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)
