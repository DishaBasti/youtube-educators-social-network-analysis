import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from io import BytesIO
import networkx as nx
from itertools import combinations
import community.community_louvain as community_louvain
from networkx.algorithms.community import label_propagation_communities, girvan_newman
from prophet import Prophet
from sklearn.cluster import KMeans

# Set Page Configurations
st.set_page_config(page_title="YouTube Educators Dashboard", layout="wide")

# Color Scheme and Theme
primary_color = "#1D1616"  # Dark mode by default
dark_color = "#8E1616"
accent_color = "#D84040"
light_color = "#EEEEEE"

# Apply CSS for Styling
st.markdown(
    f"""
    <style>
        body {{
            background-color: {primary_color};
            color: {light_color};
        }}
        .stButton > button {{
            background-color: {dark_color};
            color: {light_color};
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Dark Mode Toggle
dark_mode = st.sidebar.checkbox("Enable Dark Mode", value=True)
if not dark_mode:
    st.markdown(
        f"""
        <style>
            body {{
                background-color: {light_color};
                color: {primary_color};
            }}
            .stButton > button {{
                background-color: {accent_color};
                color: {primary_color};
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Navigation Bar
nav_options = [
    "Overview",
    "Trend Analysis",
    "Engagement Distribution",
    "Growth Analysis",
    "Content-Type Analysis",
    "Tag Cloud",
    "Community Overlap",
    "Community Detection",
    "Advanced Analytics",
    "Recommendations",
]
selected_option = st.sidebar.radio("Navigation", nav_options)

data = pd.read_csv(r"youtube_api_dataset.csv")

# Preprocess Data
data['publishedAt'] = pd.to_datetime(data['publishedAt'])
data['description'] = data['description'].fillna("No description available")
data['channel_name'] = data['channel_name'].fillna("Unknown Channel")
data['tags'] = data['tags'].fillna("No tags available")
data['year'] = data['publishedAt'].dt.year
data['month'] = data['publishedAt'].dt.month
data['week'] = data['publishedAt'].dt.isocalendar().week

# Sidebar Filters
st.sidebar.header("Filter Options")
channel_filter = st.sidebar.multiselect("Select Channels", options=data['channel_name'].unique())
year_filter = st.sidebar.multiselect("Select Year", options=data['year'].unique())

if channel_filter:
    data = data[data['channel_name'].isin(channel_filter)]
if year_filter:
    data = data[data['year'].isin(year_filter)]

# Overview Section
if selected_option == "Overview":
    st.title("YouTube Educators Dashboard")
    st.markdown(
        """This dashboard analyzes YouTube educators' networks and engagement data. It provides insights on 
        trends, growth patterns, and advanced analytics to empower content creators and researchers."""
    )

# Trend Analysis Section
if selected_option == "Trend Analysis":
    st.header("Trend Analysis by Channel")
    st.markdown("Visualize seasonal patterns in viewership.")
    heatmap_data = data.groupby([data['publishedAt'].dt.month, 'channel_name'])['views'].sum().unstack()
    fig = px.imshow(heatmap_data, text_auto=True, color_continuous_scale="Reds", labels={'color': 'Views'})
    st.plotly_chart(fig)

# Engagement Distribution Section
if selected_option == "Engagement Distribution":
    st.header("Engagement Distribution")
    st.markdown("Analyze views, likes, and comments distribution.")
    fig = px.box(data, y=["views", "likes", "comments"], points="all", labels={"value": "Engagement Metrics"})
    st.plotly_chart(fig)

# Growth Analysis Section
if selected_option == "Growth Analysis":
    st.header("Growth Analysis with Future Trend Predictions")
    st.markdown("View subscriber growth trends and forecast future growth for a selected channel.")
    channels = data['channel_name'].unique()
    selected_channel = st.selectbox("Select a channel", channels)
    channel_data = data[data['channel_name'] == selected_channel]
    growth_data = channel_data.groupby(channel_data['publishedAt'].dt.to_period("M"))['views'].sum().reset_index()
    growth_data['publishedAt'] = growth_data['publishedAt'].astype(str)
    growth_data = growth_data.rename(columns={'publishedAt': 'ds', 'views': 'y'})
    model = Prophet()
    model.fit(growth_data)
    future = model.make_future_dataframe(periods=6)
    forecast = model.predict(future)
    fig = model.plot(forecast)
    st.plotly_chart(fig)

# Content-Type Analysis Section
if selected_option == "Content-Type Analysis":
    st.header("Content-Type Analysis")
    st.markdown("Analyze the proportion of content types based on tags.")
    if 'tags' in data.columns:
        data['tags'] = data['tags'].str.split(',')
        exploded_tags = data.explode('tags')
        exploded_tags['tags'] = exploded_tags['tags'].str.strip()
        exploded_tags = exploded_tags[exploded_tags['tags'] != '']
        tag_data = exploded_tags.groupby('tags').size().reset_index(name="count")
        if tag_data.empty:
            st.warning("No valid tags found.")
        else:
            fig = px.pie(tag_data, names="tags", values="count", title="Content-Type Distribution Based on Tags")
            st.plotly_chart(fig)
    else:
        st.warning("Tags column not found in the dataset.")

# Top Channels Visualization
st.sidebar.subheader("Additional Insights")
if selected_option == "Overview":
    def plot_top_channels(data):
        top_channels = data.groupby('channel_name')[['views', 'likes', 'comments']].sum()
        top_channels = top_channels.sort_values(by='views', ascending=False).head(10)
        st.subheader("Top 10 Channels by Views, Likes, and Comments")
        st.bar_chart(top_channels)

    plot_top_channels(data)
