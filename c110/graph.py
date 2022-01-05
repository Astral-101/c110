import pandas as pd
import statistics as st
import random
import plotly.figure_factory as ff
import csv

df = pd.read_csv("averageData.csv")
averageList = df["average"].to_list()

def showPlotly(meanList):
    df = meanList
    fig = ff.create_distplot([averageList], ["average"], show_hist= False)
    fig.show()

def randomMean(counter):
    data = []
    for i in range(0, counter):
        randomIndex1 = random.randint(0, len(averageList) - 1)
        value = data[randomIndex1]
        data.append(value)
    mean = st.mean(data)
    return mean

# def setup():
#     meanList = []
#     for i in range(0, 1000):
#         meanSet = randomMean(100)
#         meanList.append(meanSet)
#     showPlotly(meanList)
#     mean = st.mean(meanList)
#     print(mean)

# setup()

def standardDeviation():
    meanList = []
    for i in range(0, 1000):
        meanSet = randomMean(100)
        meanList.append(meanSet)
    standard = st.stdev(meanList)
    return standard

standardDeviation()

