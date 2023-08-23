print("Question 1:")
# define function
def list_element(len):
    my_list=[]
    for i in range(0,len):
        # list input value
        element_input = input(f"Enter Element {i} : ")
        my_list.append(element_input)
    print(my_list)  
# input variable      
length_input=int(input("Enter The length of list input: "))
# function call
list_element(length_input)


print("Question 2:")
# define list
list_data = [1, 3,4, 5, 7, 8, 9, 12, 15, 27, 20]
# assending order
list_data.sort()
# result
print(list_data[-2])


print("Question 3:")
# define list 
list_data2 = [8, 2, [], 1, [], [], 9]
# # test_list2.remove('')
# remove empty list
res = list(filter(None, list_data2))
print(res)

print("Question 4:")
#define list     
dup_list = [1, 2, 3, 4, 2, 7, 8, 8, 3];     
     
print("Duplicate Number in given list: ");    
#for duplicate element    
for i in range(0, len(dup_list)):    
    for j in range(i+1, len(dup_list)):    
        if dup_list[i] == dup_list[j]:    
            print(dup_list[j]); 



print("Question 5:")
def ReverseList(list):
   Reverse_List = list[::-1]
   return Reverse_List

list_data3 = [100, 150, 200, 250, 300, 350]
# list_data3.sort()
print(ReverseList(list_data3))


print("Question 6:")
# define 2 tuple 
tuple1 = (1, 2,3)
tuple2 = (3, 4, 5)
combinations = []
# find combinations pairs tuple
for list1 in tuple1:
    for list2 in tuple2:
        combinations.append((list1, list2))
print(combinations)


print("Question 8:")
# define list
list_data_desc = [1, 3,4, 5, 7, 8, 9, 12, 15, 27, 20]
# decending order order
list_data_desc.sort(reverse=True)
# result
print(list_data_desc)



# print("Question 6:")
# tuple_of_lists = ([1, 2, 3], ['a', 'b', 'c'])
# print(tuple(tuple(tuple_of_lists)))