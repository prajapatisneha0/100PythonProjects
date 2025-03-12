from calendar import month

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

#  average = sum(temp_list) / len(temp_list)
#  print(average)
#
# print(data["temp"].mean())
# print(data["temp"].max())

# Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# Get data in columns
# print(data["condition"])
# print(data.condition)

# Covert celsius to fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250129.csv")
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(cinnamon_squirrels_count)
# print(black_squirrels_count)
#
# data_dict ={
#     "Fur Color" : ["Gray", "Cinnamon", "Black" ],
#     "Count" : [grey_squirrels_count , cinnamon_squirrels_count , black_squirrels_count]
# }
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")


