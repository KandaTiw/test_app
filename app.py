import streamlit as st

st.title("My first app!")

st.info("Hello again! Awesome!!!")
st.success("This is success")
st.error("This is an error message")
st.warning("This is a warning message")


st.write("""Header 2 Test IF Statement""")

placeholder = st.empty()
status = 0
if status == 1:
    placeholder.info("status = 1")
else:
    placeholder.error("status error!")

st.write("""Header 2 Test Radio Button""")
status2 = st.radio("Select an option", ["Success","Error"])

placeholder2 = st.empty()
if status2 == "Success":
    placeholder2.success("status success")
else:
    placeholder2.error("status error!")

st.write("""Test Chart""")

st.header("Area Chart")
#https://docs.streamlit.io/develop/api-reference/charts/st.area_chart
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)

st.header("Test Demo Data")

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv")

df # st.write(df)


import altair as alt

c = (
   alt.Chart(df)
   .mark_circle()
   .encode(x="bill_length_mm", y="body_mass_g", color="species")
)

st.altair_chart(c, use_container_width=True)

