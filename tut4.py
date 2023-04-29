my_list = [1, 2, 3]
my_list.append(4)
# my_list: [1, 2, 3, 4]
my_list.extend([4, 5, 6])
# my_list: [1, 2, 3, 4, 5, 6]
my_list.insert(2, 3)
# my_list: [1, 2, 3, 4]
my_list.remove(2)
# my_list: [1, 3, 2, 4]
item = my_list.pop(1)
my_list.clear()
index = my_list.index(2)
count = my_list.count(2)
my_list.sort()
my_list.reverse()