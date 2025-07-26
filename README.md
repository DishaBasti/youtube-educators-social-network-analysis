# YouTube Educators Social Network Analytics (SNA) Dashboard

This project is an end-to-end **Social Network Analytics (SNA)** and visualization tool built using Python and Streamlit. It analyzes **YouTube educators** and their ecosystem based on video data, viewer engagement, and network structures.


## What is Social Network Analytics?

**Social Network Analytics (SNA)** is a field of data analysis that examines the structure and dynamics of relationships among entities (like people, organizations, or content creators). In this project, we analyze:

- **Collaboration patterns** among YouTube educators
- **Viewer engagement and overlaps**
- **Community formation and influence**
- **Content trends and growth predictions**


## Project Objectives

1. Identify influential YouTube educator channels based on network metrics and user engagement.
2. Analyze collaboration and content overlap between channels.
3. Predict future trends in views and engagement using time-series forecasting.
4. Present all findings through an interactive **Streamlit dashboard**.

## 🧰 Tools & Technologies

| Category             | Libraries / Tools                                |
|----------------------|--------------------------------------------------|
| Data Collection      | YouTube Data API v3                              |
| Data Handling        | `pandas`, `numpy`                                |
| Visualization        | `plotly`, `matplotlib`, `seaborn`, `pyvis`       |
| Social Network Graph | `networkx`, `community` (Louvain), `bipartite`   |
| Time Series Forecast | `prophet`                                        |
| Dashboard            | `streamlit`                                      |


## 📁 Project Structure
```
youtube-educators-sna/
├── youtube_analytics.py # Main Streamlit dashboard
├── requirements.txt
├── README.md
├── youtube_api_dataset.csv 
```

## Features

- Trend analysis by month/year
- Engagement distribution (views, likes, comments)
- Growth prediction using Prophet
- Content-type and tag distribution
- Community detection and network graph
- Sidebar filters for channels and years
- Built entirely in Python with Streamlit


## Sample Visuals (Screenshots)

Coming soon


## How to Run the App Locally

1. **Clone the repository**
```bash
git clone https://github.com/DishaBasti/youtube-educators-sna.git
cd youtube-educators-sna
```
2. **Create a virtual environment (optional)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
streamlit run youtube_analytics.py
```

## YouTube Data
A youtube_api__dataset.csv is provided to demonstrate functionality.

## Using Your Own Dataset
- You can collect your own dataset from YouTube using the Data API v3:

- Get an API key from: https://console.developers.google.com

- Open and run the notebooks/data_collection.ipynb

- Save the dataset

- Update the file path in youtube_analytics.py

## Future Enhancements
 - Automate real-time data collection

 - Use transformer models for sentiment (e.g., BERT)

 - Add network animation over time

## License
MIT License – free to use and modify for academic or personal use. Please attribute the original author if reused.

## Author
**Disha S Basti**
