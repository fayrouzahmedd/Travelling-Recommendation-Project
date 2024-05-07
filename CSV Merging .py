import pandas as pd

# Read dataset files

users_df = pd.read_csv("users.csv")
flights_df = pd.read_csv("flights2.csv", usecols=['travelCode', 'userCode', 'from','place','flightType','Fprice', 'time', 'distance','agency'])
hotels_df = pd.read_csv("hotels2.csv", usecols=['travelCode', 'userCode', 'name', 'place', 'days', 'price', 'total'])

# Merge the two dataframes based on the common keys

HF_df_merged = pd.merge(flights_df, hotels_df, on=['travelCode', 'userCode', 'place'])

# Add the Fprice to total if there is a match

HF_df_merged['FHtotal'] = HF_df_merged['Fprice'] + HF_df_merged['total']

# Drop duplicates

HF_df_merged.drop_duplicates(inplace=True)

# Write the updated dataframe to a new CSV file

HF_df_merged.to_csv('FinalMerged2.csv', index=False)
