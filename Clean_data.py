import pandas as pd
import os
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)


def Drop_NA_columns(data, threshold):
    column_filter = pd.DataFrame(data.isnull().sum() / data.shape[0] > threshold, columns=["NA_percent"])
    data = data.drop(pd.Series(column_filter[column_filter["NA_percent"]].index), axis=1)
    return data

def clean_unit(column, dataset):

    for i in column:
        print(i)
        dataset[i] = pd.to_numeric(dataset[i].astype(str).str.replace(r"[%$,]", ""),errors='coerce')
    return dataset

def Category_to_One_Hot(dataset, columns):
    dataset = pd.merge(dataset.drop([columns], axis=1), dataset[columns].str.get_dummies(sep=","),
                        left_index=True, right_index=True)
    return dataset

def Outliner_by_sd(dataset, columns):
    max = np.mean(dataset[columns]) + 3 * np.std(dataset[columns])
    min = np.mean(dataset[columns]) - 3 * np.std(dataset[columns])
    dataset = dataset[(dataset[columns] > min) | (dataset[columns] < max)]
    return dataset

def Outliner_by_quartile(dataset, columns):
    quartile = np.percentile(dataset[columns], 75)-np.percentile(dataset[columns], 25)
    max = np.percentile(dataset[columns], 75) +1.5*quartile
    min = np.percentile(dataset[columns], 25) -1.5*quartile
    dataset = dataset[(dataset[columns] > min) | (dataset[columns] < max)]
    return dataset

#Cleaning the Data
#1. find out what the dataset is by looking at the columns
#it is very important to understand what each table and columns represents.
#we can actually drop the neighborhood, because we hae neighborhood_cleased
Listings = pd.read_csv("/Users/yiqunzhang/Downloads/boston-airbnb-open-data/listings.csv")
Listings = clean_unit(['host_response_rate', 'host_acceptance_rate', "price"], Listings)