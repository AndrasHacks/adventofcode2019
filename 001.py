input = open(r'001.input.txt','r')
lines = input.readlines()
summ = 0
for line in lines:
    summ = summ + (int(line) // 3 -2)
print(summ)
