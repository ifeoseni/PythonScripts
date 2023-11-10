number_list = [1,2,3,5]
numper_tuple = (1,2,3)

print(f'Original List is {number_list}')
# mutability i.e you can change list value
number_list[1] = 1
print(f'Updated List is {number_list}')

# change multiple values at once
number_list[1:3] = [0,3]  # ensure the assigned variable is equal to what was declared to avoid typeerror
print(f'Updated List is {number_list}')

colors = ["red", "yellow", "green", "blue"]
colors[1:3] = [1,2]
print(f'Colors {colors}')

# note that if the assigned values is more than the original length, it will increase the length of the width
list_4 = [1,2,3,4]
list_4[1:2] = [5,6,7,8,8,8]
print(f'Expaned list is {list_4} and the length is {len(list_4)}')

# if the assigned length is lesser than the slice number the length reduce
new_colors = ['red', 'orange', 'magenta', 'aqua', 'blue']
new_colors[1:4] = ["yellow", "green"]  # normally we are expecting 3 values but what will happen now is that the 3 values will be replaced by only 2 and the 3rd value disappears from the list
print(f'New colors is {new_colors}')