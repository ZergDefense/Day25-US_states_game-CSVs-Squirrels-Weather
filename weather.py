# with file.readlines():

# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# with csv.reader:

# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# with pandas:
import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()

sum_temp = 0
for temp in temp_list:
    sum_temp += temp
avg_temp = sum_temp/len(temp_list)
print(f"AVG temperature: {avg_temp.__round__(2)}°C")

print(data["temp"].mean())

# Get Data in Column
max_temp = data["temp"].max()
print(max_temp)
print(data.temp.max())

# Get Data in Row
print(data[data.day == "Monday"])

# Get Row with highest temp
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
print(f"Monday's temperature: {int(monday.temp) * 1.8 + 32}°F")

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
