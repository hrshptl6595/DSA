class stack(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def push(self, value):
        oldstack = stack(self.value, self.next)
        self.value = value
        self.next = oldstack

    def pop(self):
        outputval = self.value
        self.value, self.next = self.next.value, self.next.next
        return outputval

    def peek(self):
        return self.value

    def size(self):
        numelements = 0
        nextval = self.next
        while (nextval != None):
            nextval = nextval.next
            numelements += 1
        return numelements

    def isEmpty(self):
        if (self.value == None):
            return True
        else:
            return False

if __name__ == "__main__":
    mystack = stack()
    mystack.push(10)
    print "Size = ", mystack.size()
    mystack.push(9)
    print "Size = ", mystack.size()
    mystack.push(15)
    print "Size = ", mystack.size()
    print mystack.pop()
    print mystack.pop()
    print mystack.peek()
    print mystack.pop()
    print mystack.isEmpty()