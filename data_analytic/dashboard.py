import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set theme
sns.set_theme(style="whitegrid")

# Function to categorize NO2 levels
def categorize_no2(value):
    if value > 50:
        return "Buruk"
    elif value >= 30:
        return "Sedang"
    else:
        return "Baik"

# Create DataFrame
data_no2 = {
    'Station': ['Aotizhongxin', 'Nongzhanguan', 'Guanyuan', 'Gucheng', 'Dongsi', 'Tiantan', 'Changping', 'Shunyi', 'Huairou', 'Dingling'],
    'NO2': [59.31, 58.10, 57.90, 55.88, 53.70, 53.16, 44.19, 43.91, 32.51, 27.59]
}
df_no2 = pd.DataFrame(data_no2)

# Add category based on NO2
df_no2["Category"] = df_no2["NO2"].apply(categorize_no2)

# Streamlit
st.title("Air Quality Dashboard - NO2")

# Add filter based on category
selected_category = st.selectbox(
    "Choose Air Quality Category:", 
    ["Semua"] + list(df_no2["Category"].unique()), 
    key="no2_category"
)

# Filter data based on user choice
if selected_category != "Semua":
    df_filtered = df_no2[df_no2["Category"] == selected_category]
else:
    df_filtered = df_no2

# Select color based on quality
palette = {"Buruk": "red", "Sedang": "orange", "Baik": "green"}

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(x="NO2", y="Station", hue="Category", dodge=False, data=df_filtered, palette=palette)
plt.xlabel("NO2 Concentration")
plt.ylabel("Station")
plt.title("NO2 Levels Across Different Stations")

# Graph
st.pyplot(plt)


# SO2 Concentration Data
st.subheader("SO2 Concentration Across Months")

data_so2 = {
    'Month': ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    'SO2': [30.42, 26.97, 26.88, 13.67, 13.47, 7.48, 5.29, 4.37, 6.02, 8.39, 15.02, 24.25]
}

df_so2 = pd.DataFrame(data_so2)

# Add air quality categorize
def categorize_so2(value):
    if value > 25:
        return "Buruk"
    elif value >= 10:
        return "Sedang"
    else:
        return "Baik"

df_so2["Category"] = df_so2["SO2"].apply(categorize_so2)

# Streamlit
st.title("Air Quality Dashboard - SO2")

# Add filter based on category
selected_category = st.selectbox(
    "Choose Air Quality Category:", 
    ["Semua"] + list(df_so2["Category"].unique()), 
    key="so2_category"
)

# Filter data based on user choice
if selected_category != "Semua":
    df_filtered = df_so2[df_so2["Category"] == selected_category]
else:
    df_filtered = df_so2

# Select color based on quality
palette = {"Buruk": "red", "Sedang": "orange", "Baik": "green"}

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(x="SO2", y="Month", hue="Category", dodge=False, data=df_filtered, palette=palette)
plt.xlabel("SO2 Concentration")
plt.ylabel("Month")
plt.title("SO2 Levels Across Different Month")

# Graph
st.pyplot(plt)
