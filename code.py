# --------------
import pandas as pd 

# Read the data using pandas module.

df = pd.read_csv(path)
print(df.columns)
# Find the list of unique cities where matches were played
matches_city = df['city'].unique
print("Cities matches were played : {}".format(matches_city))
# Find the columns which contains null values if any ?

print(df.columns[df.isnull().values.any()])

# List down top 5 most played venues
df_unique_matches = df.drop_duplicates('match_code')
venues_top5 = df['venue'].value_counts().nlargest(5)
print(venues_top5)

# Make a runs count frequency table
print(df['runs'].value_counts())

# How many seasons were played and in which year they were played 

df_unique_matches['year'] = pd.DatetimeIndex(df_unique_matches['date']).year
print('{}: session were played'.format(len(df_unique_matches['year'].unique())))


# No. of matches played per season
print(df_unique_matches['year'].value_counts())

# Total runs across the seasons
df['year'] = pd.DatetimeIndex(df['date']).year
print(df.groupby('year').agg({"runs":"sum"}))


# Teams who have scored more than 200+ runs. Show the top 10 results
runs_per_team_per_match = df.groupby(['match_code','batting_team']).agg({"runs":"sum"})
print(runs_per_team_per_match[runs_per_team_per_match['runs']>200])

# What are the chances of chasing 200+ target
n_matches_g200 = len(runs_per_team_per_match[runs_per_team_per_match['runs']>200])

print(n_matches_g200)

df_unique_matches['first_200'] = df_unique_matches['match_code'].apply(lambda x:df[(df['match_code']==x) & df['inning']==1]['runs'].sum()>=200)

df_unique_matches['first_200'] = df_unique_matches['match_code'].apply(lambda x:df[(df['match_code']==x) & df['inning']==2]['runs'].sum()>=200)

print(len(df_unique_matches[df_unique_matches['first_200']==True]))


# Which team has the highest win count in their respective seasons ?
print(df_unique_matches.groupby(['year','winner']).agg({'winner':'max'}))





