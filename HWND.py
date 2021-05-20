import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import csv

df = pd.read_csv("PhoneData.csv")
avgRating = df["Avg Rating"].tolist()
fig = ff.create_distplot([avgRating], ["Average Rating"])
fig.show()