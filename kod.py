from collections import Counter
my_dict = {'x': 100, 'p': 125, 'c': 25, 'd': 55, 'a': 99, 'f': 87}

values = []
for k, v in my_dict.items():
    values.append(v)

maximum = []
for j in range(3):
    maximum.append(max(values))
    values.pop(values.index(max(values)))

c = Counter(maximum)
for i in maximum:
    if c[i] > 1:
        maximum.pop(maximum.index(i))

        maximum.append(max(values))
    else:
        pass

for i in range(3):
    print(list(my_dict.keys())[list(my_dict.values()).index(maximum[i])],end=" ")
