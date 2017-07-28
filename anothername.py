import random
numbers = []

mylist = 0
while mylist < 100:
    numbers.append(random.randint(0,10000))
    mylist = mylist + 1

numbers2 = sorted(numbers)

print(numbers2)


found = False
x = 0


while x < (len(numbers2)-1) and found == False:
    if numbers2[x] == numbers2[x-1] or numbers2[x] == numbers2[x+1]:
        found = True
        print('you have repeating numbers in your list')
        print(numbers2[x])
    else:
        x = x + 1
    #



if found == False:
    print('your list has no repeating numbers')
