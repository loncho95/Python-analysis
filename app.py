import csv
file = csv.reader(open('Resources/test.csv'), delimiter=';')

header = next(file)

# for row in file:
#     print(row)
# print(header)

# for column in header:
#     print (column) 

output = f'''

Total Clients:
Avarge Age:
Highest Balance:
Lowest Balance:
Longest months:
Shortest months:
'''

print(output)