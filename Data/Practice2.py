import numpy

df = numpy.array([(10,12,22,9,12,23,32)])
print "the orignal dataframe is \n", df
daily = numpy.divide(df[1:7], df[0:6]) -1
#numpy.insert(daily, 0, 0)
daily = numpy.insert(daily, 0, 0)
print "dataframe after calculaton is \n", daily
