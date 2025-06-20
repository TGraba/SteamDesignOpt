import pandas as pd
import os

# 1. Load normalized data
input_path = 'data/games_sample_normalized.csv'
df = pd.read_csv(input_path)

# 2. Compute summary statistics
stats = df.describe()

# 3. Print to console
print(stats)

# 4. Save to CSV next to the input file
output_dir = os.path.dirname(input_path)
stats.to_csv(os.path.join(output_dir, 'summary_statistics.csv'))
print(f"Summary statistics saved to: {os.path.join(output_dir, 'summary_statistics.csv')}")

