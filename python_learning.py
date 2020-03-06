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
