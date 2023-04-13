import os
from time import sleep
import streamlit as st
import streamlit.components.v1 as components
import requests


@st.cache_data
def run_server():
    os.system('python myserver.py &')
    sleep(1)

def try_html():
    run_server()

    st.write('Iframe Begin')

    r = requests.get('http://127.0.0.1:32100')
    r.raise_for_status()
    st.write(r.text)
    components.iframe("http://127.0.0.1:32100", width=800, height=800, scrolling=True)
    st.write('Iframe End')


if __name__ == '__main__':
    try_html()
