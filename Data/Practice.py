import numpy as np

def test_run():
    np.random.seed(695)
    a = np.random.randint(0, 1000, size = (5, 4))
    print "Array:\n", a
    print a.shape
    print "sum of each column:\n", a.sum(axis = 0)
    print "Sum of each row:\n", a.sum(axis = 1)
    print "min of each column\n", a.min(axis = 0)
    print "max of each row:\n", a.max(axis = 1)
    print "mean of all elements\n", a.mean()
    print "max of all elements\n", a.argmax()
    print "element at position 3, 2", a[3, 2]
    print "now check sliced version", a[0:2, 1:3]
    print "3 way slcing\n", a[:, 0:3:2]
    #n:m:t starts at n, stops before m, step size 2, omits every other step
#    a[0, 0] = 1
#    a[:,:] = -1
#    a[:,3] = [1,2,3,4,5]
    indices = np.array([(1,1,2,3)])
    print "indices vector is ", indices
    print "a vector is ", a
    print a[indices]

    np.random.seed(452)
    b = np.random.randint(0, 1000, size = (5, 4))
    print b

    mymean = b.mean()
    print mymean
    #here b < mymean;;  replaces all instances where b < mymean
    b[b<mymean] = mymean
    print "new b is \n", b

    np.random.seed(237)
    c = np.random.randint(0, 100, size = (5, 1))
    print "c is \n", c
    print c * 2

    # here it is element wise multiplication
    print c*b
if __name__ == "__main__":
    test_run()