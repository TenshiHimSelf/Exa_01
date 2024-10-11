# import external libraries
import random
# store random value into cube
def iniCubo(cb):
    for fil in range(3):  #Only 3 Workers
        for col in range(5):  # Weeks
            for pro in range(5):  # Days
                cb[fil][col][pro] = random.randint(1, 12)  # Only 12 hours Works time
# print cube function
def impCubo(cb):
    workers_names = ["Tio Lucas", "Darna", "Elizabeth"]  # workers names
    for fil in range(3):  #Only 3 Workers
        print(f'Worker: {workers_names[fil]}')
        for col in range(5):  # Weeks
            print(f'  Week {col + 1}: ', end='')
            for pro in range(5):  # Days
                print(f'[Day {pro + 1}: {cb[fil][col][pro]:>3}]', end=' ')
            print()
        print('=====================================')

# declare data cube with format [3, 5, 5] was [5, 5, 5]
cubo = [[[0 for pro in range(5)] for col in range(5)] for fil in range(3)]

# call cube functions
iniCubo(cubo)
impCubo(cubo)
