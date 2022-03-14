class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val

class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum1 = 0
        self.__sum2 = 0

    def get_counter(self):
        return self.__sum1
        return self.__sum2

    def push(self, val):
        self.__sum1 += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum2 -= val
        return val

stk = CountingStack()

for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
