'''
historical
'''

#!!!
'''
Use 64bit pandas and numpy when load a very large data file, \
otherwise there might raise the memory error because 32bit packages only support for maximum 2GB memory.
'''

'''
SET the localhost 120.0.0.1, this can avoid the no-responding in calling Gaode API for http request.
'''











'''
20200306

DON'T initialize a dictionary with list/dict or other changable values when using fromkeys(), \
otherwise the value will be modified simultaneously
'''

#eg.
test = {}.fromkeys(['a','b','c'],{})
test['a']['aa'] = 1
print(test)

test = {}.fromkeys(['a','b','c'])
for key in test.keys():
    test[key] = {}
test['a']['aa'] = 1
print(test)


# To get multiple index slice of a dataframe, use tuple as the first arg for loc function
# https://blog.csdn.net/zou_gr/article/details/108798212



'''
Python 3 'class a(object):' is equal to 'class a:'
'''

'''
for distance unit calculation, use epsg=3857 so as the meter(s) is available to measure the distance between 2 points.
'''
