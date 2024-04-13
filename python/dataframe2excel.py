import pandas as pd

# Create a DataFrame with the provided data
data = {
    'Post ID': ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010'],
    'Date': ['2021-07-01', '2021-07-02', '2021-07-03', '2021-07-04', '2021-07-05', '2021-07-06', '2021-07-07', '2021-07-08', '2021-07-09', '2021-07-10'],
    'Caption': ['"Enjoying the summer vibes!"', '"Throwback to our amazing vacation"', '"Happy Independence Day!"', '"Celebrating with family and friends"', '"New blog post is up! Check it out"',
                '"Friday mood: ready for the weekend"', '"Exploring new places and cultures"', '"Proud to be part of this team"', '"Enjoying a relaxing Sunday"', '"Summer fashion trends are here"'],
    'Likes': [42, 78, 120, 98, 64, 125, 93, 72, 51, 112],
    'Comments': [10, 15, 25, 20, 12, 32, 18, 14, 9, 28],
    'Shares': [5, 7, 12, 8, 6, 15, 9, 7, 4, 14],
    'Hashtags': ['#summer #vibes', '#throwback #vacation', '#independenceday', '#celebration #friends', '#blog #newpost', '#friday #weekend', '#travel #explore', '#team #proud', '#sunday #relax', '#fashion #summer']
}

df = pd.DataFrame(data)

# Create an Excel file with the DataFrame
df.to_excel('data.xlsx', index=False)