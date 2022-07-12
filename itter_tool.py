#using itter tools

import itertools


my_list = [[1],[2,3],[4,5,6]]

flat_list = list(itertools.chain(*my_list))
print(flat_list[3])








#nested for loop to do the same
#from sublist to making a flat list

my_list = [[1],[2,3],[4,5,6]]

flat_list = []

for sublist in my_list:
    for elements in sublist:
        flat_list.append(elements)

print(flat_list)









#using sum 
my_list = ([1,2],[2,3],[4,5,6])

flat_list = sum(my_list,[])

print(flat_list)
