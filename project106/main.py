from statistics import correlation
import plotly.express as px
import csv
import numpy as np
from statistics import correlation

def Plot(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x = "Days Present", y = "Marks in Percentage")
        fig.show()

def getDataSource(data_path):
    marks = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks in %"]))
            days_present.append(float(row["Days Present"]))

        
    return{"x": marks, "y": days_present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("The Correlation is: ", correlation(0,1))

def setup():
    data_path = "./data/gradesvsdays.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    Plot(data_path)

setup()