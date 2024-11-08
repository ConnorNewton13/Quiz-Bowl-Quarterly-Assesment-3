import tkinter as tk
from tkinter import messagebox
import sqlite3

def connect_db():
    """Establish connection to the database."""
    return sqlite3.connect('quiz_bowl.db')

def get_questions(category):
    """Fetch questions dynamically based on the category."""
    conn = connect_db()
    cursor = conn.cursor()

    # Mapping categories to respective database tables
    table_mapping = {
        "Human Resource Management": "HRQuestions",
        "Business Communications": "BusinessCommunicationQuestions",
        "Supply Chain Management": "SupplyChainManagementQuestions",
        "Business Applications Development": "BusinessApplicationsDevelopmentQuestions",
        "Business Analytics": "BusinessAnalyticsQuestions"
    }

    # Get the corresponding table name for the selected category
    table_name = table_mapping.get(category)
    
    if not table_name:
        print(f"Error: Category '{category}' does not have a corresponding table in the database.")
        return []

    try:
        print(f"Fetching questions for category '{category}' from table '{table_name}'...")
        cursor.execute(f"SELECT * FROM {table_name}")
        questions = cursor.fetchall()

        if not questions:
            print(f"No questions found for category '{category}'.")

    except sqlite3.Error as e:
        print(f"Error while querying the database: {e}")
        questions = []

    conn.close()
    return questions

def start_quiz_window(course):
    """Create a window to display the quiz for the selected course/category."""
    questions = get_questions(course)  # Get questions for the selected course/category

    if not questions:
        messagebox.showerror("Error", f"No questions available for the category '{course}'.")
        return

    score = 0
    question_index = 0

    def display_question(index):
        """Display the current question and options."""
        nonlocal question_index
        question = questions[index]
        question_label.config(text=f"Q{index + 1}: {question[1]}")

        var.set(None)  # Reset selected option
        option_1.config(text=question[2])
        option_2.config(text=question[3])
        option_3.config(text=question[4])
        option_4.config(text=question[5])

        submit_button.config(command=lambda: check_answer(index))

    def check_answer(index):
        """Check the selected answer and update score."""
        nonlocal score, question_index
        selected_option = var.get()

        if selected_option == questions[index][6]:
            score += 1

        question_index += 1
        if question_index < len(questions):
            display_question(question_index)
        else:
            messagebox.showinfo("Quiz Complete", f"Your final score is: {score}/{len(questions)}")
            quiz_window.quit()

    quiz_window = tk.Tk()
    quiz_window.title(f"{course} Quiz")

    question_label = tk.Label(quiz_window, text="", font=("Helvetica", 14), wraplength=400)
    question_label.pack(pady=10)

    var = tk.IntVar()

    option_frame = tk.Frame(quiz_window)
    option_frame.pack(pady=10)

    option_1 = tk.Radiobutton(option_frame, text="", variable=var, value=1, font=("Helvetica", 12))
    option_1.pack(anchor="w")

    option_2 = tk.Radiobutton(option_frame, text="", variable=var, value=2, font=("Helvetica", 12))
    option_2.pack(anchor="w")

    option_3 = tk.Radiobutton(option_frame, text="", variable=var, value=3, font=("Helvetica", 12))
    option_3.pack(anchor="w")

    option_4 = tk.Radiobutton(option_frame, text="", variable=var, value=4, font=("Helvetica", 12))
    option_4.pack(anchor="w")

    submit_button = tk.Button(quiz_window, text="Submit Answer", font=("Helvetica", 12), command=lambda: check_answer(question_index))
    submit_button.pack(pady=20)

    display_question(question_index)

    quiz_window.mainloop()

def category_selection_window():
    """Create a window to select quiz category."""
    window = tk.Tk()
    window.title("Select Quiz Category")

    label = tk.Label(window, text="Select a Category", font=("Helvetica", 14))
    label.pack(pady=20)

    categories = [
        "Select a Category", 
        "Human Resource Management", 
        "Business Communications", 
        "Supply Chain Management", 
        "Business Applications Development", 
        "Business Analytics"
    ]

    def start_quiz():
        """Start quiz after category selection."""
        selected_category = category_combobox.get()
        if selected_category != "Select a Category":
            window.destroy()
            start_quiz_window(selected_category)
        else:
            messagebox.showwarning("No Selection", "Please select a category.")

    category_combobox = tk.StringVar()
    category_combobox.set(categories[0])  # Default option

    category_menu = tk.OptionMenu(window, category_combobox, *categories)
    category_menu.pack(pady=20)

    start_button = tk.Button(window, text="Start Quiz", font=("Helvetica", 12), command=start_quiz)
    start_button.pack(pady=20)

    window.mainloop()

# Call the category selection window
category_selection_window()
