import pandas 

#Print temp column
data = pandas.read_csv("weather_data.csv")
print(data["tempt"])
