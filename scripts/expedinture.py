import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/expedinture.csv' ,skiprows=8)


years = ['2019', '2020', '2021', '2022', '2023', '2024']
df = df[['TIME'] + years]

df.rename(columns={'TIME': 'Country'}, inplace=True)

countries_to_keep = [
    'European Union - 27 countries (from 2020)', 
    'Poland', 
    'Sweden'
]
df = df[df['Country'].isin(countries_to_keep)]

for year in years:
    df[year] = df[year].astype(str).str.replace(r'\s+', '', regex=True).str.replace(',', '.')
    df[year] = pd.to_numeric(df[year], errors='coerce')

df = df.drop(columns=['2024'])
df = df.reset_index(drop=True)


#only Sweden & Poland
df_filtered = df[df['Country'].isin(['Poland', 'Sweden'])]

df_melted = df_filtered.melt(
    id_vars=['Country'], 
    var_name='Year', 
    value_name='Expenditure (Million EUR)'
)

# plot
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

sns.lineplot(
    data=df_melted, 
    x='Year', 
    y='Expenditure (Million EUR)', 
    hue='Country',
    style='Country',
    markers=True,
    dashes=False,
    markersize=10,
    palette=['#E41A1C', '#377EB8']  
)

plt.title('Health Care Expenditure: Poland vs Sweden', fontsize=14, pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Expenditure (Million Euro)', fontsize=12)

plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

plt.savefig("../plots/expedinture.png")