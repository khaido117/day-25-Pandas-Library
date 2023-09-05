import pandas
import os  
os.chdir("/Users/khaido/Library/CloudStorage/GoogleDrive-khaitroyy@gmail.com/My Drive/Code/day-25-Pandas-Library/Squirrel")

#Count squirrel color.
data = pandas.read_csv("squirrel_report.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

#Create dictionary for squirrel color.

data_dict = {
    "Fur Color": ["Gray", "Cinamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

#Create csv report for squirrel color.
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")