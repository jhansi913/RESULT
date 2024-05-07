import streamlit as st
import pandas as pd

df = pd.read_excel('21RES.xlsx')
top_3=df.head(5)
st.dataframe(top_3)

 
        

# Function to retrieve student result by roll number
def get_student_result(df, roll_number):
    student_data = df[df['roll_number'] == roll_number]
    st.write(student_data)
    st.write(len(student_data))
    return student_data.iloc[0].to_dict()  # Convert row to dictionary
 # Filter DataFrame by roll number
    
   

# Streamlit app title and description
st.title('Student Result Lookup')


# File uploader to upload Excel file
def main():
 if df is not None:
  roll_number = st.text_input('Enter Roll Number')
  if st.button('Show Result'):
   student_result = get_student_result(df, roll_number)
   if student_result:
    data = pd.DataFrame(student_result)
    st.table(data)
   else:
    st.write('Student not found. Please enter a valid roll number.')

  
  
   
   
    
    
  
   
   
 
 

if __name__ == "__main__":
    main()
      
       
 
           
     
          
              
               
            
                
  
    
     
