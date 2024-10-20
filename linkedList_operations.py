from linkedlist import LinkedList

new_list = LinkedList()
node_data = [76,34,52,96]

for data in node_data:
    new_list.insert_at_head(data)
    new_list.print_list()

#test search function
print ("Search for 34")
node = new_list.search(34)
if node: 
    print (node.data)
else:
    print (node)

print ("Search for -1")
node = new_list.search(-1)
if node:
    print(node.data)
else:
    print(node)

#test delete
#1. Delete head
new_list.delete(96)
print ("List after deleting the head: ")
new_list.print_list()

#undo delete
new_list.insert_at_head(96)

#2. Delete node 34
new_list.delete(34)
print("List after deleting node 34")
new_list.print_list()

#Selection Sort
new_list.selection_sort()
print ("Sorted List")
new_list.print_list()