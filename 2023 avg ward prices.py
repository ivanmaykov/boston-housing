#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import matplotlib.ticker as ticker

# Connect to the SQLite database
con = sqlite3.connect('2023_houses.db')

# SQL query to calculate average price per year
query = """
SELECT SUBSTRING(PID, 1, 2) AS Ward, ROUND(AVG(LAND_VALUE + BLDG_VALUE)) AS average_price
FROM "2023_table"
WHERE LAND_VALUE > 0
    AND BLDG_VALUE > 0
GROUP BY Ward;
"""

# Execute the query and read the results into a DataFrame
df_2023 = pd.read_sql_query(query, con)

# Define custom labels for the legend
labels = ['01 = East Boston', '02 = Charlestown', '03 = Back Bay/Beacon Hill; Downtown/North End/South End'
          '04 = Back Bay/Beacon Hill; Downtown/North End/South End; Jamaica Plain/Mission Hill', 
          '05 = Back Bay/Beacon Hill; Downtown/North End/South End; Fenway/Kenmore', '06 = South Boston',
          '07 = South Boston', '08 = Downtown/North End/South End; North Dorchester; Roxbury/Franklin Field',
          '09 = Downtown/North End/South End', '10 = Fenway/Kenmore; Jamaica Plain/Mission Hill', 
          '11 = Jamaica Plain/Mission Hill', '12 = Jamaica Plain/Mission Hill; Roxbury/Franklin Field',
          '13 = North Dorchester', '14 = South Dorchester; Mattapan; Roxbury/Franklin Field', 
          '15 = North Dorchester; South Dorchester', '16 = South Dorchester', '17= South Dorchester; Mattapan; Roxbury/Franklin Field',
          '18 = Hyde Park; Mattapan; Roslindale/Moss Hill/West Roxbury', 
          '19 = Jamaica Plain/Mission Hill; Roslindale/Moss Hill/West Roxbury', '20 = Roslindale/Moss Hill/West Roxbury',
          '21 = Allston/Brighton', '22 = Allston/Brighton']

# Create the bar plot
plt.figure(figsize=(10, 6))
bars = plt.bar(df_2023['Ward'], df_2023['average_price'])

# Add Legend to associate ward number with neighborhood
plt.legend(bars, labels)
legend = plt.legend(bars, labels, bbox_to_anchor=(1.05, 1.00), loc='upper left')

# Adjust layout
plt.tight_layout()

# Add currency value onto Y-axis
formatter = ticker.StrMethodFormatter('${x:,.0f}')
plt.gca().yaxis.set_major_formatter(formatter)

# Label Graph
plt.xlabel('Boston Neighborhoods')
plt.ylabel('Average Price')
plt.title('Average 2023 Boston Property Prices Based on Ward Codes')
plt.show()


# In[ ]:




