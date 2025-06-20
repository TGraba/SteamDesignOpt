import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 1. Load raw data
input_path = 'data/games_sample.csv'
df = pd.read_csv(input_path)

# 2. Identify numeric columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

# 3. Apply Min-Max scaling to [0,1]
scaler = MinMaxScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# 4. Build output path in the same folder
base_dir, fname = os.path.split(input_path)
name, ext = os.path.splitext(fname)
output_path = os.path.join('data', 'games_sample_normalized.csv')

# 5. Save normalized data
df.to_csv(output_path, index=False)
print(f"Normalized dataset saved to: {output_path}")

