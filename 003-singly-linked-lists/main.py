class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_position(self, data, position):
        if position < 0:
            raise ValueError("Position must be non-negative.")
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    raise IndexError("Position out of bounds.")
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def update(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return
            current = current.next
        raise ValueError(f"Data {old_data} not found in the list.")

    def delete_at_beginning(self):
        if self.head is None:
            raise IndexError("List is empty.")
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            raise IndexError("List is empty.")
        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None

    def delete_node(self, data):
        if self.head is None:
            raise IndexError("List is empty.")
        if self.head.data == data:
            self.head = self.head.next
        else:
            current = self.head
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    return
                current = current.next
            raise ValueError(f"Data {data} not found in the list.")
        
# Create a singly linked list
sll = SinglyLinkedList()

# Insert elements
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_beginning(5)
sll.insert_at_position(15, 2)

# Display the list
sll.display()  # Output: 5 -> 10 -> 15 -> 20 -> None

# Update an element
sll.update(15, 25)
sll.display()  # Output: 5 -> 10 -> 25 -> 20 -> None

# Delete elements
sll.delete_at_beginning()
sll.delete_at_end()
sll.delete_node(10)
sll.display()  # Output: 25 -> None