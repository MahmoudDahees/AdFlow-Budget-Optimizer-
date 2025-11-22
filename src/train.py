
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("G:\ML projects\Projects\AdFlow Budget Optimizer\Data\marketing_dataset_USA_daily_2000.csv")
data = data.drop("Campaign_ID",axis=1)
pd.set_option('display.float_format', '{:.10f}'.format)

data.iloc[:,0] = data.iloc[:,0].map({"TikTok":0,"Facebook":1,"Google":2}).astype(float)
data.iloc[:,1] = data.iloc[:,1].map({"Traffic":0,"Awareness":1,"Conversions":2})

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler

x = data.drop("Suggested_Budget",axis=1)
y = data["Suggested_Budget"]
y
x_temp,x_test,y_temp,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
x_train,x_cv,y_train,y_cv = train_test_split(x_temp,y_temp,test_size=0.3,random_state=42)

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_cv = scaler.transform(x_cv)
x_test = scaler.transform(x_test)

model = SGDRegressor()
model.fit(x_train,y_train)

import joblib
joblib.dump(model,"model.pkl")
joblib.dump(scaler,"scaler.pkl")
