import random
print('this')

i = 6
print(i)
j = 9
#                  1 
#         012345678901234
parrot = 'Norwegian Blue'

print(parrot[0])


letters = "abcdefghijklmnopqrstuvwxyz"

print(letters[25::-1])


name = 'ted'

print(1 + 2, 3 * 4, "Equal?")
print('the name, "' + name + '" has a basis.')

for s in range(1 , 6):
     print('the name, "' + name + '" has a basis.')
     print(s)
     s+=s
     print(s)
print(s)



for i in range(1, 100):
    # print (i)
    if i % 11 == 0:
        print (i)
        break


for i in range(21):
    if i == 0 or (i % 3 == 0 or i % 5 ==0):
        continue
    print (i)



highest = 10

answer = random.randint(1,highest)
user_answer = int(input("Enter a random number between1 & {}".format(highest)))
while user_answer != answer:
    if 0 < user_answer < answer:
        user_answer = int(input("Guess higher"))
        continue
    elif user_answer > answer:
        user_answer = int(input("Guess lower"))
        continue
    elif user_answer == 0:
        print('y u quit tho?')
        break
    print("you got it right!")