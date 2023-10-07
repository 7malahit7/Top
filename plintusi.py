def listOfFigures():
    print("""
             1  - плинтус слева
             2  - плинтус справа
             3  - плинтус слева на потолке
             4  - плинтус справа на потолке
             5  - равнобедренный треугольник с основанием слева
             6  - равнобедренный треугольник с основанием справа
             7  - равнобедренный треугольник с основанием снизу
             8  - равнобедренный треугольник с основанием сверху
             9  - часы 
             10 - бабочка
        """)

def figure1(size):
    for i in range(size):
        print(" ",end="")
        for j in range(size):
            if(i>=j):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def figure2(size):
    for i in range(size):
        print(" ",end="")
        for j in range(size):
            if(j > size - i - 2):
                print("*",end="")
            else:
                print(" ",end="")    
        print()

def figure3(size):
    for i in range(size):
        print(" ",end="")
        for j in range(size):
            if(j< size - i):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def figure4(size):
    for i in range(size):
        print(" ",end="")
        for j in range(size):
            if(i <= j):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def figure5(size):
    size//=2
    for i in range(size):
        print(" ",end="")
        for j in range(size):
            if(i>=j):
                print("*",end="")
            else:
                print(" ",end="")
        print()
    print(" ", end = "")
    for i in range(size//2+1):
        print("*", end="")
    print()
    figure3(size//2)

def figure6(size):
    figure2(size//2)
    for i in range(size//2+1):
        print("*", end="")
    print()
    figure4(size//2)

def figure7(size):
    for k in range(size):
        print(" ",end="")
    print("*",end="") 
    print()
    for i in range(size):
        for j in range(size):
            if(j > size - i - 2):
                print("*",end="")
            else:
                print(" ",end="")
        print("*",end="")
        for j in range(size):
            if(i>=j):
                print("*",end="")
            else:
                print(" ",end="")

        print()

def figure8(size): 

    for i in range(size):
        for j in range(size):
            if(i <= j):
                print("*",end="")
            else:
                print(" ",end="")
        print("*",end="")
        for j in range(size):
            if(j< size - i):
                print("*",end="")
            else:
                print(" ",end="")   
        print() 
    for k in range(size):
        print(" ",end="")
    print("*",end="") 
    print()
    
def figure9(size):
    size //= 2
    for i in range(size):
        print(" ",end="")
        for j in range(size):
            if(i>=j):
                print("*",end="")
            else:
                print(" ",end="")
               
        print(" ",end="")
        for j in range(size):
            if(j > size - i - 2):
                print("*",end="")
            else:
                print(" ",end="")    
        print()

    
    print(" ",end="")
    for i in range(size*2+1):
        print("*", end="")
    print()

    for i in range(size):
        print(" ",end="")
        for j in range(size):
            if(j< size - i):
                print("*",end="")
            else:
                print(" ",end="")
        print(" ",end="")
        for j in range(size):
            if(i <= j):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def figure10(size):
    size//=2
    for i in range(size):
        print(" ",end="")
        for j in range(size):
            if(i <= j):
                print("*",end="")
            else:
                print(" ",end="")
        print("*",end="")
        for j in range(size):
            if(j< size - i):
                print("*",end="")
            else:
                print(" ",end="")
        print()
    for i in range(size+1):
        print(" ",end="")
    print("*")
    for i in range(size):
        print(" ",end="")
        for j in range(size):
            if(j > size - i - 2):
                print("*",end="")
            else:
                print(" ",end="")   
        print("*",end="") 
        for j in range(size):
            if(i>=j):
                print("*",end="")
            else:
                print(" ",end="")
        print()
    
       

cont = "y"
size = 8   #примерный размер
while(cont == "y"):
    listOfFigures()
    choice = int(input("\nВыберите фигуру из списка выше: "))
    print("\n" * 100)  # чтобы другой текст не мешал
    if(choice == 1):
        figure1(size)
    elif(choice == 2):
        figure2(size)
    elif(choice == 3):
        figure3(size)
    elif(choice == 4):
        figure4(size)
    elif(choice == 5):
        figure5(size)
    elif(choice == 6):
        figure6(size)
    elif(choice == 7):
        figure7(size)
    elif(choice == 8):
        figure8(size)
    elif(choice == 9):
        figure9(size)
    elif(choice == 10):
        figure10(size)
    else:
        print("Неверный номер!")
    cont = str(input("Продолжаем? <y/n>: "))
