class CountDown:
    def __init__(self, start):
        self.count = start + 1
    def __iter__(self):
        return self
    def __next__(self):
        self.count -= 1
        if self.count < 0:
            raise StopIteration
        return self.count
if __name__ == '__main__':
    counter = CountDown(5)
    for i in counter:
        print(i)