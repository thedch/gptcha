import fire
import os
import streamlit as st
import streamlit.components.v1 as components

from datetime import datetime


@st.cache_data
def run_server():
    os.system('python myserver.py &')

def try_html():
    run_server()

    st.write('Iframe Begin')
    components.iframe("http://127.0.0.1:32100", width=800, height=800, scrolling=True)
    st.write('Iframe End')


if __name__ == '__main__':
    try_html()
