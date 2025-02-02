import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import pandas as pd

# Load environment variables
load_dotenv()

# Fetch API key
api_key = os.getenv('GOOGLE_API_KEY')

if not api_key:
    st.error("API key not found.")
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro', safety_settings={
        "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE",  # Allow all content
    })

    # Streamlit app configuration
    st.set_page_config(page_title='Text to SQL App', page_icon=None)

    # Header
    col1, col2 = st.columns((0.2, 0.8))
    col1.image('logo.png')
    col2.markdown(
    """
    <div style="
        text-align: center; 
        font-size: 40px; 
        font-weight: bold; 
        color: #FFD700; 
        padding: 20px; 
        border-radius: 10px; 
        background: linear-gradient(90deg, #FF5733, #FFD700, #33FF57);
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent;
    ">
        SQL QUERY AI ASSISTANT 🚀
    </div>
    """,
    unsafe_allow_html=True
)

    st.write("#### :rainbow[This is SQL Query Generator Web App Using Google Gemini]")

    # User input
    query_input = st.text_area('Please Enter Your Prompt Using Simple English')
    submit = st.button('Generate SQL')

    # Prompts
    prompt_1 = "Based upon the prompt generate a SQL query and make sure to exclude ''' in the beginning and the end."
    prompt_2 = "Based upon the prompt, create a simple input table with 3 columns and 4 rows before applying the query. Then, create a sample output table after applying the query. Ensure the tables are small and easy to understand."
    prompt_3 = "Explain the SQL query in detail without any example output."

    if submit:
        with st.spinner('Generating....'):
            # Generate SQL query
            response = model.generate_content([prompt_1, query_input])
            st.write("#### The Generated SQL Query Code:")
            st.code(response.text, language='sql')
            
            response2 = model.generate_content([prompt_2, query_input])

            # Extract tables from response
            table_text = response2.text.split("\n\n")  # Assuming tables are separated by double newlines
            if len(table_text) >= 2:
                input_table_text = table_text[0]  # First part is the input table
                output_table_text = table_text[1]  # Second part is the output table

                # Convert text tables into DataFrames
                try:
                    output_table = [row.split("|")[1:-1] for row in output_table_text.split("\n") if "|" in row]

                    if len(output_table) > 1:
                        output_df = pd.DataFrame(output_table[1:], columns=[col.strip() for col in output_table[0]])
                        st.write("#### Sample Output Table:")
                        st.dataframe(output_df)
                    else:
                        st.warning("Output table could not be generated properly.")

                except Exception as e:
                    st.error(f"Error while parsing tables: {e}")
                    st.text("Raw Input Table Text:\n" + input_table_text)
                    st.text("Raw Output Table Text:\n" + output_table_text)

            else:
                st.warning("Could not parse the tables. Please try again.")


            # Generate explanation
            response3 = model.generate_content([prompt_3, query_input])
            st.write("#### Explanation of the Generated SQL Query Code:")
            explanation = response3.text

            # Format explanation as a Markdown list
            lines = explanation.split('\n')
            md_list = []
            for line in lines:
                if line.startswith('*'):
                    md_list.append(f" {line[1:]}")
                else:
                    md_list.append(line)
            md_explanation = '\n'.join(md_list)
            st.markdown(md_explanation)
            
            st.markdown(
    """
    <div style="text-align:center; font-size:24px; font-weight:bold; color:#4CAF50; padding: 13px; border-radius: 10px; background-color: #f0f0f0;">
        🎉 End of Results 🎉
    </div>
    """,
    unsafe_allow_html=True
)
