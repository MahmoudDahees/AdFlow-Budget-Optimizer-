from src.predict.py import predict
import gradio as gd

interface = gd.Interface(
    fn=predict,
    inputs=[
        gd.Dropdown(choices=["TikTok","Facebook","Google"], label="Platform"),
        gd.Dropdown(choices=["Traffic","Awareness","Conversions"], label="Objective"),
        gd.Slider(minimum=0, maximum=3, step=0.01, label="CTR_est"),
        gd.Slider(minimum=0, maximum=3, step=0.01, label="CPC_est"),
        gd.Slider(minimum=0, maximum=3, step=0.01, label="Historical_CPC"),
        gd.Slider(minimum=0, maximum=1, step=0.01, label="Historical_ConvRate"),
        gd.Slider(minimum=0, maximum=20000, step=100, label="Historical_Budget"),
        gd.Slider(minimum=0, maximum=1, step=0.01, label="Best_Source_Score"),
        gd.Slider(minimum=0, maximum=100, step=1, label="Leads_Forward"),
        gd.Slider(minimum=0, maximum=100, step=1, label="Leads_Rejected"),
        gd.Slider(minimum=0, maximum=1, step=0.01, label="Qualification_Rate"),
        gd.Slider(minimum=0, maximum=100, step=1, label="Active_Leads")
    ],
    outputs=gd.Text(),
    title="Ads Budget Predictor",
)

interface.launch()

