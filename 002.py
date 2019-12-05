def fuel_for_fuel(fuel, summ):
    fuelfuel = fuel // 3 - 2
    if fuelfuel < 1:
        return summ
    else:
        return fuel_for_fuel(fuelfuel, summ + fuelfuel)

input = open(r'001.input.txt','r')
lines = input.readlines()
summ = 0
for line in lines:
    fuel = int(line) // 3 - 2
    summ = summ + fuel + fuel_for_fuel(fuel, 0
            )
print(summ)







