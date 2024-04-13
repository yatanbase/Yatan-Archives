import pandas as pd
import random

# Follower Growth
follower_growth_data = {
    'Date': pd.date_range(start='2021-01-01', end='2021-01-10'),
    'Followers Count': [random.randint(100, 1000) for _ in range(10)]
}
follower_growth_df = pd.DataFrame(follower_growth_data)

# Sentiment Analysis
sentiment_analysis_data = {
    'Post ID': ['P1', 'P2', 'P3', 'P4', 'P5'],
    'Sentiment Score': [random.random() for _ in range(5)],
    'Sentiment Label': random.choices(['positive', 'negative', 'neutral'], k=5)
}
sentiment_analysis_df = pd.DataFrame(sentiment_analysis_data)

# Audience Preferences
audience_preferences_data = {
    'Post ID': ['P1', 'P2', 'P3', 'P4', 'P5'],
    'Audience Age Group': random.choices(['18-24', '25-34', '35-44', '45+'], k=5),
    'Audience Gender': random.choices(['Male', 'Female'], k=5),
    'Audience Location': random.choices(['USA', 'UK', 'Canada'], k=5)
}
audience_preferences_df = pd.DataFrame(audience_preferences_data)

# Trends Analysis
trends_analysis_data = {
    'Topic': ['Technology', 'Fashion', 'Health', 'Food', 'Travel'],
    'Trending Score': [random.random() for _ in range(5)],
    'Trending Label': random.choices(['popular', 'normal', 'declining'], k=5)
}
trends_analysis_df = pd.DataFrame(trends_analysis_data)

# Engagement Rates
engagement_rates_data = {
    'Post ID': ['P1', 'P2', 'P3', 'P4', 'P5'],
    'Engagement Rate (%)': [random.randint(1, 10) for _ in range(5)]
}
engagement_rates_df = pd.DataFrame(engagement_rates_data)

# Save dataframes to Excel file
with pd.ExcelWriter('sample_data.xlsx') as writer:
    follower_growth_df.to_excel(writer, sheet_name='Follower Growth', index=False)
    sentiment_analysis_df.to_excel(writer, sheet_name='Sentiment Analysis', index=False)
    audience_preferences_df.to_excel(writer, sheet_name='Audience Preferences', index=False)
    trends_analysis_df.to_excel(writer, sheet_name='Trends Analysis', index=False)
    engagement_rates_df.to_excel(writer, sheet_name='Engagement Rates', index=False)