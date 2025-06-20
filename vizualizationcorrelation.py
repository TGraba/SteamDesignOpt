import os
import ast
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load normalized data
input_path = 'data/games_sample_normalized.csv'
df = pd.read_csv(input_path)

# 2. Convert supported_languages from string‐list to count
#    e.g. "['English','French',…]" → 2, 3, …
df['supported_languages_count'] = df['supported_languages'].apply(
    lambda x: len(ast.literal_eval(x)) if pd.notna(x) else 0
)

# 3. Prepare output folder
output_dir = os.path.join(os.path.dirname(input_path), 'eda_plots')
os.makedirs(output_dir, exist_ok=True)

# 4. Histograms for key numeric variables
vars_to_plot = [
    'dlc_count',
    'achievements',
    'supported_languages_count',
    'average_playtime_forever',
    'pct_pos_total'
]

for col in vars_to_plot:
    plt.figure(figsize=(6,4))
    plt.hist(df[col].dropna(), bins=30, edgecolor='black')
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.tight_layout()
    fn = os.path.join(output_dir, f'{col}_histogram.png')
    plt.savefig(fn)
    plt.close()
    print(f"Saved histogram: {fn}")

# 5. Correlation heatmap on the same variables
corr = df[vars_to_plot].corr()

plt.figure(figsize=(6,5))
plt.imshow(corr, cmap='viridis', interpolation='nearest')
plt.colorbar(label='Pearson r')
plt.xticks(range(len(vars_to_plot)), vars_to_plot, rotation=45)
plt.yticks(range(len(vars_to_plot)), vars_to_plot)
plt.title('Correlation Heatmap')
plt.tight_layout()
heatmap_fn = os.path.join(output_dir, 'correlation_heatmap.png')
plt.savefig(heatmap_fn)
plt.close()
print(f"Saved correlation heatmap: {heatmap_fn}")
