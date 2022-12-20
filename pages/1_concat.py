import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import streamlit as st
import pandas as pd
from csv_util import concat


st.title('CSV CONCATTER')
st.subheader('1. UPLOAD YOUR FILE')
DATAFRAMES = []
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    st.write("filename:", uploaded_file.name)
    if uploaded_file is not None:
        try:
            # Can be used wherever a "file-like" object is accepted:
            dataframe = pd.read_csv(uploaded_file, index_col=0, encoding="utf-8")
            DATAFRAMES.append(dataframe)
        except:
            st.error('Invalid style object had ditected', icon="🚨")


st.subheader('2. DOWNLOAD CONCATED FILE')
st.write("you can see donwload button if you uploaded 2 or more files")

if 2 <= len(DATAFRAMES):
    csv = concat.convert_df(DATAFRAMES)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='concated.csv',
        mime='text/csv',
    )