n = 'pyThon pROgrAMMING'
m = '4258976413'
o = 'a45aw@!##'
l = 'python'
################################
print(n.capitalize())
# >>> 'Python programming'
################################
print(n.title())
# >>> 'Python Programming'
################################
print(n.count('M'))
#شمارش
# >>> 2
################################
print(n.endswith('M'))
# >>> False
print(n.endswith('G'))
# >>> True
################################
# شماره پلاک
print(n.find('G'))
# >>> 17
print(n.find('MING'))
# >>> 14
##################################
# شماره پلاک
print(n.index('G'))
# >>> 17
##################################
# عدد بودن رو چک میکند
print(n.isalnum())
# >>> False
print(m.isalnum())
# >>> True
print(o.isalnum())
# >>> False
##################################
# الفبا بودن را چک میکند
print(n.isalpha())
# >>> False
print(m.isalpha())
# >>> False
print(o.isalpha())
# >>> False
print(l.isalpha())
# >>> True
##################################
# حروف کوچک رو بررسی میکنه
print('python'.islower())
# >>> True
print('Python'.islower())
# >>> False
##################################
#حروف بزرگ رو بررسی میکنه
print('PYTHON'.isupper())
# >>> True
print('Python'.isupper())
# >>> False
# ###############################
print('PYTHON'.lower())
# >>> python
print('Python'.upper())
# >>> PYTHON
##################################
f = ['Banana', 'Kiwi', 'Apple']
'$$$'.join(f)
# >>> 'Banana$$$Kiwi$$$Apple
##################################
print('Banana$$$Kiwi$$$Apple'.replace('$', ' '))
# >>> 'Banana   Kiwi   Apple'
##################################
#برش
print('Banana$Kiwi$Apple'.split('$'))
# >>> ['Banana', 'Kiwi', 'Apple']
##################################
print('#$%#$%#$%#$%Banana Kiwi Apple$#$%#$%#$%'.strip('$#%'))
# >>> 'Banana Kiwi Apple'
##################################
print(n.startswith('p'))
# >>> True
print(n.startswith('P'))
# >>> False
##################################