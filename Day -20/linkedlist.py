class Node:
    def __init__(self, data):   # corrected
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):         # corrected
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")

    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next

    def insert_at_position(self, pos, data):
        new_node = Node(data)

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for _ in range(pos - 1):
            if temp is None:
                return
            temp = temp.next

        if temp is None:
            return

        new_node.next = temp.next
        temp.next = new_node

    def delete_value(self, key):
        if self.head is None:
            return

        if self.head.data == key:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next

    def delete_at_position(self, pos):
        if self.head is None:
            return

        if pos == 0:
            self.head = self.head.next
            return

        temp = self.head
        for _ in range(pos - 1):
            if temp is None or temp.next is None:
                return
            temp = temp.next

        temp.next = temp.next.next

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def get(self, pos):
        temp = self.head
        for _ in range(pos):
            if temp is None:
                return None
            temp = temp.next

        return temp.data if temp else None
    
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        self.head = prev

    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow==fast:
                return True
        return False
    




# =========================
# INPUT / TESTING SECTION
# =========================

ll = LinkedList()

n = int(input("Enter number of elements: "))
for _ in range(n):
    val = int(input("Enter value: "))
    ll.insert_end(val)

print("\nLinked List:")
ll.display()

pos = int(input("\nEnter position to insert: "))
data = int(input("Enter value to insert: "))
ll.insert_at_position(pos, data)

print("After insertion:")
ll.display()

key = int(input("\nEnter value to delete: "))
ll.delete_value(key)

print("After deleting value:")
ll.display()

pos = int(input("\nEnter position to delete: "))
ll.delete_at_position(pos)

print("After deleting position:")
ll.display()

key = int(input("\nEnter value to search: "))
print("Found:" if ll.search(key) else "Not Found")

pos = int(input("\nEnter position to access: "))
print("Value at position:", ll.get(pos))
