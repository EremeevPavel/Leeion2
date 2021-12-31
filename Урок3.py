my_list = [10, None, -30, 'True', [1+2], 9.5]

for i, item in enumerate(my_list, 1):

    print(f"{i}){item} - {type(item)}")
