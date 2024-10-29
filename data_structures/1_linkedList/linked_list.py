class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        iterator = self.head
        llstr = ''
        while iterator:
            llstr += str(iterator.data)+' --> ' if iterator.next else str(iterator.data)
            iterator = iterator.next
        print(llstr)

    def get_length(self):
        count = 0
        iterator = self.head
        while iterator:
            count+=1
            iterator = iterator.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        iterator = self.head

        while iterator.next:
            iterator = iterator.next

        iterator.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        iterator = self.head
        while iterator:
            if count == index - 1:
                node = Node(data, iterator.next)
                iterator.next = node
                break

            iterator = iterator.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        iterator = self.head
        while iterator:
            if count == index - 1:
                iterator.next = iterator.next.next
                break

            iterator = iterator.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    ll.print()

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print()
