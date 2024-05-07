import pandas as pd

df = pd.read_csv('FinalMerged2.csv')
df = df.sort_values(by=['Fprice', 'FHtotal', 'days'], ascending=True)

df['FHtotal_to_Fprice'] = df['FHtotal'] / df['Fprice'] # O(n)


df = df.sort_values(by='FHtotal_to_Fprice', ascending=False)
name = input("Enter your name: ")
budget = float(input("Enter your budget: "))
num_cities = int(input("Enter the number of cities you want to visit: "))

memo = {}
if (budget, num_cities) in memo:
    selected_cities = memo[(budget, num_cities)]
    
else:    
    selected_cities = []
    total_cost = 0
    for index, row in df.iterrows():
        if total_cost + row['FHtotal'] <= budget and row['place'] not in selected_cities:
            selected_cities.append(row['place'])
            total_cost += row['FHtotal']
        if len(selected_cities) == num_cities:
            break
    memo[(budget, num_cities)] = selected_cities
print(f"Dear {name}, we recommend the following cities within your budget of {budget}:")

for num_cities in selected_cities:
    flightType = df[df['place'] == num_cities]['flightType'].iloc[0]
    agency = df[df['place'] == num_cities]['agency'].iloc[0]
    days = df[df['place'] == num_cities]['days'].iloc[0]
    hotel = df[df['place'] == num_cities]['name'].iloc[0]
    FHtotal = df[df['place'] == num_cities]['FHtotal'].iloc[0]
    print(f"{num_cities} (flight type: {flightType}, agency: {agency}, days: {days}, hotel: {hotel}, total price: ${FHtotal})")
    