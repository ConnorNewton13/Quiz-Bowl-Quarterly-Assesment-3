This is the Quiz Bowl Game. 
The Quiz Bowl Application is a Python-based quiz system that allows users to select a category and answer multiple-choice questions from a connected SQLite database. The questions are categorized into different fields, such as Human Resource Management (HR), Business Communications, Supply Chain Management, Business Applications Development, and Business Analytics.

The application is built using Tkinter for the graphical user interface (GUI), and SQLite3 for the database management. The database stores the quiz questions, and the application fetches questions dynamically based on the selected category.

Features
Category Selection: Users can select a category to start the quiz.
Multiple-Choice Questions: Each question has four options, with one correct answer.
Score Tracking: The quiz tracks the user's score and displays it at the end.
Database-Driven: Questions are stored and fetched from an SQLite database.

Database Setup
The questions are stored in an SQLite database called quiz_bowl.py. You need to ensure the database is set up with the required tables and data.

Steps to Initialize Database
Download or clone this project.
Ensure the database is created and populated by running the following code. This will create the database and insert quiz questions into the database.

Running the Quiz Bowl Application
Once the database is set up, you can run the main quiz application.

Steps to Run the Application
Make sure the quiz_bowl.db is in the same directory as your Python script.
Run the following Python script to start the quiz application:

How to Play
Run the Python script.
Select a quiz category (e.g., Human Resource Management).
Answer the multiple-choice questions.
The score will be displayed at the end of the quiz.
