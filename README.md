# Housing Price Prediction

A simple machine learning pipeline to predict housing prices using Ridge Regression. It includes data preprocessing (outlier removal, categorical encoding) and model evaluation.

## Usage

1. **Preprocess the data:** 
   Cleans the raw data, removes extreme top 10% outliers, and encodes categorical variables.
   ```bash
   python preprocess.py
   ```
   *(This generates `Housing_processed.csv`)*

2. **Train and evaluate the model:** 
   Scales the features, trains a Ridge Regression model, and prints evaluation metrics.
   ```bash
   python main.py
   ```

## 📊 Expected Metrics

After running `main.py`, you will see evaluation metrics similar to these *(exact values may vary slightly)*:

```text
--- Model Evaluation ---
MSE  : 563979885676.506
MAE  : 575568.2536289269
R2   : 0.6989346447565128
```

**Metric Breakdown:**
* **R² Score (~0.69):** The model explains roughly 69% of the variance in housing prices.
* **MAE (~575568):** The average absolute difference between predicted and actual prices.
