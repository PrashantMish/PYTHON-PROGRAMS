for i in range(1,11):
    if i == 5:
        break
    print(i,end=' ')
print()
# Output -> 1 2 3 4

for i in range(1, 11):
    if i == 5:
        continue
    print(i,end=' ')
print()
# Output -> 1 2 3 4 6 7 8 9 10

for i in range(1, 11):
    if i == 5:
        pass
    print(i,end=' ')

# Output -> 1 2 3 4 5 6 7 8 9 10
