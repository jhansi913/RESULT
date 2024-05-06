import streamlit as st
import pandas as p

df = pd.read_excel('22-Res11.xlsx')

# Function to read student result data from Excel file
def load_student_results(file_path):
    try:
        df = pd.read_excel(file_path, engine='openpyxl')  # Read Excel file into DataFrame
        return df
    except Exception as e:
        st.error(f"Error occurred: {e}")
        return None
        

# Function to retrieve student result by roll number
def get_student_result(df, roll_number):
    student_data = df[df['Roll Number'] == roll_number]  # Filter DataFrame by roll number
    if len(student_data) > 0:
        return student_data.iloc[0].to_dict()  # Convert row to dictionary
    else:
        return None

# Streamlit app title and description
st.title('Student Result Lookup')
st.write('Upload your student result Excel file (.xlsx format):')

# File uploader to upload Excel file
 
# Main app logic
if df is not None:
     roll_number = st.text_input('Enter Roll Number')     
    if st.button('Show Result'):
         student_result = get_student_result(df, roll_number)
        if student_result:
            st.write(f"Name: {student_result['Name']}")
            st.write(f"Math Score: {student_result['Math']}")
            st.write(f"Science Score: {student_result['Science']}")
            st.write(f"History Score: {student_result['History']}")
         else:
             st.write('Student not found. Please enter a valid roll number.')
               
            
                
  
    
     
