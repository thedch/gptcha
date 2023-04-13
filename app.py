import streamlit as st
import streamlit.components.v1 as components

from datetime import datetime


@st.cache_data
def run_server():
    import os
    os.system('python myserver.py &')


def try_html():
    st.write('Hmmm')
    run_server()

    st.write('Iframe Begin')
    components.iframe("http://localhost:8000", width=800, height=800, scrolling=True)
    st.write('Iframe End')


def try_custom_component():
    from frontend import component_zero

    def run_component(props):
        value = component_zero(key='zero', **props)
        return value

    def handle_event(value):
        st.header('Streamlit')
        st.write('Received from component: ', value)

    st.title('Component Zero Demo')
    st.session_state.counter = st.session_state.counter + 1
    props = {
        'initial_state': {'message': '' },
        'counter': st.session_state.counter,
        'datetime': str(datetime.now().strftime("%H:%M:%S, %d %b %Y"))
    }

    handle_event(run_component(props))

if __name__ == '__main__':
    try_html()
