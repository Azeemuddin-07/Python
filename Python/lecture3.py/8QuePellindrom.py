

list = []
list.append(input("enter 1st element : "))
list.append(input("enter 2nd element : "))
list.append(input("enter 3rd element : "))
copy_list = list.copy() # copy_list is a variable.
copy_list.reverse()
if(copy_list == list):
    print("It is pellindrome") # pellindrome means equal from start & end. ex-- 121 , ma'am.
else:
    print("Not pellindrome")
