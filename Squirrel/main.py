import pandas
import os  
os.chdir("/Users/khaido/Library/CloudStorage/GoogleDrive-khaitroyy@gmail.com/My Drive/Code/day-25-Pandas-Library/Squirrel")

data = pandas.read_csv("squirrel_report.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")