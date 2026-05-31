import pandas as pd
import plotly.express as px

df = pd.read_csv('../data/testing.csv')

countries_to_compare = ['Sweden', 'New Zealand']
df_filtered = df[df['country'].isin(countries_to_compare)]


custom_colors = {
    'Sweden': 'red',   
    'New Zealand': 'green',      
}

fig3 = px.line(
    df_filtered, 
    x='date', 
    y='new_tests_7day_smoothed',
    color='country',
    color_discrete_map=custom_colors, # color map
    title='Comparison of COVID-19 Testing (7-Day Smoothed)',
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

fig3.write_html("../plots/testing_every_7days_2countries.html")