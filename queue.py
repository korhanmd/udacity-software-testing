import array

class Queue:
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if self.size == self.max:
            return False
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

def test1():
    msg = "test1 NOT OK"
    q = Queue(3)
    res = q.empty()
    if not res:
        print msg
        return
    res = q.enqueue(10)
    if not res:
        print msg
        return
    res = q.enqueue(11)
    if not res:
        print msg
        return
    x = q.dequeue()
    if x != 10:
        print msg
        return
    x = q.dequeue()
    if x != 11:
        print msg
        return
    res = q.empty()
    if not res:
        print msg
        return
    print "test1 OK"

def test2():
    msg = "test2 NOT OK"
    q = Queue(2)
    res = q.empty()
    if not res:
    	print msg
    	return
    res = q.enqueue(10)
    if not res:
    	print msg
    	return
    res = q.enqueue(11)
    if not res:
    	print msg
    	return
    res = q.enqueue(12)
    if res:
    	print msg
    	return
    x = q.dequeue()
    if x != 10:
        print msg
        return
    x = q.dequeue()
    if x != 11:
        print msg
        return
    x = q.dequeue()
    if x != None:
        print msg
        return
    res = q.empty()
    if not res:
        print msg
        return
    print "test2 OK"

test1()
test2()