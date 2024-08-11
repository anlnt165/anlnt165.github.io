import pandas as pd
import matplotlib as plt

# Read files
df = pd.read_csv('DigiDB_digimonlist.csv')
# print(df)

# Accessing columns headers
headers = list(df.columns.values)
# print(headers)

# Create a new dataframe
dataFrame = df[['Lv50 SP', 'Lv50 Atk']]
# Index is set to be Digimon
new_index = df[['Digimon']].iloc[:,0].tolist()

# Make the new dataframe an index
dataFrame_indexed = dataFrame.set_index([new_index])
print(dataFrame_indexed)

# Getting only certain digimon
select_digimon = dataFrame_indexed.loc[['Poyomon', 'Botamon', 'Punimon', 'Pabumon', 'Kuramon']]
print(select_digimon)

# Plotting horizontal bar using df.plot.barh where h is horizontal
# This is for compound bar chart where the 2 columns in dataframe is compounded and the index
# is the x axis
ax = select_digimon.plot(kind='barh', color={'orange','blue'}).get_figure()
# Save figure - needs to get figure first then save figure
ax.savefig('horizontal bar.png')

