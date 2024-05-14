import streamlit as st
import pandas as pd

 
 
 

 
        

# Function to retrieve student result by roll number
def get_student_result(df, roll_number):
    student_data = df[df['REGD. NO'] == roll_number]
    st.write(student_data)
    st.write(len(student_data))
    return student_data
       # Convert row to dictionary
 # Filter DataFrame by roll numbertodict
    
   

# Streamlit app title and description
st.title('Student Result Lookup')


# File uploader to upload Excel file
def main():
  data = pd.read_excel('21RES.xlsx')
  data.dropna(subset=['BRANCH'], inplace=True)
  dept_list=['CSE','IT','CSM','EEE','ECE']
  selected_dept = st.selectbox("Select Department", dept_list, key="selectbox1")
  df=data[data["BRANCH"]==selected_dept]
  df=df.dropna(axis=1, how='all')
  st.write(df.head())
  roll_number = st.text_input('Enter Roll Number')
  if st.button('Show Result'):
   student_result = get_student_result(df, roll_number)
   if student_result.empty():
    data = pd.DataFrame(student_result)
    st.table(data)
   else:
    st.write('Student not found. Please enter a valid roll number.')

  
  
   
   
    
    
  
   
   
 
 

if __name__ == "__main__":
    main()
      
       
 
           
     
          
              
               
            
                
  
    
     
