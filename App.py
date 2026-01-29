import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

st.set_page_config(page_title="Customer Offer Recommendation System", layout="wide")
st.title("Customer Offer Recommendation System")
st.write("Predict Customer segment & suggest best marketing offer using KMeans")
df = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Mall_Customers.csv")

x = df.iloc[:,[3,4]].values

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

kmeans = KMeans(n_clusters=5,init="k-means++",random_state=42)
labels = kmeans.fit_predict(x_scaled)

centers = scaler.inverse_transform(kmeans.cluster_centers_)

def marketing_strategy(cluster, centers):
    income, spending = centers[cluster]

    if income > 70 and spending > 70:
        return "💎 Premium Customers: VIP offers, loyalty rewards, luxury products"
    elif income > 70 and spending <= 40:
        return "🎯 Potential Customers: Discount coupons, free trials"
    elif income <= 40 and spending > 70:
        return "🔥 Deal Seekers: Flash sales, bundle offers"
    elif income <= 40 and spending <= 40:
        return "📉 Low-Value Customers: Minimal marketing, automated emails"
    else:
        return "🛒 Average Customers: Seasonal offers & personalized recommendations"



st.header("📊 Enter Customer Details")
income = st.number_input("Annual Income (k$")
spending = st.number_input("Spending Score (1-100")
if st.button("Predict Customer segemnt"):
    user_data = scaler.transform([[income,spending]])
    cluster = kmeans.predict(user_data)[0]

    st.success(f"Customer belongs to cluster {cluster}")
    st.info(marketing_strategy(cluster, centers))

