# -----------------------------------
# declaring local arrayList
# -----------------------------------
vec1 = [5, 1, 7, 4, 9]
vec2 = [6, 8, 2, 5, 4, 3, 1]

#the first will NOT print 1, 5 and 4
# -----------------------------------
# Declaring a joins functions
# -----------------------------------
def Join():
    salida = []
    for act in vec1:
        control = act in vec2
        if control:
            salida.append(act)
        return salida
def FullJoin():
    salida2 = vec1
    for act in vec2:
        control = act in salida2
        if not control:
            salida2.append(act)
        return salida2



def FullOuterJoin(vec1, vec2):
    #This was the same one that was on the Exam practice D, I did it on my on :D
    exit = []

    for element in vec1:
        if element not in vec2:
            exit.append(element)

    for element in vec2:
        if element not in vec1:
            exit.append(element)
    return exit

resultFullOuterJoin = FullOuterJoin(vec1, vec2)

def RightJoin(vec1, vec2):
    exit = []

    for element in vec2:
        if element not in vec1:
            exit.append(element)
    return exit

resultRightJoin = RightJoin(vec1, vec2)






# -----------------------------------
# Executing joins functions
# -----------------------------------
print(Join())
print('')
print(FullJoin())
print()
print("Will print all numbers of the vectos but NOT the duplicated ones.")
print(resultFullOuterJoin)
print("")
print("On this Join, only will pint the uniques values of Vec2")
print(resultRightJoin)
