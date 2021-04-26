class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_

class LinkedList:
    
    def __init__(self, collection=None):
        self.head = None

        if collection:
            for item in reversed(collection): 
                self.insert(item)

# add ability to be used in a for in loop
    def __iter__(self):
        def value_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return value_generator()
# Use dunder methods make your code more readable and elegant
    def __str__(self):
        out = ''
        for value in self:
            out += f'[ {value} ] -> '
        out += 'None'
        return out
# Use dunder methods make your code more readable and elegant
    def __len__(self):
        return len(list(iter(self)))

# add ability for two custom data structure to be considered equal
    def __eq__(self, other):
        return list(self) == list(other)

    def __getitem__(self, index):
        for i, item in enumerate(self):
            if i == index:
                return item

        raise IndexError

    def insert(self, value):
            self.head = Node(value, self.head)

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node


# add ability to convert to a list or other collection type
def convert_list_to_tuple(input_list):
    return tuple(input_list)

# add ability to be used in a list comprehension
def rtn_words_with_a_specific_letter(iterable_list, required_letter):
    return [x for x in iterable_list if required_letter in x]
