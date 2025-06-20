import os
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import shap
from sklearn.metrics import mean_squared_error, r2_score
from scipy.optimize import linprog
import matplotlib.pyplot as plt

# 1. Load normalized data
data_path = 'data/games_sample_normalized.csv'
df = pd.read_csv(data_path)

# 2a. Keep only numeric columns
numeric_df = df.select_dtypes(include=[np.number])

# 2b. Define features (X) and target (y)
drop_cols = ['num_reviews_total', 'pct_pos_recent', 'num_reviews_recent', 'appid', 'name']
features = [c for c in numeric_df.columns if c not in ['pct_pos_total'] + drop_cols]
X = numeric_df[features]
y = numeric_df['pct_pos_total']

# 3. Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Train XGBoost regressor
model = XGBRegressor(
    objective='reg:squarederror',
    random_state=42,
    n_estimators=200
)
model.fit(X_train, y_train)

# 5. Evaluate model
y_pred = model.predict(X_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2  = r2_score(y_test, y_pred)
print(f"Test RMSE: {rmse:.4f}")
print(f"Test R²:   {r2:.4f}")

# 6. Explain with SHAP
explainer   = shap.Explainer(model, X_train)
shap_values = explainer(X_train)

# Save SHAP summary plot
shap.summary_plot(shap_values, X_train, show=False)
shap_plot_path = os.path.join(os.path.dirname(data_path), 'shap_summary.png')
plt.savefig(shap_plot_path, bbox_inches='tight')
plt.close()
print(f"SHAP summary plot saved to: {shap_plot_path}")

# 7. Prepare for optimization
phi   = np.abs(shap_values.values).mean(axis=0)  # mean absolute SHAP per feature
costs = np.ones_like(phi)                         # unit cost for each feature
B     = 5.0                                      # total budget

# 8. Solve linear program: maximize phi·x s.t. costs·x ≤ B, 0 ≤ x ≤ 1
c      = -phi       # linprog minimizes, so invert sign
A_ub   = [costs]
b_ub   = [B]
bounds = [(0, 1) for _ in phi]

res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
x_opt = res.x

# 9. Report optimal configuration
opt_df = pd.DataFrame({
    'feature': features,
    'shap_weight': phi,
    'optimal_x': x_opt,
    'cost_per_unit': costs
})
opt_path = os.path.join(os.path.dirname(data_path), 'optimal_configuration.csv')
opt_df.to_csv(opt_path, index=False)
print(f"Optimal configuration saved to: {opt_path}")
