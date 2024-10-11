import random
# store random values into libraries
def iniCubo(cb):
    for fil in range(3):  # Only 2 workers
        for col in range(5):  # 5 weeks
            for pro in range(5):  # 5 days
                cb[fil][col][pro] = random.randint(1, 12)  # Solo 12 horas

# Print cube Funcion
def impCubo(cb):
    for fil in range(3):  # Only 3 workers
        print(f"Worker: {['Tio Lucas', 'Darna', 'Elizabeth'][fil]}")
        for col in range(5):  # 5 weeks
            print(f'Week {col + 1}: ', end="")
            for pro in range(5):  # 5 days
                print(f'[{cb[fil][col][pro]:>3}]', end="")
            print()
        print('=====================================')

# sum all days by weeks and get the total wooking hours
def sumaSemanas(cb):
    for fil in range(3):  # Only 3 workers
        total_horas = 0
        print(f"All working Hours by week for: {['Tio Lucas', 'Darna', 'Elizabeth'][fil]}:")
        for col in range(5):  # 5 Weeks
            suma = sum(cb[fil][col])  # sum all working hours
            total_horas += suma  # totalSum
            print(f"  Week {col + 1}: {suma} Hours")
        print(f"Total working hours: {total_horas}") #Total working hours
        print('=====================================')

# declare data cube with format [3,5,5] was [5,5,5] but I will only work with 3 workers a the same time
cubo = [[[0 for pro in range(5)] for col in range(5)] for fil in range(3)]

# call cube functions
iniCubo(cubo)
impCubo(cubo)
sumaSemanas(cubo)
