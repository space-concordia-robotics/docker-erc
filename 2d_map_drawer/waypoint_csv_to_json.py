import csv
points_dict = {}


with open('points.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count > 0:
            if(row[0]) == 'START':
                key = 0
            else:
                key = row[0]
            d = {str(key) : [row[1].replace(',', '.') ,row[2].replace(',', '.')]}
            points_dict.update(d)            
            
        line_count += 1
print(points_dict)

import json

with open('data.json', 'w') as fp:
    json.dump(points_dict, fp)
            
