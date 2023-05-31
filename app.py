# Required packages importing
import streamlit as st
from streamlit_player import st_player
import base64
import time

# Header template
html_temp = """
    <body style="background-color:red;">
    <div style="background-color:tomato;padding:10px">
    <h3 style="color:white;text-align:center;"> Infra Provisoning tool</h3>
    </div>
    </body>
"""
# Hide Styles
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
# Page Config details
st.set_page_config(
        page_title = 'InfraProvisoningtool',
        page_icon = "🅰",
        layout = "wide",
        initial_sidebar_state = "expanded"
    )

def main():
    """
    This function contains the streamlit code details
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.write('\n')
    st.write("Infra Provisoning tool for the Azure Cloud Resources.")
    st.write('\n')

# main function call
if __name__ == '__main__':
    main()