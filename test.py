import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data (You can replace this with your own dataset)
@st.cache_data
def load_data():
    # Sample sales data for demonstration
    data = {
        'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
        'Sales': np.random.randint(100, 1000, size=100),
        'Category': np.random.choice(['Electronics', 'Clothing', 'Home Appliances'], size=100),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], size=100),
        'Profit': np.random.uniform(10, 300, size=100)
    }
    df = pd.DataFrame(data)
    return df

# Load the dataset
df = load_data()

# Streamlit UI components
st.title("Sales Data Dashboard")

# Sidebar filters
st.sidebar.header("Filter Data")
category_filter = st.sidebar.multiselect("Select Categories", options=df['Category'].unique(), default=df['Category'].unique())
region_filter = st.sidebar.multiselect("Select Regions", options=df['Region'].unique(), default=df['Region'].unique())

# Apply filters
filtered_data = df[(df['Category'].isin(category_filter)) & (df['Region'].isin(region_filter))]

# Show filtered data table
st.subheader("Filtered Sales Data")
st.dataframe(filtered_data)

# Show basic statistics
st.subheader("Summary Statistics")
st.write(filtered_data.describe())

# Total Sales and Profit
st.subheader("Total Sales and Profit")
total_sales = filtered_data['Sales'].sum()
total_profit = filtered_data['Profit'].sum()
st.write(f"Total Sales: ${total_sales:,.2f}")
st.write(f"Total Profit: ${total_profit:,.2f}")

# Visualize Sales by Category
st.subheader("Sales by Category")
category_sales = filtered_data.groupby('Category')['Sales'].sum().sort_values()
fig, ax = plt.subplots()
category_sales.plot(kind='bar', ax=ax, color='skyblue')
ax.set_title("Sales by Category")
ax.set_xlabel("Category")
ax.set_ylabel("Sales")
st.pyplot(fig)

# Visualize Sales over Time
st.subheader("Sales Over Time")
daily_sales = filtered_data.groupby('Date')['Sales'].sum()
fig, ax = plt.subplots()
daily_sales.plot(kind='line', ax=ax, color='green')
ax.set_title("Daily Sales Trend")
ax.set_xlabel("Date")
ax.set_ylabel("Sales")
st.pyplot(fig)

# Visualize Profit by Region
st.subheader("Profit by Region")
region_profit = filtered_data.groupby('Region')['Profit'].sum().sort_values()
fig, ax = plt.subplots()
region_profit.plot(kind='pie', ax=ax, autopct='%1.1f%%', colors=sns.color_palette("Set2", n_colors=4).as_hex())
ax.set_title("Profit Distribution by Region")
st.pyplot(fig)

# Conclusion or additional insights
st.subheader("Conclusion")
st.write("""
- This dashboard provides insights into sales data based on different categories and regions.
- You can filter the data to focus on specific regions or categories and explore the overall trends.
""")