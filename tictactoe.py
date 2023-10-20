import random
def printField(field):
    for i in range(3):
        for j in range(3):
            print(field[i][j],end=" ")
        print()
    print()
def inputSpot(field,korz):
    printField(field)
    if(korz=='x'):
        korz = 'x'
    else:
        korz = '0'
    while(1):
        spotS = 0
        spotR = 0
        while(spotR<1 or spotR>3):
            spotR = int(input("Введите номер ряда клетки:"))
        while(spotS<1 or spotS>3):
            spotS = int(input("Введите номер столбца клетки:"))
        if(field[spotR-1][spotS-1] != '#'):
            continue
        else:
            field[spotR-1][spotS-1] = korz
            break
def newField():
    field = [['#', '#', '#'], ['#','#','#'], ['#', '#', '#']] 
    return field
def randomPC(field,korz):
    if(korz=='0'):
        korz = 'x'
    else:
        korz = '0'
    while(1):
        spotS = random.randint(1,3)
        spotR = random.randint(1,3)
        if(field[spotR-1][spotS-1] != '#'):
            continue
        else:
            field[spotR-1][spotS-1] = korz
            break     
def checkWinner(field):
    if field[0][0] == 'x' and  field[0][1] == 'x' and field[0][2] == 'x':
        print("Выйграли крестики!")
        printField(field)
        return True
    elif field[1][0] == 'x' and  field[1][1] == 'x' and field[1][2] == 'x':    
        print("Выйграли крестики!")
        printField(field)
        return True
    elif field[2][0] == 'x' and  field[2][1] == 'x' and field[2][2] == 'x':    
        print("Выйграли крестики!")
        printField(field)
        return True
    elif field[0][0] == 'x' and  field[1][0] == 'x' and field[2][0] == 'x':    
        print("Выйграли крестики!")
        printField(field) 
        return True
    elif field[0][1] == 'x' and  field[1][1] == 'x' and field[2][1] == 'x':    
        print("Выйграли крестики!")
        printField(field)
        return True
    elif field[0][2] == 'x' and  field[1][2] == 'x' and field[2][2] == 'x':    
        print("Выйграли крестики!")
        printField(field)
        return True  
    elif field[0][0] == 'x' and  field[1][1] == 'x' and field[2][2] == 'x':    
        print("Выйграли крестики!")
        printField(field)
        return True
    elif field[0][2] == 'x' and  field[1][1] == 'x' and field[2][0] == 'x':    
        print("Выйграли крестики!")
        printField(field)
        return True    
    if field[0][0] == '0' and  field[0][1] == '0' and field[0][2] == '0':
        print("Выйграли нолики!")
        printField(field)
        return True
    elif field[1][0] == '0' and  field[1][1] == '0' and field[1][2] == '0':    
        print("Выйграли нолики!")
        printField(field)
        return True
    elif field[2][0] == '0' and  field[2][1] == '0' and field[2][2] == '0':    
        print("Выйграли нолики!")
        printField(field)
        return True
    elif field[0][0] == '0' and  field[1][0] == '0' and field[2][0] == '0':    
        print("Выйграли нолики!")
        printField(field)
        return True
    elif field[0][1] == '0' and  field[1][1] == '0' and field[2][1] == '0':    
        print("Выйграли нолики!")
        printField(field)
        return True
    elif field[0][2] == '0' and  field[1][2] == '0' and field[2][2] == '0':    
        print("Выйграли нолики!")
        printField(field)
        return True  
    elif field[0][0] == '0' and  field[1][1] == '0' and field[2][2] == '0':    
        print("Выйграли нолики!")
        printField(field)
        return True
    elif field[0][2] == '0' and  field[1][1] == '0' and field[2][0] == '0':    
        print("Выйграли нолики!")
        printField(field)
        return True
    
while(1):
    kORz = 0
    while(kORz!='0' and kORz!='x'):
        kORz = str(input("Выберите сторону [x / 0]: "))
    field = newField()
    attemps = 0
    while(1):
        if(checkWinner(field)):
            break
        if(kORz=='x'):
            if(attemps!=9):
                inputSpot(field,kORz)
            else:   
                break
            attemps+=1
            if(attemps!=9):
                randomPC(field,kORz)
            else:
                break
            attemps+=1
        else:
            attemps+=1
            if(attemps!=9):
                randomPC(field,kORz)
            else:
                break
            if(attemps!=9):
                inputSpot(field,kORz)
            else:
                break
            attemps+=1
    cont = 0
    while(cont != 'y' and cont != 'n'):
        cont = str(input("Продолжить?[y/n]"))
    if(cont=='n'):
        break
