# **AdFlow-Budget-Optimizer**

**AdFlow-Budget-Optimizer** is a **real-time advertising budget estimation tool** designed to help marketing teams and businesses **optimize their daily ad spend**. The main goal of this project is to dynamically adjust the daily advertising budget based on key performance indicators, ensuring **maximum efficiency** and **improved ROI** for campaigns.

---

## **Project Overview**

Managing ad budgets effectively is one of the most challenging tasks in digital marketing. Traditional approaches often rely on **static budgets** or **manual adjustments**, which can lead to **underperformance** or **overspending**. 

**AdFlow-Budget-Optimizer** solves this problem by predicting the **optimal daily budget** for advertising campaigns using historical data and campaign-specific features.

The system leverages multiple features to make accurate predictions, with the **three most critical features** being:

- **Historical_Budget**: The budget allocated in previous campaigns or previous days.  
- **Leads_Forward**: The number of leads that successfully progressed to the next stage in the sales funnel.  
- **Leads_Rejected**: The number of leads that were rejected or disqualified.  

By analyzing these and other relevant features, the model can estimate a budget that balances **performance** with **cost efficiency**.

---

## **Models and Methodology**

I experimented with multiple machine learning approaches to find the most suitable model for this task:

- **Stochastic Decision Regressor (SDRegressor)**: This model showed the **best performance** in terms of **Mean Squared Error (MSE)**.  
- **Neural Network**: Performed reasonably, but slightly less effective compared to SDRegressor on this dataset.  

The workflow included:  

1. **Data preprocessing** – cleaning, scaling, and encoding features.  
2. **Feature selection** – identifying the most influential features for budget prediction.  
3. **Model training and evaluation** – using **cross-validation** to select the best model and tune hyperparameters.  
4. **Testing** – validating the model on **unseen test data** to ensure generalization and reliable predictions.  

The final **SDRegressor** model demonstrated robust performance and was able to predict daily budgets accurately, helping businesses **dynamically adjust spending** and **maximize campaign efficiency**.

---

## **Key Benefits**

- **Real-time budget adjustment**: Provides daily recommendations based on actual performance.  
- **Data-driven decisions**: Uses historical and campaign-specific features for optimal predictions.  
- **Improved ROI**: Helps marketers avoid overspending while maximizing leads and conversions.  
- **Flexible and scalable**: Can be integrated into various marketing platforms or dashboards.  

---

## **Future Improvements**

- Integrate more advanced **neural network architectures** for better predictions.  
- Include additional performance metrics such as **CTR** or **CPA**.  
- Develop a **user-friendly dashboard** for live monitoring and adjustments.  
- Extend the model to **predict budget allocation across multiple channels** simultaneously.  

---

## **Usage Example**

```python
from src.predict import predict

# Example input features
input_features = {
    "Historical_Budget": 1500,
    "Leads_Forward": 30,
    "Leads_Rejected": 5,
    # Add other features as needed
}

# Get predicted budget
predicted_budget = predict(input_features)
print(f"Recommended Daily Budget: ${predicted_budget:.2f}")
