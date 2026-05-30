import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/infant_mortality.csv',skiprows=11)

# remove empty columns
df = df.dropna(axis=1, how='all')

df.rename(columns={'TIME': 'Country'}, inplace=True)


countries = [
    'European Union - 27 countries (from 2020)', 
    'Poland', 
    'Sweden'
]
df = df[df['Country'].isin(countries)]


df = df.replace(':', pd.NA)


years = df.columns.drop('Country')
df[years] = df[years].apply(pd.to_numeric)
df = df.drop(columns=['2024'])
# reset index
df = df.reset_index(drop=True)



df_melted = df.melt(id_vars=['Country'], var_name='Year', value_name='Number of deaths')
df_melted['Number of deaths'] = df_melted['Number of deaths'].astype(float)



plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

sns.lineplot(
    data=df_melted, 
    x='Year', 
    y='Number of deaths', 
    hue='Country',
    style='Country',
    markers=True,
    dashes=False,
    markersize=10,
        palette=["#0FB32A",'#E41A1C', '#377EB8']  
)

plt.title('Infant Mortality (COVID-19) by Country/Region', fontsize=14, pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of cases', fontsize=12)

plt.legend(title='Country / Region', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

plt.savefig("../plots/infant_mortality.png")