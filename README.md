
# Student Records Management System

A web-based application built using Streamlit and SQLite to manage student records. This application allows you to perform CRUD (Create, Read, Update, Delete) operations on student data, including adding student information, viewing, searching, modifying, and deleting records.

## Features
- Create Table: Creates a table to store student records in SQLite.
- Add Record: Allows adding new student records with details like admission number, issue date, registration number, and personal information.
- View Records: Displays all student records stored in the database in a tabular format.
- Search Record: Search for student records by any of the available fields such as Admission Form No, Registration No, Name, etc.
- Modify Record: Modify existing student records by selecting the field to update.
- Delete Record: Delete a student record using the Registration No.
- Sort Records: Sort the records by Registration No for easy viewing.

## Technologies Used
- Streamlit: For building the interactive web app interface.
- SQLite: For database management and storage.
- Pandas: For handling and displaying student records in tabular form.

## Installation

### Prerequisites:
- Python 3.x
- Streamlit
- SQLite3
- Pandas

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/Lata2804/student-records-management.git
   cd student-records-management
2.Install the required dependencies:
pip install streamlit

3.Run the Streamlit app:

streamlit run student_db_app.py
Open your browser and go to the URL provided by Streamlit (usually http://localhost:2000).

### Small demo clip:



https://github.com/user-attachments/assets/8d393d36-58f4-4179-b89e-7631fa45d922



### Usage:
- Create Table: Click the "Create Table" button to create a new database table for storing student records.
- Add Record: Fill in the student details and click "Add Record" to store it in the database.
- View Records: View all stored student records in a tabular format.
- Search Record: Search for student records by entering a value in the specified search field.
- Modify Record: Select a record to modify by entering the Registration No and updating the desired field.
- Delete Record: Delete a record by entering the Registration No and clicking the "Delete Record" button.
- Sort Records: View the student records sorted by Registration No.
### Contributing:
Feel free to fork this project and submit pull requests. If you find any bugs or issues, please open an issue on GitHub.

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** license.

- You are free to copy, modify, distribute, and perform the work for **non-commercial purposes only**.
- **Commercial use** is not allowed under this license.
- You must **provide appropriate credit** when using or adapting this work, and indicate if changes were made.
- If you remix or adapt the material, you must distribute your contributions under the same license.

For more details, you can refer to the full legal code of the [CC BY-NC 4.0 License](https://creativecommons.org/licenses/by-nc/4.0/legalcode).
