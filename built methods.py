cartoons=['tom & jerry','dora','bujji','ben-ten','little krishna','doraemon']
print(cartoons)
print("after appending an element:")
cartoons.append('oggy & cockroach')
print(cartoons)
print('after inserting element')
cartoons.insert(2,'roll no 21')
print(cartoons)
print('after popping element')
cartoons.pop()
print(cartoons)
cartoons.pop(3)
print(cartoons)
cartoons.remove('dora')
print(cartoons)
print(cartoons.index('ben-ten'))
print("after reversing the list:")
cartoons.reverse()
print(cartoons)