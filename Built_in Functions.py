""" built in functions """
''' sort'''
# print(sorted([1,2,3,9,4,11,6]))
# print(sorted((1,2,3,9,4,11,6)))
# print(sorted({1,2,3,9,4,11,6}))
# print(sorted(['a','A','Z','z']))
# print(ord('G'))   
# print(chr(89))

''' all method ''' # any 1 arguement is false output will be false

# print(all([True,1,2,'e']))
# print(all([True,1,2,'']))
# print(all([True,1,2,'False']))
# print(all([True,1,2,None]))

''' any method'''  # any 1 argument is true  output will be true

# print(any([True,False,'h']))
# print(any(['g',False,]))
# print(any([True,False,]))
# print(any([None,False,'',0]))

''' bool method '''

# print(bool(0))
# print(bool(True))
# print(bool(False))
# print(bool(None))
# print(bool(''))
# print(bool(' '))
# print(bool('  '))

''' eval '''

# a=print(eval('5+6.8-1'))
# b=print(eval('4+6.8-11'))
# print(a,type(a))
# print(b,type(b))

''' sum method '''

# print(sum([1,2,3,4,5]))
# print(sum((1,2,3,4,50)))

''' reversed list'''

# for i in reversed ([1,2,3,4,]):
#     print(i)

''' reversed tuple'''

# for i in reversed ((19,20,22,23,24)):
#     print(i)


''' enumerates '''

a=['bread','milk','python']
# b=enumerate(a)
# print(list(b))
# print(tuple(b))
# print(dict(b))

# a=['bread','milk','python']
# b=enumerate(a,10)
# b=enumerate(a,-3)
# print(list(b))

''' doc string''' # used to print code in the comments

def gm():
    '''jagadishkajgsjgfjvsahkdfvh'''
print(gm.__doc__)   

