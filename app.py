import base64
import streamlit as st
import streamlit.components.v1 as components

from datetime import datetime

if 'counter' not in st.session_state:
    st.session_state.counter = 0



def main():
    st.title('PDF Reader')
    with open('./attn-small.pdf', "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    pdf_embed = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="400" height="1000" type="application/pdf"></iframe>'

    st.markdown(pdf_embed, unsafe_allow_html=True)
    st.write('Finished', base64_pdf[:100])


@st.cache_data
def run_server():
    st.write('Running server...')
    print('Starting...')
    import os
    os.system('python frontend/myserver.py &')
    st.write('Server started')
    print('Returning...')


def try_html():
    st.write('Hmmm')
    run_server()

    st.write('Iframe Begin')
    components.iframe("http://localhost:8000/frontend", width= 800, height=800, scrolling=True)
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
    # main()
    try_html()
    # try_custom_component()
    # try_gpt4_custom_component()
