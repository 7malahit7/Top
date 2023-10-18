#bulls and cows

import random


attemps = 0
bulls = 0
cows = 0
computerArray = []


computerArray.append(random.randint(1,9))
for i in range(3):
    computerArray.append(random.randint(0,9))

# 0 - массив из уникальных чисел
# 1 - массив с повторяющимся числом

while(1):
    isnotUnique = False
    for i in range(4):
        for j in range(i+1,4):
            if computerArray[i]==computerArray[j]:
                isnotUnique = True
                break
        if(isnotUnique==True):
            break
    if(isnotUnique==True):
        computerArray = []
        computerArray.append(random.randint(1,9))
        for i in range(3):
            computerArray.append(random.randint(0,9))
        isnotUnique = True
    elif isnotUnique == False:
        break

       

while(bulls!=4):
    cows = 0
    bulls = 0
    userNumber = 0
    while(userNumber <=1000 or userNumber>=9999):
        userNumber = int(input("Введите четырех-значное число: "))
    userArray = []

    for i in range(4):
        userArray.append(userNumber%10)
        userNumber//=10
    for i in range(2):
        temp = userArray[i]
        userArray[i] =  userArray[4-i-1]
        userArray[4-i-1] = temp
    for i in range(4):
        for j in range(4):
            if computerArray[i] == userArray[j]:
                if i == j:
                    bulls+=1
                else:
                    cows+=1

    print(userArray)
    attemps+=1        
    print("быков: ",bulls)
    print("коров: ",cows)
print("Кол-во попыток: ",attemps)
