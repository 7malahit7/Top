#bulls and cows

import random


attemps = 0
bulls = 0
cows = 0
computerArray = []


computerArray.append(random.randint(1,9))
for i in range(3):
    computerArray.append(random.randint(0,9))

# Массив из уникальных чисел
while(1):
    isUnique = False
    for i in range(4):
        for j in range(i+1,4):
            if computerArray[i]==computerArray[j]:
                isUnique = True
                break
        if(isUnique==True):
            break
    if(isUnique==True):
        computerArray = []
        computerArray.append(random.randint(1,9))
        for i in range(3):
            computerArray.append(random.randint(0,9))
        isUnique = True
    elif isUnique == False:
        break
               
print(computerArray)
while(bulls!=4):
    cows = 0
    bulls = 0
    userNumber = int(input("Введите четырех-значное число: "))
    userArray = []
    
    for i in range(4):
        userArray.append(userNumber%10)
        userNumber//=10
    for i in range(2):
        temp = userArray[i]
        userArray[i] =  userArray[4-i-1]
        userArray[4-i-1] = temp

    for i in computerArray:
        if(i in userArray):
            for j in range(4):
                if (userArray[j]==computerArray[j]):
                    bulls+=1
                    break
                else:
                    cows+=1
                    break
    print(computerArray)
    print(userArray)        
    print("быков: ",bulls)
    print("коров: ",cows)
