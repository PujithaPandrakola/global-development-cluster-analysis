# 🌍 Global Development Cluster Analysis using Machine Learning

## 📌 Project Overview

This project focuses on performing Cluster Analysis on a Global Development Measurement dataset using Machine Learning clustering algorithms.

The objective is to group countries based on economic, healthcare, population, and technological indicators such as:

- Birth Rate
- CO2 Emissions
- Energy Usage
- Internet Usage
- Life Expectancy
- Infant Mortality
- Population Statistics
- Health Expenditure

The project applies multiple clustering techniques and performs comparative analysis to identify the best clustering model.

---

# 🎯 Business Objective

To analyze global development indicators and cluster countries with similar development patterns for better understanding of:

- Developed Countries
- Developing Countries
- Underdeveloped Countries
- Emerging Economies
- Industrial Economies

This helps in:
- Economic analysis
- Policy planning
- International development studies
- Business expansion strategies

---

# 📂 Dataset Information

The dataset contains global development metrics for various countries.

### Features Used

- Birth Rate
- CO2 Emissions
- Days to Start Business
- Energy Usage
- Health Expenditure % GDP
- Infant Mortality Rate
- Internet Usage
- Lending Interest
- Life Expectancy Female
- Life Expectancy Male
- Mobile Phone Usage
- Population Statistics
- Population Urban

---

# ⚙️ Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

# 📊 Data Science Workflow

## 1. Data Cleaning
- Removed highly missing columns
- Removed constant columns
- Handled missing values
- Converted datatypes

## 2. Exploratory Data Analysis (EDA)
- Distribution Analysis
- Correlation Heatmap
- Outlier Detection
- Pattern Analysis

## 3. Data Preprocessing
- Feature Scaling using StandardScaler

## 4. Clustering Models
### KMeans Clustering
- Elbow Method
- Silhouette Score

### Hierarchical Clustering
- Dendrogram
- Agglomerative Clustering

## 5. Comparative Analysis
Compared models using Silhouette Score.

---

# 🤖 Machine Learning Models Used

| Model | Silhouette Score |
|-------|------------------|
| KMeans Clustering | 0.222 |
| Hierarchical Clustering | 0.254 |

### ✅ Best Model
Hierarchical Clustering achieved better cluster separation and compactness.

---

# 📈 Cluster Categories

The countries were grouped into:

- 🌱 Emerging Economies
- 🏆 Developed Countries
- ⚠️ Underdeveloped Countries
- 📈 Developing Countries
- 🏭 Industrial High Population Economies

---

# 📷 Visualizations

## Correlation Heatmap
Shows relationships between development indicators.

## Elbow Method
Used to determine optimal number of clusters.

## PCA Visualization
Visual representation of clustered countries.

---

# 🚀 Streamlit Deployment

The project was deployed using Streamlit for interactive cluster prediction.

---

# ▶️ How to Run the Project

## 1️⃣ Clone Repository

```bash
git clone <your-github-repo-link>
```

---

## 2️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run Streamlit App

```bash
streamlit run app/app.py
```

---

# 📁 Project Structure

```text
Global_Development_Clustering_Project/
│
├── data/
├── notebooks/
├── models/
├── app/
├── images/
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📌 Key Learnings

- Data Cleaning Techniques
- Exploratory Data Analysis
- Feature Scaling
- Unsupervised Learning
- KMeans Clustering
- Hierarchical Clustering
- PCA Visualization
- Streamlit Deployment

---

# 📬 Author

### Pandrakola Pujitha

Aspiring Data Scientist / Data Analyst

📍 Hyderabad, India

🔗 LinkedIn:
https://www.linkedin.com/in/pujithapandrakola

# 🌐 Live Demo

🔗 Streamlit Application:  
https://global-development-cluster-analysis-jhr973y4jk6cuvwkciq2pq.streamlit.app/

---

# ⭐ Conclusion

This project successfully analyzed global development indicators and grouped countries into meaningful clusters using Machine Learning clustering algorithms.

Comparative analysis showed that Hierarchical Clustering performed better than KMeans based on Silhouette Score evaluation.
