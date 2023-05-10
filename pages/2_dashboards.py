import pandas as pd
import plotly.express as ex
import streamlit as st

dataset = pd.read_csv("hotel_bookings.csv")

fig = ex.histogram(dataset,x='arrival_date_month', color= 'arrival_date_year')

st.title('Visualising the dataset')
st.divider()
st.header('1. No. of bookings per month')
st.caption('You can filter by the year by clicking on it')
st.plotly_chart(fig,theme=None, use_container_width=True)

month=dataset.groupby(["arrival_date_month"])[["arrival_date_month"]].count()
month = month["arrival_date_month"].sort_values()

fig2 = ex.bar(month)
st.subheader('Total no. of bookings for all the years grouped by each month')
st.plotly_chart(fig2,theme=None, use_container_width=True)

dataset_country =  dataset['country']
dataset_country = dataset_country.value_counts().to_frame()

country=dataset.groupby(["country"])[["country"]].count()
country = country["country"].sort_values(ascending=False)
country = country[:10]

st.subheader('2. Top 10 countries by distribution of guests')
st.caption('The country names are in Alpha 3 format, you can sort the values by clicking on the column')
st.dataframe(country)

dataset_repeated = dataset['is_repeated_guest'].value_counts().to_frame()

fig = ex.pie(dataset_repeated, values='is_repeated_guest',color= dataset_repeated.index,title='Percentage of repeated guests')

st.subheader('3. Total percentage of repeated guests')

st.plotly_chart(fig, theme=None)


segments=dataset["market_segment"].value_counts()

# pie plot
fig = ex.pie(segments,
             values=segments.values,
             names=segments.index)
fig.update_traces(rotation=-90, textinfo="percent+label")

st.subheader('4. Total no. of bookings per market segment')
st.plotly_chart(fig,theme=None)
