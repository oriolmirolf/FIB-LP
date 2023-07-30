
class Tree:
    def __init__(self, x):
        self.rt = x
        self.child = []
        
    def __iter__(self):
        yield self.rt
        queue = self.child
        while queue:
            node = queue.pop(0)
            yield node.rt
            queue += node.child
        
    def addChild(self, a):
        self.child.append(a)

    def ithChild(self, i):
        return self.child[i] 
