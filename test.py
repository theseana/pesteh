a = ['apple', 'kiwi', 'banana']

#  اضافه میکنه
a.append('orange')
print(a)
# ['apple', 'kiwi', 'banana', 'ora
# nge']

# شماره پلاک
print(a.index('kiwi'))

# اخرین پلاک رو برمیداره
print(a.pop())
print(a)

b = ['Lemon']
a.extend(b)
print(a)


#پاک میکنه
a.remove('banana')
print(a)

# اضافه کردن به پلاک مشخصی
a.insert(1, 'watermelon')
print(a)