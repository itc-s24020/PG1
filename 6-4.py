class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        # MyIterator  が __next() を実装しているのでselfをイテレータとして返す
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration()
        value = self.data[self.index]
        self.index = self.index + 1
        return value

# シーケンスの一例として文字列を渡す
itr = MyIterator("spam")
for char in itr:
    print(char, end=" ")

class Reverse:
    '''シーケンスを逆順にループするイテレータ'''

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

# シーケンスの一例として文字列を渡す
rev = Reverse('spam')
for char in rev:
    print(char, end=" ")                                    
