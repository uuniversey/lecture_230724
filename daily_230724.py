

# 1445. hw_5_2

# def count_character(my_str, alpabet):
#     return my_str.count(alpabet)

# result = count_character("Hello, World!", "o")
# print(result)



# 1446. hw_5_4

# def find_min_max(my_list):
#     list_box = sorted(my_list)

#     return (list_box[0], list_box[-1])

# result = find_min_max([3, 1, 7, 2, 5])
# print(result) 



# 1440. ws_5_1

# def reverse_string(my_str):
    
#     my_list = list(reversed(my_str))
#     return ''.join(my_list)

# result = reverse_string("Hello, World!")
# print(result)



# 1468. ws_5_2

# def remove_duplicates(my_list):
#     new_lst = []
#     new_lst = list(set(my_list))

#     return new_lst

# result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# print(result)



# 1442. ws_5_3

# def sort_tuple(my_tuple):
#     new_tuple = ()
#     sorted_tuple = tuple(sorted(my_tuple))
#     new_tuple = sorted_tuple
#     return new_tuple

# result = sort_tuple((5, 2, 8, 1, 3))
# print(result)



# 1443. ws_5_4

# def capitalize_words(my_str):
#     capi = my_str.title()
#     return capi


# result = capitalize_words("hello, world!")
# print(result)



# 1444. ws_5_5

even_box = []
odd_box = []
result_box = []

def even_elements(num_box):
    
    for i in range(len(my_list)):
        num = num_box.pop(0)
        if num % 2 == 0:
            even_box.append(num)
        
        else:
            odd_box.append(num)
            
    result_box.extend(even_box)
    return result_box

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
