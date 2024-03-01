my_list = [1, 2, 3, 4, 5, 2, 6, 7, 2]
element_to_remove = 2
count_removed = 0

while element_to_remove in my_list:
    my_list.remove(element_to_remove)
    count_removed += 1

print("تعداد عناصر حذف شده:", count_removed)
print("لیست پس از حذف:", my_list)
