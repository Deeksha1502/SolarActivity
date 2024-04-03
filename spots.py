
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import tensorflow as tf
import warnings
from plotly import graph_objects as go
warnings.filterwarnings("ignore")
import streamlit as st
from PIL import Image
from keras.models import load_model
st.set_page_config(page_title="Solar Activity", page_icon=":tada", layout = "wide")

with st.container():
    st.subheader("The below graphs are displaying the variation in the solar activity by using the SUNSPOTS data")

st.title("Visualising the data")
data=pd.read_csv("Sunspots.csv")
data.head()
st.write(data)
sunspots = data.iloc[:,-1]


fig1=plt.figure(figsize=(28,6))
plt.plot(sunspots)
plt.ylabel(data.columns[-1], fontsize = 12, color = 'm')
plt.xlabel("Months from Jan 1749 to Jan 2021", fontsize = 12, color = 'm')
plt.title("Visualize the Data", fontsize = 18, color = 'r', weight = 'bold')
plt.show()
# plt.savefig('sunspotGraph1.png')
st.pyplot(fig1)


'''Approx 11 years cycle ---> approx 132 months cycle'''
fig2=plt.figure(figsize=(28,6))
plt.plot(sunspots)            # The whole data
plt.plot(sunspots[:72])       # Data from 1749, actual cycles started from 1755 --> 6 years means 72 months
plt.plot(sunspots[72:72+132]) # Showing the first cycle
plt.plot(sunspots[-13:])      # Displaying the current cycle
plt.ylabel(data.columns[-1], fontsize = 12, color = 'm')
plt.xlabel("Months from Jan 1749 to Jan 2021", fontsize = 12, color = 'm')
plt.title("Understanding the Sunspots data", fontsize = 18, color = 'r', weight = 'bold')
plt.legend(["Full data", "Before 1755 - The first cycle", "The first cycle", "After 2019 - The currect cycle"], fontsize = 12)
plt.show()
# plt.savefig('sunspotGraph2.png')
st.pyplot(fig2)



# Some changes for a better visualization of solar cycles
'''Collect all the years from 1755 to 2019 and use it as xticklabels'''
years = []
start = 1755
for i in range(0, len(data.iloc[:,-1][72:]),132):
    years.append(start)
    start+=11

fig3=plt.figure(figsize = (28, 6))
plt.plot(sunspots[72:])
plt.title("Visualize Solar Cycle 1 till Solar Cycle 24", weight = 'bold', color = 'r', fontsize = 18)
plt.xlim(72, 3265-12)
plt.xticks(range(72, len(sunspots),132))
plt.gca().set_xticklabels(years)
plt.show()
# plt.savefig('sunspotGraph3.png')
st.pyplot(fig3)


# Visualise the variation in the data distribution along with the outliers in the time series data
fig3=plt.figure(figsize = (15,6))
plt.subplot(2, 1, 1)
sns.distplot(sunspots)
plt.title("Variation in the data distribution", fontsize = 15, color = 'r', weight = 'bold')
plt.subplot(2, 1, 2)
sns.boxplot(sunspots)
plt.title("Boxplot of data", fontsize = 15, color = 'r', weight = 'bold')
plt.tight_layout()
plt.show()
# plt.savefig('sunspotGraph4.png')
st.pyplot(fig3)

image = Image.open('sunspotGraph3.png')
# st.image(image,caption = 'Sunsport Graph')
with open("sunspotGraph3.png", "rb") as file:
    btn=st.download_button(label="Download graph", data=file, file_name='/sunspotGraph3.png',mime="image/png")

def plot_raw_data():
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=data['Date'], y=data['Monthly Mean Total Sunspot Number'], name ='LSTM'))
    fig2.layout.update(title_text="Sunspots data")
    st.plotly_chart(fig2)

plot_raw_data()

