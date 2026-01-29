# 🛍️ Customer Segmentation & Offer Recommendation System

## 📌 Project Overview

This project focuses on **Customer Segmentation** using unsupervised machine learning techniques and builds a simple **Marketing Offer Recommendation System** on top of it.

The goal is to:

* Understand customer behavior based on **Annual Income** and **Spending Score**
* Segment customers into meaningful groups
* Recommend **targeted marketing strategies** for each segment
* Compare **K-Means** and **DBSCAN** clustering techniques
* Deploy a **Streamlit web application** for real-time customer segmentation

This project is designed to be **industry‑ready**, **portfolio‑friendly**, and easy to understand for beginners.

---

## 🧠 Why Customer Segmentation?

Customer segmentation helps businesses:

* Identify high‑value customers
* Personalize marketing campaigns
* Increase customer retention
* Optimize discounts and promotions
* Improve ROI on marketing spend

Instead of treating all customers the same, segmentation allows **data‑driven decision making**.

---

## 📊 Dataset Used

**Mall Customers Dataset**

Features used in this project:

* `Annual Income (k$)`
* `Spending Score (1-100)`

These two features are widely used in real‑world marketing analytics.

---

## ⚙️ Technologies & Libraries

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit‑learn
* Streamlit

---

## 🔍 Data Preprocessing

* Selected relevant features (Income & Spending Score)
* Applied **StandardScaler** for feature normalization
* Scaling is mandatory because distance‑based algorithms are used

---

## 🔵 K‑Means Clustering

### 🔹 What is K‑Means?

K‑Means is a **distance‑based clustering algorithm** that groups data points into `k` clusters based on similarity.

### 🔹 How `k` was selected?

1. **Elbow Method** – minimizes WCSS (Within Cluster Sum of Squares)
2. **Silhouette Score** – measures cluster separation quality

Both methods suggested **k = 5** as the optimal number of clusters.

### 🔹 Why K‑Means is best for this project?

✔ Produces **clear & interpretable clusters**
✔ Easy to assign **new customers** to clusters
✔ Works very well with numerical marketing data
✔ Fast and scalable for large datasets
✔ Ideal for **real‑time recommendation systems**

That is why **K‑Means is chosen as the primary model** for customer segmentation and offer recommendation.

---

## 🟠 DBSCAN Clustering

### 🔹 What is DBSCAN?

DBSCAN is a **density‑based clustering algorithm** that can:

* Detect arbitrary shaped clusters
* Identify noise (outliers)

### 🔹 Why DBSCAN is included?

* To compare clustering behavior
* To show handling of noisy data

### 🔹 Limitations for this use case

❌ Cannot easily predict cluster for new customers
❌ Sensitive to `eps` parameter
❌ Less suitable for deployment systems

Hence, DBSCAN is used **only for comparison**, not for recommendation.

---

## 🎯 Customer Segments & Marketing Strategies

| Segment Type        | Description                  | Recommended Strategy                         |
| ------------------- | ---------------------------- | -------------------------------------------- |
| Premium Customers   | High income & high spending  | VIP offers, loyalty rewards, luxury products |
| Potential Customers | High income but low spending | Discounts, free trials, onboarding offers    |
| Deal Seekers        | Low income but high spending | Flash sales, coupons, bundle offers          |
| Low‑Value Customers | Low income & low spending    | Minimal marketing, automated emails          |
| Average Customers   | Moderate income & spending   | Seasonal & personalized offers               |

These strategies are mapped using **K‑Means cluster predictions**.

---

## 🚀 Streamlit Web Application

The Streamlit app allows:

* User to enter **Income & Spending Score**
* Predict customer segment using **trained K‑Means model**
* Display **personalized marketing offer**

This simulates a **real business use‑case**.

---

## 🖼️ Visualizations Included

All plots are saved and uploaded to GitHub for transparency:

* Elbow Method plot
* K‑Means cluster visualization
* DBSCAN k‑distance plot
* DBSCAN cluster visualization

---

## 📂 Project Structure

```
Customer-Segmentation-and-Offer-Recommendation/
├── images/
│   ├── elbow_method.png
│   ├── kmeans_clusters.png
│   ├── dbscan_k_distance.png
│   └── dbscan_clusters.png
├── notebooks/
│   └── customer_segmentation_analysis.ipynb
├── app.py
├── Mall_Customers.csv
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Run Streamlit app

```
streamlit run app.py
```

---

## 📈 Business Impact

* Enables targeted marketing
* Improves customer engagement
* Reduces marketing cost
* Data‑driven segmentation

---

## 🎯 Learning Outcomes

* Unsupervised learning
* K‑Means & DBSCAN comparison
* Feature scaling importance
* Model deployment using Streamlit
* Marketing analytics use‑case

---
## Live Demo :- https://customer-segmentation-offer-recommendation-using-k-means-f4v2d.streamlit.app/
## 👨‍💻 Author

**Satyam Kumar**
AI & Machine Learning Enthusiast

---

⭐ If you like this project, don’t forget to star the repository!
