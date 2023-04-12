# import os, shutil
# from streamlit import components

# def _get_static_path():
#     return os.path.join(os.path.dirname(__file__), "static")

# def pdf_component(pdf_path, width, height, key=None):
#     static_path = _get_static_path()
#     shutil.copyfile(pdf_path, os.path.join(static_path, "local_pdf.pdf"))
#     local_pdf_url = f"/{key}/static/local_pdf.pdf"

#     # return components.html(
#     #     f"""
#     #     <embed src="{local_pdf_url}" width="{width}" height="{height}" type="application/pdf" />
#     #     """,
#     #     height=height,
#     #     scrolling=True,
#     # )
#     return components.html(
#         f"""
#         <embed src="{local_pdf_url}" width="{width}" height="{height}" type="application/pdf" />
#         """,
#         height=int(height.strip("px")),
#         scrolling=True,
#     )
