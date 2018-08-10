class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        self.push(nestedList)

    def push(self, l):
        for s in l:
            if type(s) is list:
                for i in s:
                    self.stack.append(i)
            else:
                self.stack.append(s)

    def next(self):
        """
        :rtype: int
        """
        l = self.stack.pop()
        return l


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack

i, v = NestedIterator([[1,1],2,[1,1]]), []
while i.hasNext():
    v.append(i.next())
print(v)
