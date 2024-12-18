import streamlit as st
import plotly.express as px
import pandas as pd
import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
cursor.execute("SELECT date FROM temperature_data")
date = cursor.fetchall()
date = [item[0] for item in date]
#df = pd.read_csv("data.txt")


cursor.execute("SELECT temperature FROM temperature_data")
temperature = cursor.fetchall()
temperature = [item[0] for item in temperature]

# figure = px.line(x=df["date"], y=df["temperature"],
#                  labels={"x":"Date", "y": "Temperature (C)"})

figure = px.line(x=date, y=temperature,
                 labels={"x":"Date", "y": "Temperature (C)"})
st.plotly_chart(figure)