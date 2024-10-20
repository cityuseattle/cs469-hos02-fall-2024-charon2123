class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def print_list(self):
        cur = self.head
        arr = []
        while cur:
            arr.append(str(cur.data))
            cur = cur.next
        print('->'.join(arr))

    def insert_at_head(self,data):
        if data is not None:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    
    def search(self, data):
        cur = self.head

        #check if the LinkedList has no node
        if cur is None:
            return None
        while cur and cur.next:
            if cur.data == data:
                return cur
            cur = cur.next

    def delete(self, data):
        cur = self.head
        prev = None

        if cur is not None and cur.data == data:
            self.head = self.head.next
            return
        while cur:
            if cur.data == data:
                prev.next = cur.next
                break
            prev, cur = cur, cur.next

    def find_smallest(self, node):
        if node is None:
            return None

        cur = node

        #holder for smallest node
        smallest_node = cur
        smallest = cur.data

        while cur:
            if cur.data < smallest:
                smallest = cur.data
                smallest_node = cur
            cur = cur.next
        return smallest, smallest_node

    def selection_sort(self):
        cur = self.head
        while (cur):
            _, smallest_node = self.find_smallest(cur)
            cur.data, smallest_node.data = smallest_node.data, cur.data
            cur = cur.next        