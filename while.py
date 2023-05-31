n = 5
while n>10:
    print (n)
    n = n+1
print('off')
"""
while True:
    line = input('> ')
    if line == 'done':
        break
print(line)
print('Done!')
"""
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
