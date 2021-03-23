from queue import Queue

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

def test3():
    msg = "test3 NOT OK"
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
    res = q.full()
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
    print "test3 OK"

test1()
test2()
test3()