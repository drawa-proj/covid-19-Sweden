import pandas as pd
import plotly.express as px
import pandas as pd


df = pd.read_csv('../data/vaccinations_age.csv')
df_sewden=df[df['country']=='Sweden']

df_sewden['date'] = pd.to_datetime(df_sewden['date'])

unique_groups = ['15-17', '18-24', '25-49', '50-59', '60-69', '70-79', '80+']
df_clean = df_sewden[df_sewden['age_group'].isin(unique_groups)].copy()
# convert date to string
df_clean['year_month'] = df_clean['date'].dt.strftime('%Y-%m')
df_clean = df_clean.groupby(['year_month', 'age_group'])['people_vaccinated_per_hundred'].max().reset_index()

all_months = df_clean['year_month'].unique()
idx = pd.MultiIndex.from_product([all_months, unique_groups], names=['year_month', 'age_group'])

df_clean = df_clean.set_index(['year_month', 'age_group']).reindex(idx, fill_value=0).reset_index()


# sort
df_clean = df_clean.sort_values(by='year_month')

# animated plot
fig_race = px.bar(
    df_clean, 
    x="people_vaccinated_per_hundred", 
    y="age_group", 
    color="age_group", 
    animation_frame="year_month", 
    animation_group="age_group", 
    orientation='h', 
    range_x=[0, 100], 
    category_orders={"age_group": unique_groups},
    title="COVID-19 Vaccination in Sweden (Vaccinated)",
    labels={
        "people_vaccinated_per_hundred": "Vaccinated (%)",
        "age_group": "Age Group",
        "year_month": "Date"
    }
)


fig_race.update_layout(
    yaxis={'categoryorder':'category descending'},
    template="plotly_white",
        title_font=dict(size=24), 
    
    font=dict(size=14),

    legend=dict(
        title_font=dict(size=18), 
        font=dict(size=16),       
        itemsizing='constant'     
    )
)



fig_race.write_html("../plots/vaccinated.html")