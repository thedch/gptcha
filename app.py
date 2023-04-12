import base64
import streamlit as st

def main():
    st.title('PDF Reader')
    with open('./attn-small.pdf', "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    pdf_embed = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="400" height="1000" type="application/pdf"></iframe>'

    st.markdown(pdf_embed, unsafe_allow_html=True)
    st.write('Finished', base64_pdf[:100])


if __name__ == '__main__':
    main()
