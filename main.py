import random

import streamlit as st
import numpy as np
import pandas as pd


# Streamlit Layout
left_column, right_column = st.columns(2)


# Random seed to ensure reproducibility of python code
np.random.seed(2000)

st.title("Superstore Regional Sales")

with right_column:
    def create_dataframe():
        global dataframe
        dataframe = pd.DataFrame(
            np.random.rand(10, 20),
            columns=('Col %d' % i for i in range(20))
        )

    # Create dataframe
    create_dataframe()
    st.dataframe(dataframe.style.highlight_max(axis=0))
    x = st.slider('X')


with left_column:
    st.write(x, 'squared is', x * x)
    st.text_input("What is your name", key="name")
    st.write(st.session_state.name)


