import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Real Estate Sales Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("Real_Estate_Sales_2001-2022_GL.csv", low_memory=False)
    df['Date Recorded'] = pd.to_datetime(df['Date Recorded'], errors='coerce')
    df['Year'] = pd.DatetimeIndex(df['Date Recorded']).year
    df['Month'] = pd.DatetimeIndex(df['Date Recorded']).month_name()
    return df

df = load_data()

# Title
st.title("🏠 Real Estate Sales Dashboard (2001-2022)")
st.markdown("Explore trends in property sales across Connecticut towns.")

# Sidebar Filters
st.sidebar.header("🔎 Filter Data")
towns = sorted(df['Town'].dropna().unique())
property_types = sorted(df['Property Type'].dropna().unique())
residential_types = sorted(df['Residential Type'].dropna().unique())
years = sorted(df['Year'].dropna().unique())

selected_towns = st.sidebar.multiselect("Select Town(s)", towns, default=towns[:5])
selected_property_types = st.sidebar.multiselect("Select Property Type(s)", property_types, default=property_types)
selected_res_types = st.sidebar.multiselect("Select Residential Type(s)", residential_types, default=residential_types)
selected_year_range = st.sidebar.slider("Select Year Range", int(min(years)), int(max(years)), (int(min(years)), int(max(years))))

# Apply filters
filtered_df = df[
    df['Town'].isin(selected_towns) &
    df['Property Type'].isin(selected_property_types) &
    df['Residential Type'].isin(selected_res_types) &
    df['Year'].between(selected_year_range[0], selected_year_range[1])
]

# Handle empty state
if filtered_df.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("🏘️ Total Properties Sold", f"{len(filtered_df):,}")
col2.metric("💸 Average Sale Amount", f"${filtered_df['Sale Amount'].mean():,.0f}")
col3.metric("📅 Year Range", f"{filtered_df['Year'].min()} - {filtered_df['Year'].max()}")

st.markdown("---")

# Sales Trend Over Time
st.subheader("📈 Sales Trend Over Time")
sales_trend = filtered_df.groupby('Year')['Sale Amount'].sum().reset_index()
fig1 = px.line(sales_trend, x='Year', y='Sale Amount', title="Total Sales Per Year")
st.plotly_chart(fig1, use_container_width=True)

# Sales by Property Type
st.subheader("📊 Sales by Property Type")
type_sales = filtered_df['Property Type'].value_counts().reset_index()
type_sales.columns = ['Property Type', 'Count']
fig2 = px.pie(type_sales, names='Property Type', values='Count', title="Sales Distribution by Property Type", hole=0.4)
st.plotly_chart(fig2, use_container_width=True)

# Top Towns by Number of Sales
st.subheader("🏘️ Top Towns by Number of Sales")
top_towns = filtered_df['Town'].value_counts().head(10).reset_index()
top_towns.columns = ['Town', 'Count']
fig3 = px.bar(top_towns, x='Town', y='Count', color='Town', title="Top 10 Towns by Number of Sales")
st.plotly_chart(fig3, use_container_width=True)

# Average Sale Amount by Town
st.subheader("💰 Average Sale Amount by Town")
avg_sale = filtered_df.groupby('Town')['Sale Amount'].mean().reset_index()
avg_sale = avg_sale.sort_values('Sale Amount', ascending=False).head(10)
fig4 = px.bar(avg_sale, x='Town', y='Sale Amount', title="Average Sale Amount by Town", color='Town')
st.plotly_chart(fig4, use_container_width=True)

# Heatmap: Sales Count by Town and Year
st.subheader("🌐 Sales Heatmap by Town and Year")
heatmap_df = filtered_df.groupby(['Town', 'Year']).size().unstack(fill_value=0)
fig5 = px.imshow(heatmap_df, labels=dict(x="Year", y="Town", color="Number of Sales"),
                 title="Heatmap of Sales Frequency", aspect="auto")
st.plotly_chart(fig5, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("📌 Use filters on the sidebar to explore specific trends in real estate sales.")
