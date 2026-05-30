import pandas as pd
import plotly.express as px

df = pd.read_csv('../data/testing.csv')

countries_to_compare = ['Denmark', 'Finland', 'Norway', 'Sweden']
df_filtered = df[df['country'].isin(countries_to_compare)]


custom_colors = {
    'Sweden': 'red',
    'Denmark': '#1f77b4',     
    'Finland': '#aec7e8',     
    'Norway': '#000080',      
}

fig3 = px.line(
    df_filtered, 
    x='date', 
    y='new_tests',
    color='country',
    color_discrete_map=custom_colors, # color map
    title='Comparison of COVID-19 Testing ', 
    labels={
        'new_tests': 'Number of new tests', 
        'date': 'Date',                                   
        'country': 'Country'                              
    },
    template='plotly_white'
)


fig3.update_xaxes(
    rangeslider_visible=True,

)
fig3.update_layout(
    title_font=dict(size=24), 
    
    font=dict(size=14),

    legend=dict(
        title_font=dict(size=18), 
        font=dict(size=16),       
        itemsizing='constant'     
    )
)

fig3.write_html("../plots/testing_everyday_4countries.html")