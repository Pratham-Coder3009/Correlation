from types import DynamicClassAttribute
import pandas as pd
import numpy as np 
import plotly.express as px

import csv

def getDataSource(data_path):
    Days_Present=[]
    Mark_Percentage=[]
    with open(data_path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            Days_Present.append(float(row["Days Present"]))
            Mark_Percentage.append(float(row["Marks In Percentage"]))
    
    return{"x":Days_Present,"y":Mark_Percentage}

def findCorrelation(datasource):
        correlation=np.corrcoef(datasource['x'],datasource['y'])
        print("Correlation between Days Present and Marks in Percentage:  \n",correlation[0,1])

def setup():
        data_path=r"C:\Users\prath\OneDrive\Desktop\Correlation\correlation-master\code3.csv"

        datasource=getDataSource(data_path)
        findCorrelation(datasource)
setup()