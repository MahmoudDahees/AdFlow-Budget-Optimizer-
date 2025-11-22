import gradio as gd
import numpy as np
import pandas as pd
import joblib

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

def predict(platform, objective,ctr_est,cpc_est, cpc, conv_rate, budget, score, leads_fwd, leads_rej, qual_rate, active_leads):

    col = ['Platform', 'Objective', 'CTR_est', 'CPC_est', 'Historical_CPC',
       'Historical_ConvRate', 'Historical_Budget', 'Best_Source_Score',
       'Leads_Forward', 'Leads_Rejected', 'Qualification_Rate',
       'Active_Leads']
    platform_map = {"TikTok":0,"Facebook":1,"Google":2}
    objective_map = {"Traffic":0,"Awareness":1,"Conversions":2}
    
    X = pd.DataFrame([[platform_map[platform], objective_map[objective], ctr_est, cpc_est,
                   cpc, conv_rate, budget, score, leads_fwd, leads_rej,
                   qual_rate, active_leads]], columns=col)

    X = scaler.transform(X) 
    
    pred = model.predict(X)

    if pred < 0:
        pred = np.array([0])
    return "Best daily budget for your campaign is " + str(int(pred[0])) + "$"
