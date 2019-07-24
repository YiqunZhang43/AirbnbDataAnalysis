from AirBnbBoston import app
import json, plotly
from flask import  render_template
import sys
#sys.path.insert(0,"/Users/yiqunzhang/Airbnb/AirbnbDataAnalysis")
from Wranging_Data import return_figures

@app.route('/')

@app.route('/index')
def index():
    figures = return_figures()
    ids = ["figure-{}".format(i) for i,_ in enumerate(figures)]
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html',
                           ids = ids,
                           figuresJSON=figuresJSON)