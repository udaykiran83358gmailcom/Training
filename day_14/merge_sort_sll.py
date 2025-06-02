class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        if not self.head:
            self.head = self.temp = new
        else:
            self.temp.next = new
            self.temp = new

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

    def merge(self, head):
        if not head or not head.next:
            return head

        mid = self.get_middle(head)
        mid_next = mid.next
        mid.next = None

        left = self.merge(head)
        right = self.merge(mid_next)

        return self.merge_sort(left, right)

    def merge_sort(self, left, right):
        dummy = Node(-1)
        tail = dummy
        while left and right:
            if left.data > right.data:
                tail.next = right
                right = right.next
            else:
                tail.next = left
                left = left.next
            tail = tail.next

        while left:
            tail.next = left
            left = left.next
            tail = tail.next

        while right:
            tail.next = right
            right = right.next
            tail = tail.next

        return dummy.next

    def get_middle(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sort(self):
        self.head = self.merge(self.head)

# Test the implementation
obj = LinkedList()
obj.insert(4)
obj.insert(2)
obj.insert(1)
obj.insert(5)
obj.insert(3)

print("Original List:")
obj.display()

obj.sort()

print("Sorted List:")
obj.display()
