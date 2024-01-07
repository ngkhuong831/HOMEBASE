import csv
from statistics import mean

def get_data_from_csv(csv_file):
    data = []
    try:
        with open(csv_file, mode='r', encoding='utf8') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Read the headers
            age_index = headers.index('Age')
            for row in reader:
                data.append(int(row[age_index]))
        return data
    except FileNotFoundError:
        print('File not existed!')
    except csv.Error as e:
        print('Error: ', e)

# Demonstration

# Get data
ageList = get_data_from_csv(csv_file = 'data.csv')

# Calculate Average Age
if ageList:
    print('Average Age:', mean(ageList))
else:
    print('No valid age values found!')