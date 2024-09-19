import streamlit as st
import plotly.express as px
import numpy as np

from eda import eda_app
from ml import ml_app
from about import about_app

def main():
    st.title('Hello first project')
    st.write('This is a simple Streamlit app.')



if __name__ == "__main__":
    main()