# Second problem
dict_numbers = {
    'oneight':'18', 'threeight':'38', 'fiveight':'58',
                  'nineight':'98', 'eightwo':'82', 'eighthree':'83',
                  'sevenine':'79','twone':'21',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

results = []
f = open('firstone.txt', 'r')
for line in f:
    for key, value in dict_numbers.items():
       line = line.replace(key, value)
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
print(results)
total = sum(results)
print(total)