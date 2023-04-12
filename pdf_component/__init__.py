import streamlit as st
from streamlit.components.v1 import declare_component

_component_func = declare_component(
    "pdf_component",
    path='./pdf_component',
)

def pdf_component(pdf_path: str, width: str = "800px", height: str = "2100px", key=None):
    return _component_func(pdf_path=pdf_path, width=width, height=height, key=key)
