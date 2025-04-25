
import streamlit as st
import pandas as pd
import plotly.express as px

# Set Page Layout
st.set_page_config(page_title="SuperMarket Analysis Deployment", page_icon="🛒")

df = pd.read_csv("cleaned_supermarket_sales.csv")
st.dataframe(df.head())


page = st.sidebar.radio('Pages', ['Univariate Analysis', "Bivariate Analysis", "Multivariate Analysis"])

if page == "Univariate Analysis":
    chart = st.selectbox("Select Chart", ["Histogram", "Pie"])

    if chart == "Histogram":
        st.plotly_chart(px.histogram(data_frame=df.groupby("Product line")["Total"].mean().sort_values(ascending=False).reset_index().round(2),
        x="Product line", y="Total", title="AVG Quantity purchased per transaction, broken down by product line")
        ,key="Histogram_Chart")

    elif chart == "Pie":
        st.plotly_chart(px.pie(data_frame=df.groupby('Payment')['Total'].sum().sort_values(ascending=False).reset_index().round(2), values="Total",
        names="Payment"), key="Pie_chart")

elif page == "Bivariate Analysis":

    chart = st.selectbox("Select Chart", ["Heatmap", "Scatterplot", "Bar"])

    if chart == "Heatmap":
        st.plotly_chart(px.imshow(df.corr(numeric_only=True).round(2), height=600, width=1200, text_auto=True))

    elif chart == "Scatterplot":
        st.plotly_chart(px.scatter(data_frame=df.groupby(["Date"])['Total'].sum().sort_values(ascending=False).reset_index().round(2),
        x="Date", y='Total', size="Total", title="Traffic over time by total sales to identify peaks"))

    elif chart == "Bar":
        st.plotly_chart(px.bar(data_frame=df.groupby('Day')['Total'].sum().sort_values(ascending=False).reset_index().round(2),
        x='Day', y='Total', title="Traffic on Days of the week that achieve highest sales"), title="Correlation Between Numeric Columns")

elif page == "Multivariate Analysis":

    chart = st.selectbox("Select Chart", ["SunBurst", "Bar"])



    if chart == "Bar":
        st.plotly_chart(px.bar(data_frame=df.groupby(["Customer type", "Gender"])['Total'].sum().reset_index().round(2),
    x='Gender', y='Total', color='Customer type', title="Customer Type Analysis by Gender", text_auto=True, barmode='group'))

    elif chart == "SunBurst":
        st.plotly_chart(px.sunburst(data_frame=df.groupby(["Branch", "City"])['Total'].sum().sort_values(ascending=False).reset_index().round(2),
    path=['Branch', 'City'],  title="Cost of Goods Sold by Branch and City", color='Total'))
