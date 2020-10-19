# IMPORT THE NEEDED LIBRARIES
import csv
import math

# READ THE CSV FILE
with open('data.csv',newline = '') as csv_data:
    reader = csv.reader(csv_data)
    file_data = list(reader)

# STORE THE DATA IN A LIST
data = file_data[0]

                #STANDARD DEVIATION STARTS


# TAKE OUT THE MEAN OF THE DATA
def MEAN(data):
    n = len(data)
    total = 0

    for x in data:
        total+=int(x)

    mean = total/n
    return mean

# SQUARING AND GETTING THE VALUES
squarelist = []

for number in data:
    a = int(number)-MEAN(data)
    a = a**2
    squarelist.append(a)


# GETTING THE SUM
sum = 0

for i in squarelist:
    sum = sum+i

# DIVIDING THE SUM BY THE TOTAL VALUES
result = sum/(len(data)-1)


# GETTING THE STANDARD DEVIATION BY GETTING THE SQUARE ROOT OF THE RESULT
standard_deviation = math.sqrt(result)
print("THIS IS THE STANDARD DEVIATION OF THE VALUES")
print(standard_deviation)
 