import plotly.figure_factory as pff
import pandas as pd
import csv

df = pd.read_csv('data.csv')

Fig = pff.create_distplot([df['Height'].tolist()], ["Height"], show_hist = True)
Fig.show()