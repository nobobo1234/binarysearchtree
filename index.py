from tree import Tree
from random import randint

tree = Tree()

for i in range(0, 10):
    tree.add_value(randint(0, 100))

tree.traverse()

search = input('What value do you want to find?')
result = tree.search(int(search))
if result is not None:
    print('Found:', result)
else:
    print(search + ' not found :(')
