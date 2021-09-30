#Python Remove Character from String using replace()

s = 'abc12321cba'

print(s.replace('a', ''))

#Output: bc12321cb

#**********************************************************************************

#Python Remove Character from String using translate()

s = 'abc12321cba'

print(s.translate({ord('a'): None}))

#Output: bc12321cb

#**********************************************************************************

#Remove specified number of times
s = 'abababab'
print(s.replace('a', 'A', 2))

#Output: AbAbabab


#**********************************************************************************

#If you want to replace multiple characters, that can be done easily using an iterator. Let’s see how to remove characters ‘a’, ‘b’ and ‘c’ from a string.

s = 'abc12321cba'

print(s.translate({ord(i): None for i in 'abc'}))

#Output: 12321
