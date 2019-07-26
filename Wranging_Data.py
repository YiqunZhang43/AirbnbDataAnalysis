import pandas as pd
import os
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
import sys
import numpy
from AirbnbDataAnalysis.Clean_data import Drop_NA_columns, Outliner_by_quartile, Outliner_by_sd, clean_unit, Category_to_One_Hot
from AirbnbDataAnalysis.Plotly_Chart import Make_a_Histrogram

def clean_data(file_path, threshold=0.75  ):
    data = pd.read_csv(file_path)
    data = Drop_NA_columns(data,threshold)
    data["Host_More_Than_3"] = data["host_total_listings_count"] >= 3
    data = clean_unit(['price','host_response_rate', 'host_acceptance_rate','extra_people','cleaning_fee'],data)
    data = Category_to_One_Hot(data, "amenities")
    return data

def return_figures():
    Figures = []
    df = clean_data("/Users/yiqunzhang/Downloads/boston-airbnb-open-data/listings.csv")
    Figures.append(Make_a_Histrogram("price","Host_More_Than_3",df))
    Figures.append(Make_a_Histrogram("minimum_nights","Host_More_Than_3",df))
    Figures.append(Make_a_Histrogram("availability_30","Host_More_Than_3",df))
    Figures.append(Make_a_Histrogram("review_scores_rating", "Host_More_Than_3",df))
    return Figures


#return_figures()

data = clean_data("/Users/yiqunzhang/Downloads/boston-airbnb-open-data/listings.csv",threshold=0.75 )
print(np.mean(data[data["Host_More_Than_3"] == False]["price"]))