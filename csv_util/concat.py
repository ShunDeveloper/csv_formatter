import streamlit as st
import pandas as pd

def convert_df(dataframes,Transpose=False):    
    # check dataframes
    for i in range(len(dataframes)):
        if isinstance(dataframes[i], pd.DataFrame) == False:
            raise ValueError('invalid object: input must be dataframes')
    
    # concat dataframe
    columns = list(dataframes[0].columns)
    for i in range(len(dataframes)-1):
        if columns == list(dataframes[i+1].columns):
            concated_df = pd.concat([dataframes[i],dataframes[i+1]])
        else:
            st.error('ERROR: Columns must be same', icon="🚨")
    
    # reset index
    concated_df.reset_index(drop=True, inplace=True)
    
    # option: Transpose
    if Transpose:
        concated_df = concated_df.T
    
    return concated_df.to_csv().encode('utf-8')