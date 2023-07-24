

# print(help(list))


# print('hello'.capitalize())

# numbers = [1, 2, 3]
# numbers.append(4)

# print(numbers)


# print('banana'.find('a')) # 1
# print('banana'.find('z')) # -1

# print('banana'.index('a')) # 1
# print('banana'.index('z')) # ValueError: substring not found

# string1 = 'HELLO'
# string2 = 'Hello'

# print(string1.isupper()) #True
# print(string2.isupper()) #False
# print(string1.islower()) #False
# print(string2.islower()) #False


# string1 = 'Hello'
# string2 = '123'
# print(string1.isalpha()) #True
# print(string2.isalpha()) #False



# print(string1.istitle())


# text = 'Hello, world!'
# new_text = text.replace('world', 'Python')

# print (new_text)

# text = '   Hello, world!   ' 
# new_text = text.strip()

# print (new_text)



# text = 'Hello, world!' 
# words = text.split(',')

# print (words)



# words = ['Hello', 'world!'] 
# text = ', '.join(words)

# print (text)



# text = 'heLLo, woRld!' 
# new_text1 = text.capitalize()
# new_text2 = text.title()
# new_text3 = text.upper()
# new_text4 = text.swapcase()

# print (new_text1)
# print (new_text2)
# print (new_text3)
# print (new_text4)



# numbers = [1, 2, 3]
# numbers2 = [4, 5, 6]

# # numbers.append(numbers2)
# # print(numbers) # [1, 2, 3, [4, 5, 6]]

# numbers.extend(numbers2)
# print(numbers) # [1, 2, 3, 4, 5, 6]



# my_list = [1,2,3,4,4,3,2,2,2,23,3,3,3,2,3,3,]
# count = my_list.count(3)
# print(count)



# my_list = [3,2,1]
# my_list.sort()
# print(my_list) # [1, 2, 3]

# my_list.sort(reverse=True)
# print(my_list) # [3, 2, 1]



# my_list = [1,3,6,7,2,9,8]
# my_list.reverse()
# print(my_list)



# # sort 메서드 vs sorted 함수

# numbers = [3,2,1]

# print(numbers.sort()) #None
# # 원본을 바꿔버린다

# print(sorted(numbers)) #[1,2,3]
# # 원본을 건드리지 않고 사본을 만들어서 리턴



# numbers = [1,2,3]

# # 1. 할당
# list1 = numbers 

# # 2. 슬라이싱 (복사본을 만든다.)
# list2 = numbers[:] 

# numbers[0] = 100

# print(list1) # [100, 2, 3]
# print(list2) # [1, 2, 3]


# my_str = 'hello'
# kk = reversed(my_str)



# print(kk)


# print (76 % 2 == 1)



# 별 찍기 - 1

# case = int(input())

# for i in range(case):
#     print ('*' * (i+1))



# 별 찍기 -2

# case = int(input())

# for i in range(case):
#     print (' ' * (case-1-i) + '*' * (i+1))



# 별 찍기 -3

# case = int(input())

# for i in range(case):
#     print('*' * (case - i))



# 별 찍기 -4

# case = int(input())

# for i in range(case):
#     print (' ' * i + '*' * (case-i))



# 별 찍기 -5

# case = int(input())

# for i in range(case):
#     print(' ' * (case - (i+1)) + '*' * (2*i+1)  + ' ')



# 별 찍기 -6

# case = int(input())

# for i in range(case):
#     print(' ' * i + '*' * (2*(case-i)-1)  + ' ')



# 별 찍기 -7


# case = int(input())

# for i in range(case):
#     print(' ' * (case - (i+1)) + '*' * (2*i+1)  + ' ')

# for i in range(case-1):
#     print(' ' * (i+1) + '*' * (2*(case-1-i)-1)  + ' ')



# 별 찍기 -8


# case = int(input())

# for i in range(case):
#     print('*' * (i+1) + ' ' * ((2*case) - 2*(i+1)) + '*' * (i+1))

# for i in range(case):
#     print('*' * (case-i-1) + ' ' * (2*(i+1)) + '*' * (case-i-1)) 



# 별 찍기 -9


case = int(input())

for i in range(case):
    print(' ' * i + '*' * (2*case-(2*(i))-1) + ' ' * i)

for i in range(case-1):
    print(' ' * (case-2-i) + '*' * (2*i + 3) + ' ' * (case-2-i))



