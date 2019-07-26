#
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import numpy as np
from Detect_Outliner import Outliner_by_quartile
plotly.tools.set_credentials_file(username='Evazhang43', api_key='VEMecPY2nPLBiOCMycOS')
from Clean_data import clean_unit
#bar char is for count
def Bar_by_Group(column,group,data):
    result = data.groupby([group, column])[column].count().reset_index(name='count')
    trace1 = go.Bar(
        x=result[column],
        y=result[result[group] == True]["count"],
        name="Less"
    )

    trace2 = go.Bar(
        x=result[column],
        y=result[result[group] == False]["count"],
        name="More"
    )
    data = [trace1, trace2]
    layout = go.Layout(barmode="group")
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='grouped-bar')
    # result = pd.DataFrame(result)

#Histrogram is for quantative data
def Make_a_Histrogram(column, group, dataset):
    quartile = np.percentile(dataset[column], 75) - np.percentile(dataset[column], 25)
    MaxValue = np.percentile(dataset[column], 75) + 1.5 * quartile
    MinValue = max(np.percentile(dataset[column], 25) - 1.5 * quartile, 0)
    Professional = go.Histogram(
        x=Listings[dataset[group] == True][column],
        xbins=dict(
            start=MinValue,
            end=MaxValue,
            size=(MaxValue-MinValue)/10),
        histnorm='probability',
        opacity=0.75,
        name= "Professional"
    )
    Individual = go.Histogram(
        x=Listings[dataset[group] == False][column],
        xbins=dict(
            start=MinValue,
            end=MaxValue,
            size=(MaxValue - MinValue) / 10),
        histnorm='probability',
        opacity=0.75,
        name = "Individual"
    )
    layout = dict(title = column, barmode = "overlay", xaxis = dict(title = group), yaxis = dict(title = column))
    data = [Professional, Individual]
    layout = go.Layout(barmode='overlay')
    FigureDic = dict(data = data, layout = layout)
   # fig = go.Figure(data=data, layout=layout)
    return FigureDic
    #py.plot(fig, filename='overlaid histogram')

file_path = "/Users/yiqunzhang/Downloads/boston-airbnb-open-data/CleanedListing.csv"
Listings = pd.read_csv(file_path)
#Bar_by_Group("bathrooms", "host_more_than_4", Listings)
Make_a_Histrogram("availability_30","host_more_than_4", Listings )
#Outliner_by_quartile(Listings, "availability_30")