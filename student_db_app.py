import streamlit as st
import sqlite3
from datetime import date
import pandas as pd

# Database connection
conn = sqlite3.connect('student.db', check_same_thread=False)
c = conn.cursor()

# Column names
show_columns = [
    "Admission Form No", "Issue Date", "Registration No",
    "Name", "Father's Name", "Mother's Name", "Gender",
    "Date of Birth", "Phone", "Email", "Address"
]
column = [
    "admission_no", "issue_date", "registration_no",
    "name", "father_name", "mother_name", "gender",
    "dob", "phone", "email", "address"
]

# Functions
def create_table():
    c.execute('''DROP TABLE IF EXISTS student''')
    c.execute('''
        CREATE TABLE student (
            admission_no INTEGER PRIMARY KEY,
            issue_date DATE,
            registration_no INTEGER UNIQUE,
            name VARCHAR(50),
            father_name VARCHAR(50),
            mother_name VARCHAR(50),
            gender VARCHAR(10),
            dob DATE,
            phone VARCHAR(15),
            email VARCHAR(50),
            address TEXT
        )
    ''')
    conn.commit()
    st.success("Table created successfully!")

def add_record():
    with st.form("add_form"):
        admno = st.number_input("Admission Form No", min_value=1, step=1)
        issuedate = st.date_input("Issue Date", value=date.today())
        regno = st.number_input("Registration No", min_value=1, step=1)
        name = st.text_input("Name")
        father = st.text_input("Father's Name")
        mother = st.text_input("Mother's Name")
        gender = st.radio("Gender", ["Male", "Female", "Other"])
        dob = st.date_input("Date of Birth", min_value=date(1980, 1, 1), max_value=date.today())
        phone = st.text_input("Phone Number")
        email = st.text_input("Email Address")
        address = st.text_area("Address")
        submitted = st.form_submit_button("Add Record")
        
        if submitted:
            try:
                c.execute('''INSERT INTO student VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                          (admno, issuedate, regno, name, father, mother, gender, dob, phone, email, address))
                conn.commit()
                st.success("Record added successfully!")
            except Exception as e:
                st.error(f"Error: {e}")

def view_records():
    c.execute("SELECT * FROM student")
    rows = c.fetchall()
    if rows:
        df = pd.DataFrame(rows, columns=show_columns)
        st.dataframe(df)
    else:
        st.warning("No records found!")

def search_record(column_name, search_value):
    query = f"SELECT * FROM student WHERE {column_name} = ?"
    c.execute(query, (search_value,))
    rows = c.fetchall()
    if rows:
        df = pd.DataFrame(rows, columns=show_columns)
        st.dataframe(df)
    else:
        st.warning("No matching records found!")

def modify_record():
    with st.form("modify_form"):
        regno = st.number_input("Enter Registration No", min_value=1, step=1)
        field_to_update = st.selectbox("Field to Modify", show_columns)
        new_value = st.text_input("New Value")
        submitted = st.form_submit_button("Update Record")
        
        if submitted:
            try:
                field_name = column[show_columns.index(field_to_update)]
                c.execute(f"UPDATE student SET {field_name} = ? WHERE registration_no = ?", (new_value, regno))
                conn.commit()
                st.success("Record updated successfully!")
            except Exception as e:
                st.error(f"Error: {e}")

def delete_record():
    regno = st.number_input("Enter Registration No to Delete", min_value=1, step=1)
    if st.button("Delete Record"):
        try:
            c.execute("DELETE FROM student WHERE registration_no = ?", (regno,))
            conn.commit()
            st.success("Record deleted successfully!")
        except Exception as e:
            st.error(f"Error: {e}")

def sort_records():
    c.execute("SELECT * FROM student ORDER BY registration_no")
    rows = c.fetchall()
    if rows:
        df = pd.DataFrame(rows, columns=show_columns)
        st.dataframe(df)
    else:
        st.warning("No records found!")

# Streamlit App Layout
st.title("Student Records Management System")

menu = st.sidebar.selectbox("Menu", ["Create Table", "Add Record", "View Records", "Search Record", "Modify Record", "Delete Record", "Sort Records"])

if menu == "Create Table":
    st.subheader("Create Table")
    if st.button("Create Table"):
        create_table()

elif menu == "Add Record":
    st.subheader("Add Record")
    add_record()

elif menu == "View Records":
    st.subheader("View All Records")
    view_records()

elif menu == "Search Record":
    st.subheader("Search Record")
    search_field = st.selectbox("Search By", show_columns)
    search_value = st.text_input("Enter Search Value")
    if st.button("Search"):
        search_record(column[show_columns.index(search_field)], search_value)

elif menu == "Modify Record":
    st.subheader("Modify Record")
    modify_record()

elif menu == "Delete Record":
    st.subheader("Delete Record")
    delete_record()

elif menu == "Sort Records":
    st.subheader("Sort Records by Registration No")
    if st.button("Sort"):
        sort_records()