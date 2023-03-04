class LinkedList:
    def __init__(self, value):
        self.tail = {
            'value': '',
            'next': None}
        self.head = { 
            'value': value,
            'next': self.tail
        }
        self.length = 1

    def show_head(self):
        print(
            f"{self.head}"
        )

    def show_tail(self):
        print(
            f"{self.tail}"
        )

    def append(self, value):
        append_val = {
            'value': value,
            'next': None
        }

        if not self.head['next']['value']:
            del self.tail
            self.tail = append_val
            self.head['next'] = append_val
            self.length += 1
        else:
            current_tail = self.tail
            current_tail['next'] = append_val
            self.tail = append_val
            self.length += 1

mylinkedList = LinkedList(10)
mylinkedList.append(5)
mylinkedList.append(16)

print(mylinkedList.head)
print(mylinkedList.tail)
