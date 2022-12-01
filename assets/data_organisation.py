import pandas as pd
import plotly.express as px

corruption_data = pd.read_csv("assets/corruption_index_data.csv")
GDP_data = pd.read_csv("assets/GDP_per_capita_data.csv")
main_data = corruption_data.merge(GDP_data)
graph_1 = px.histogram(main_data, x='GDP_per_capita', y='Country')
graph_2 = px.histogram(main_data, x='Index', y='Country')
