Student Success Platform (SSP) 🎓


A Python-based CLI tool designed to replace the chaos of paper records with clean, digital logic.

📖 Overview
The Student Success Platform (SSP) is a streamlined application built to help educators and class monitors manage student performance without needing a messy pile of papers.

Instead of calculating grades manually—which is slow and prone to errors—this program allows you to enter student details and marks, and it automatically handles the grading logic. It is a lightweight, text-based tool that demonstrates the power of Python's memory structures.

✨ Key Features
📝 Seamless Record Entry Input student details (Roll Number, Name) and marks for as many subjects as you need. The system adapts to your data.

🧠 Smart Auto-Grading Forget the calculator. The program validates your input (0-100) and automatically maps scores to the correct Letter Grade (A through F) instantly.

🔍 Instant Lookup Stop digging through stacks of paper. Simply type a Roll Number, and the system retrieves and displays that student's complete report card.

🛡️ Built-in Validation The system includes error handling to prevent mistakes. If you accidentally enter marks outside the valid 0-100 range, it warns you immediately.

🛠️ Technologies Used
Language: Python 3.x
Libraries: None (Built using standard Python libraries only)
Architecture: Command Line Interface (CLI)



🎮 How to Use (Testing Guide)
Once the program starts, you will be welcomed by the main menu. Here is how to navigate the platform:

1. Add Student Data (Option 1)
Select 1 from the menu.

Enter the Roll Number (e.g., 101) and Student Name.
Enter the number of subjects (e.g., 3).
Input the Subject Name (e.g., Maths) and Marks (e.g., 95).
Result: The system will automatically calculate and store the Grade 'A'.

2. Search for a Student (Option 2)
Select 2 from the main menu.
Enter the Roll Number you used previously (e.g., 101).
Result: The program displays a clean, formatted table showing that student's performance.

3. Exit (Option 3)
Select 3 to close the application cleanly.
