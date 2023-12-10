# Advent of code
# first one
# goal: first and last digit, from 2-digit number, sum
# for every line of code:
# read first and last digit
# from 2-digit numer
# sum
# For example:For example: 1abc2, pqr3stu8vwx, a1b2c3d4e5f, treb7uchet
# 1abc2

results = []
f = open('firstone.txt', 'r')
for line in f:
    numbers = ""
    for char in line:
        if char.isnumeric():
            numbers += char
            break
    for char in reversed(line):
        if char.isnumeric():
            numbers += char
            break
    results.append(int(numbers))

total = sum(results)
print(total)
#lines = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
#numbers = ""
#for i in range(0, len(lines)):
 #   if lines[i] in ["0", "1","2", "3", "4", "5", "6", "7", "8", "9"]:
  #      numbers += lines[i]
#print(numbers) 