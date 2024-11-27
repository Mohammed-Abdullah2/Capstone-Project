# Capstone Project🎓🥳
## [Examples of previous bootcamp demos](https://drive.google.com/drive/folders/1MEL3hZiofg_4rksTD8txyPIlGYkz8NYU?usp=drive_link)



# YouTube Channels Analysis Project

This repository contains a data analysis project focused on YouTube channels. It includes data scraping, cleaning, and insightful analysis to uncover trends and provide actionable recommendations for YouTube creators. The project uses `youtube_data.ipynb` for data collection and `insighets.ipynb` for analysis and visualization.

## Project Overview

This project aims to analyze YouTube channel performance, focusing on:

- **Data Collection**: Scraping data from YouTube using custom scripts.
- **Data Cleaning**: Preparing the scraped data for analysis.
- **Exploratory Data Analysis (EDA)**: Identifying patterns and insights in the data.
- **Visualization**: Communicating findings using charts and graphs.
- **Recommendations**: Providing strategies for improving channel performance.

## Repository Structure

The repository is organized as follows:

- `youtube_data.ipynb`: Notebook for scraping YouTube channel data.
- `youtube_data_full_clean.csv`: Cleaned dataset containing key metrics for analysis.
- `insighets.ipynb`: Main notebook for analysis and visualization.
- `README.md`: This file, with project details and usage instructions.

## Scraping Process

The scraping process is implemented in the `youtube_data.ipynb` notebook. It involves the following steps:

1. **Target Data**:
   - Channel Name
   - Category (e.g., Gaming, Education, Entertainment)
   - Subscriber Count
   - Total Views
   - Video Count
   - Engagement Metrics (e.g., likes, comments, shares)
   - Upload Frequency

2. **Scraping Method**:
   - The script uses web scraping techniques with Python libraries such as:
     - `requests` for fetching web pages.
     - `BeautifulSoup` for parsing HTML content.
   - YouTube data is extracted from publicly available channel pages.

3. **Data Storage**:
   - Scraped data is stored as a DataFrame using `pandas` and saved to `youtube_data_full_clean.csv` for further analysis.

4. **Error Handling**:
   - The notebook includes error handling for missing values and inaccessible pages to ensure robust data collection.

## Dataset Description

The cleaned dataset (`youtube_data_full_clean.csv`) includes the following columns:

- **Channel Name**: The name of the channel.
- **Category**: The content category.
- **Subscribers**: The number of subscribers.
- **Total Views**: The cumulative views across all videos.
- **Average Views**: The average views per video.
- **Videos**: The total number of uploaded videos.
- **Engagement Metrics**: Metrics such as likes, comments, and shares.
- **Country**: The channel's region (if applicable).
- **Upload Frequency**: The regularity of content uploads.

## Analysis and Insights

The `insighets.ipynb` notebook provides the following:

- Exploratory Data Analysis (EDA) with descriptive statistics.
- Insights into content categories that perform well.
- Visualizations highlighting subscriber growth and engagement trends.
- Recommendations for optimizing upload frequency and content strategy.