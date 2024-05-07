import streamlit as st
import pandas as pd

def main():
    st.title('Student Record Search')

    # Load sample data (replace with your DataFrame loading logic)
    data = {
        'Roll Number': [101, 102, 103, 104],
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [20, 22, 21, 23],
        'Grade': ['A', 'B', 'B', 'A']
    }
    df = pd.DataFrame(data)

    # Input field for user to enter roll number
    roll_number = st.number_input('Enter Roll Number:', min_value=1, step=1)

    if st.button('Search'):
        # Filter DataFrame to find row with matching roll number
        row = df[df['Roll Number'] == roll_number]

        # Display row if found
        if not row.empty:
            st.write('Student Record:')
            st.table(row)
        else:
            st.write(f'No student found with Roll Number: {roll_number}')

if __name__ == '__main__':
    main()
