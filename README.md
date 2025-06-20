# Steam Game Design Optimization Framework

This repository contains the full Python pipeline used in the research paper:

**"Balancing Complexity and Perception: A Data-Driven Optimization Framework for Game Design"**  
Authors: Tvrtko Grabarić, Dijana Bratić (2025)

---

## 📌 Overview

This project implements a modular data-driven framework for analyzing and optimizing video game design. Using Steam metadata, it combines machine learning and linear programming to find feature combinations that maximize user-perceived value under resource constraints.

---

## 🧩 Project Structure

```
steam-optimization-framework/
├── data/
│   ├── games_sample.csv
│   └── games_sample_normalized.csv (generated)
├── eda_plots/ (generated)
├── check_libraries.py
├── normalization.py
├── descriptive_stats.py
├── vizualizationcorrelation.py
├── model_optimize.py
├── shap_summary.png (generated)
├── optimal_configuration.csv (generated)
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🛠 Installation

Clone the repository and install dependencies using pip:

```bash
git clone https://github.com/yourusername/steam-optimization-framework.git
cd steam-optimization-framework
pip install -r requirements.txt
```

---

## 📊 Dataset

The file `data/games_sample.csv` is a sample dataset extracted from SteamDB or similar public sources. It must include the following columns:

| Column              | Description                                   |
|---------------------|-----------------------------------------------|
| `tags_count`        | Number of tags/genres                         |
| `languages_count`   | Number of supported languages                 |
| `achievements_count`| Number of in-game achievements                |
| `playtime_forever`  | Total recorded playtime (in minutes)          |
| `positive_ratings`  | Count of positive user reviews                |
| `negative_ratings`  | Count of negative user reviews                |

---

## 🚀 Usage

Run the scripts **in this order**:

1. 🔍 **Check environment**
   ```bash
   python check_libraries.py
   ```

2. 🔄 **Normalize raw data**
   ```bash
   python normalization.py
   ```

3. 📈 **Descriptive statistics**
   ```bash
   python descriptive_stats.py
   ```

4. 🧠 **EDA and correlations**
   ```bash
   python vizualizationcorrelation.py
   ```

5. 🤖 **Train model + optimize features**
   ```bash
   python model_optimize.py
   ```

---

## 📤 Outputs

- `data/games_sample_normalized.csv` – scaled dataset
- `summary_statistics.csv` – descriptive stats
- `eda_plots/` – histograms and correlation heatmap
- `shap_summary.png` – global SHAP explanation plot
- `optimal_configuration.csv` – linear programming solution for optimal feature allocation

---

## 📘 Method Summary

- **Model**: XGBoost Regressor trained on normalized features.
- **Target variable**:  
  ```python
  target = positive_ratings / (positive_ratings + negative_ratings)
  ```
- **Explainability**: SHAP values used to derive feature importance.
- **Optimization**: `scipy.optimize.linprog` solves for optimal feature mix under constraint `∑x_i ≤ B`.

---

## 🔍 Citation

**Paper DOI**: _TBD_  
If using this code or method, please cite the original paper (to be linked upon publication).

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.

---

## ✉ Contact

For any questions or collaboration proposals, please contact:  
**Tvrtko Grabarić**  
University of Zagreb, Faculty of Graphic Arts  
tvrtko.grabaric@grf.hr