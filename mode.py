from collections import Counter
import csv
with open("HeightWeight.csv", newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []

for i in range(len(file_data)):
    n_num = file_data[i] [2]
    new_data.append(float(n_num))

data = Counter(new_data)
mode_data_for_range = {

                "100-110":0,
                "110-120":0,
                "120-130":0,
                "130-140":0,
                "140-150":0
         

                       }

for weight,occurance in data.items():
    if 100< float(weight) < 110:
        mode_data_for_range["100-110"] += occurance
    elif 110< float(weight) <120:
        mode_data_for_range["110-120"] +=occurance
    elif 120< float(weight) <130:
        mode_data_for_range["120-130"] +=occurance
    elif 130< float(weight) <140:
        mode_data_for_range["130-140"] +=occurance
    elif 140< float(weight) <150:
        mode_data_for_range["120-130"] +=occurance

mode_range ,mode_occurance =0,0

for range,occurance in mode_data_for_range.items():
    if occurance>mode_occurance:
        mode_range,mode_occurance = [int(range.split("-")[0]),int(range.split("-")[1])],occurance

mode = float((mode_range[0] + mode_range [1])/2)

print(f"mode is  -->  {mode:2f}" )