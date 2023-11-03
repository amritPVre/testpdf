import streamlit as st
from xhtml2pdf import pisa
from io import BytesIO

# Define a function to create an HTML report
def create_html(data):
    html_content = f"""
    <html>
    <head>
    <style>
    /* Add your CSS styling here */
    .report-container {{
        font-family: 'Arial', sans-serif;
    }}
    .header {{
        text-align: center;
        /* ... */
    }}
    /* ... */
    </style>
    </head>
    <body>
    <div class="report-container">
        <div class="header">
            <h1>Report</h1>
        </div>
        <div class="content">
            <!-- Use the data to fill in details -->
            <p>Name: {data['name']}</p>
            <p>Age: {data['age']}</p>
            <!-- Add more details as needed -->
        </div>
    </div>
    </body>
    </html>
    """
    return html_content

# Define a function to convert HTML to PDF
def convert_html_to_pdf(html_content):
    pdf = BytesIO()
    pisa_status = pisa.CreatePDF(html_content, dest=pdf)
    if pisa_status.err:
        st.error('An error occurred while creating the PDF.')
        return None
    return pdf.getvalue()

# Create a form for the user to input data
with st.form(key='my_form'):
    name = st.text_input(label='Enter your name')
    age = st.number_input(label='Enter your age', step=1)
    submit_button = st.form_submit_button(label='Generate Report')

# When the user submits the form, create and download the PDF
if submit_button:
    data = {'name': name, 'age': age}
    html = create_html(data)
    pdf = convert_html_to_pdf(html)

    if pdf:
        st.download_button(label='Download PDF',
                           data=pdf,
                           file_name='report.pdf',
                           mime='application/pdf')
