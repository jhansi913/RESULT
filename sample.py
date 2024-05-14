import streamlit as st
import pandas as pd

def load_data(file_path):
    """
    Load student results data from Excel file and drop rows with null values.
    """
    # Load Excel file into a pandas DataFrame
    df = pd.read_excel(file_path)
    
    # Drop rows with any null values
    df.dropna(inplace=True)
    
    return df

def main():
    st.title("Student Results Viewer")

    # File upload for Excel file
    uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

    if uploaded_file is not None:
        # Load data from the uploaded Excel file
        df = load_data(uploaded_file)

        st.sidebar.subheader("Enter Roll Number")

        # Input field for roll number
        roll_number = st.sidebar.text_input("Roll Number")

        if roll_number:
            # Filter data based on the entered roll number
            student_result = df[df['Roll Number'] == roll_number]

            if not student_result.empty:
                st.subheader(f"Results for Roll Number: {roll_number}")
                # Display the student's result in a table format
                st.write(student_result)
            else:
                st.error("Student with this Roll Number not found")

if __name__ == "__main__":
    main()
