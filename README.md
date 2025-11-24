# Student-Success-Platform-SSP-
Student Record Management System (SRMS) 🎓

A Python-based CLI tool designed to automate student grade calculations and record organization.

📌 Overview

The Problem: Manual student administration is tedious and error-prone. Calculating grades by hand leads to calculation mistakes, and retrieving specific student records from physical paper stacks is inefficient.

The Solution: This SRMS is a command-line interface tool that automates the math and organization. It allows for instant data entry, automated grade calculation based on score logic, and formatted reporting.

Context: This project was built to meet the requirements of CPL 101, demonstrating mastery of Python's core memory structures (Lists and Dictionaries) without relying on external databases.

🚀 Features

📝 Dynamic Record Entry: Input student details (Roll No, Name) and marks for multiple subjects effortlessly.

🧠 Smart Grading Algorithm: Automated logic that maps numerical scores to Letter Grades instantly (e.g., 90 → 'A').

🔍 Instant Search: Retrieve a specific student's full academic record by simply entering their Roll Number.

📊 Professional Table View: Generates a clean, column-aligned marksheet directly in the console/terminal.


Steps to Install & Run the Project
1. Since this is a simple script, you don't need to install any heavy software or external packages.
2. Download the Code: Download the .py file (e.g., studentrecord.py) to your computer.
3. Open Terminal/Command Prompt: Navigate to the folder where you saved the file.
4. Run the Script: Type the following command and hit Enter: bash python main.py
Instructions for Testing Once the program starts, you will see a menu with 3 options. Here is how to test it:

1. EnterData(Option1):
   
o Select 1 to start adding students.
o Enter a Roll Number (e.g., 101) and Name.
o Enter the number of subjects (e.g., 3).
o Enter the Subject Name (e.g., Maths) and Marks (e.g., 95). o Check: See if it assigns Grade 'A' automatically.

2. SearchforaStudent(Option2):
   
o Select 2 from the main menu.
o Enter the Roll Number you just created (101).
o Check: The program should display a neat table with that student's marks and grades.

3. Exit(Option3):
o Select 3 to close the application.

