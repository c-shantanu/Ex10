empty_lst = []
total_items = int(input("Total number of items: "))
for i in range(0,total_items):
    grocery = input("Enter your shopping list: ")
    empty_lst.append(grocery)
    if len(empty_lst) == 3:
        break
    
joined_string = ",".join(empty_lst)
print(joined_string)