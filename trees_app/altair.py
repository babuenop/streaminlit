import streamlit as st
import pandas as pd
import altair as alt

st.title('SF Trees')
st.write('This app analyses trees in San Francisco using'
         ' a dataset kindly provided by SF DPW')
trees_df = pd.read_csv('trees.csv')

df_caretaker = trees_df.groupby(['caretaker']).count()['tree_id'].reset_index()
df_caretaker.columns = ['caretaker', 'tree_count']
fig = alt.Chart(df_caretaker).mark_bar().encode(x ='caretaker', y = 'tree_count')
st.altair_chart(fig)

st.title('SF Trees')
st.write('This app analyses trees in San Francisco using'
         ' a dataset kindly provided by SF DPW')

trees_df = pd.read_csv('trees.csv')
fig = alt.Chart(trees_df).mark_bar().encode(x = 'caretaker', y = 'count(*):Q')
st.altair_chart(fig)