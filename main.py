import pandas 

#Print temp column
data = pandas.read_csv("weather_data.csv")

#Convert to dictionary
data_dict = data.to_dict()

#Convert to list 
#Not use for data frame
temp_list = data["temp"].tolist()

#Get average temp
average_temp = data["temp"].mean()

#Get maximum temp
max_temp = data["temp"].max()

#Get data in row
data_row = data[data.day == "Monday"]

#Get row which has highest temp
highest_temp = data[data.temp == data.temp.max()]

#Create variable for a row
monday = data[data.day == "Monday"]
monday_temp = monday.temp
f_monday = (monday_temp * 9/5) + 32

#Create Dataframe from scratch 
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("new_data.csv")


