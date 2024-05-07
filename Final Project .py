import pandas as pd

# 1. Reading the data from the CSV file: This operation depends on the size of the file 
# but can generally be considered to have a complexity of O(n), 
# where n is the number of rows in the file.

# Read the data from the CSV file
df = pd.read_csv('FinalMerged2.csv') # O(n)

# ----------------------------------------------------

# 2. Sorting the dataframe: The complexity of sorting a dataframe using the `sort_values` function
# is typically O(n log n), where n is the number of rows in the dataframe. 
# Since the sorting is performed twice in this code, 
# the overall complexity is O(n log n).

# Select the cities with the lowest Fprice and FHtotal
df = df.sort_values(by=['FHtotal', 'Fprice', 'days'], ascending=True) # O(n log n).

# ----------------------------------------------------

# 3. This operation involves performing element-wise division on two columns of the dataframe,
# which can be considered to have a complexity of O(n).

# Calculate the value-to-weight ratio for each city
df['FHtotal_to_Fprice'] = df['FHtotal'] / df['Fprice'] # O(n)

# Sort the cities by value-to-weight ratio in descending order
df = df.sort_values(by='FHtotal_to_Fprice', ascending=False)

# ----------------------------------------------------

# 4. Getting user input: This step involves reading user input,
# which is generally considered to have a complexity of O(1)
# since it doesn't depend on the input size.

# Get user input O(1)
name = input("Enter your name: ")
budget = float(input("Enter your budget: "))
num_cities = int(input("Enter the number of cities you want to visit: "))

# ----------------------------------------------------

# 5. The complexity of this algorithm depends on the number of cities (`num_cities`) 
# and the number of rows in the dataframe (`n`).
# In the worst case, where `num_cities` is equal to `n`, 
# the complexity would be O(n^2). 
# since it breaks out of the loop as soon as it reaches the desired number of cities,
# the average case complexity would be less than O(n^2).

# Check if the result for the current combination of budget 
# and number of cities is already in the memoization dictionary

memo = {}

if (budget, num_cities) in memo:
    selected_cities = memo[(budget, num_cities)]
    
else:    
    # Use the dynamic programming knapsack table algorithm to select the cities that fit within the budget 
    selected_cities = []
    total_cost = 0
    for index, row in df.iterrows():
        if total_cost + row['FHtotal'] <= budget and row['place'] not in selected_cities:
            selected_cities.append(row['place'])
            total_cost += row['FHtotal']
        if len(selected_cities) == num_cities:
            break
    
    # Store the result in the memoization dictionary
    memo[(budget, num_cities)] = selected_cities

# ----------------------------------------------------

# 6. Printing the recommendations: Printing the recommendations involves
# iterating over the selected cities and retrieving corresponding information from the dataframe.
# This step has a complexity of O(num_cities).

# Print the recommendations with flight type, agency, days, and hotel names
print(f"Dear {name}, we recommend the following cities within your budget of {budget}:")

for num_cities in selected_cities:
    flightType = df[df['place'] == num_cities]['flightType'].iloc[0]
    agency = df[df['place'] == num_cities]['agency'].iloc[0]
    days = df[df['place'] == num_cities]['days'].iloc[0]
    hotel = df[df['place'] == num_cities]['name'].iloc[0]
    FHtotal = df[df['place'] == num_cities]['FHtotal'].iloc[0]
    print(f"{num_cities} (flight type: {flightType}, agency: {agency}, days: {days}, hotel: {hotel}, total price: ${FHtotal} )")

# Therefore, the overall complexity of the code is dominated by the sorting operations 
# and can be approximated as O(n log n), 
# where n is the number of rows in the dataframe.