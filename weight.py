import plotly.figure_factory as pff
import pandas as pd
import csv

df = pd.read_csv('data.csv')

Fig = pff.create_distplot([df['Weight'].tolist()], ["Weight"], show_hist = False)
Fig.show()