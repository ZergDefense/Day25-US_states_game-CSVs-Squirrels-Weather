import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Get Data in Column
# max_temp = data["temp"].max()
# print(max_temp)
# print(data.temp.max())

fur_list = data["Primary Fur Color"].to_list()
# print(fur_list)

num_of_gray = 0
num_of_cinnamon = 0
num_of_black = 0
for fur in fur_list:
    if fur == "Gray":
        num_of_gray += 1
    elif fur == "Cinnamon":
        num_of_cinnamon += 1
    elif fur == "Black":
        num_of_black += 1

fur_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [num_of_gray, num_of_cinnamon, num_of_black],
}
print(fur_dict)

squirrel_fur_table = pandas.DataFrame(fur_dict)
squirrel_fur_table.to_csv("squirrel_fur_table.csv")

furs = data["Primary Fur Color"].value_counts()
furs.to_csv("furs.csv")
print(furs)
