import plotly.figure_factory as ff
import pandas as pd
df = pd.read_csv("rating.csv")
r = df["Avg Rating"].tolist()

fig = ff.create_distplot([r],["Average Rating"],show_hist=False)
fig.show()