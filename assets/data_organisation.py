from pandas import read_csv
from plotly.express import histogram

corruption_data = read_csv("assets/corruption_index_data.csv")
GDP_data = read_csv("assets/GDP_per_capita_data.csv")
main_data = corruption_data.merge(GDP_data)  # merge corruption_data and GDP_data dfs by the 'coutry' column
graph_1 = histogram(main_data, x='GDP_per_capita', y='Country')  # graph that shows GDP per capita of countries
graph_2 = histogram(main_data, x='Index', y='Country')  # graph that shows corruption index of countries
