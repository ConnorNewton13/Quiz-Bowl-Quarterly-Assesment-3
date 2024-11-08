import sqlite3

def create_db():
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS HRQuestions (
        question_id INTEGER PRIMARY KEY,
        question_text TEXT,
        option_1 TEXT,
        option_2 TEXT,
        option_3 TEXT,
        option_4 TEXT,
        correct_answer INTEGER
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS BusinessCommunicationQuestions (
        question_id INTEGER PRIMARY KEY,
        question_text TEXT,
        option_1 TEXT,
        option_2 TEXT,
        option_3 TEXT,
        option_4 TEXT,
        correct_answer INTEGER
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS SupplyChainManagementQuestions (
        question_id INTEGER PRIMARY KEY,
        question_text TEXT,
        option_1 TEXT,
        option_2 TEXT,
        option_3 TEXT,
        option_4 TEXT,
        correct_answer INTEGER
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS BusinessApplicationsDevelopmentQuestions (
        question_id INTEGER PRIMARY KEY,
        question_text TEXT,
        option_1 TEXT,
        option_2 TEXT,
        option_3 TEXT,
        option_4 TEXT,
        correct_answer INTEGER
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS BusinessAnalyticsQuestions (
        question_id INTEGER PRIMARY KEY,
        question_text TEXT,
        option_1 TEXT,
        option_2 TEXT,
        option_3 TEXT,
        option_4 TEXT,
        correct_answer INTEGER
    );
    """)

    hr_questions = [
        ("Which of the following is a primary function of human resource management?", "Developing marketing strategies", "Managing the financial records of the company", "Recruiting, training, and developing employees", "Conducting market research", 3),
        ("What is the purpose of a job analysis in HRM?", "To determine the compensation for the job", "To assess the financial performance of the department", "To identify the duties, responsibilities, and qualifications for a job", "To calculate the productivity of employees", 3),
        ("Which of the following is an example of a non-financial reward?", "Profit sharing", "Performance bonuses", "Paid time off", "Stock options", 3),
        ("The Equal Employment Opportunity (EEO) laws are primarily designed to:", "Ensure that all employees receive the same salary", "Prevent discrimination based on protected characteristics such as race, gender, and age", "Ensure that all job candidates pass the same background checks", "Regulate the number of employees a company can hire", 2),
        ("Which of the following is NOT a common method for employee performance appraisal?", "360-degree feedback", "Management by objectives (MBO)", "Random selection", "Graphic rating scales", 3),
        ("Which law requires employers to provide a safe and healthy workplace for their employees?", "The Civil Rights Act", "The Occupational Safety and Health Act (OSHA)", "The Family and Medical Leave Act (FMLA)", "The Fair Labor Standards Act (FLSA)", 2),
        ("What is the term for the process by which new employees are introduced to their company and its culture?", "Recruiting", "Orientation", "Job analysis", "Training needs assessment", 2),
        ("A company’s policy of providing equal opportunities for all employees, regardless of background, is known as:", "Affirmative action", "Employee engagement", "Job rotation", "Diversity and inclusion", 4),
        ("Which of the following is considered a 'soft skill' that HR professionals value most in candidates?", "Technical proficiency", "Problem-solving", "Computer programming", "Data analysis", 2),
        ("What is the main goal of a compensation strategy?", "To maximize employee retention", "To reduce recruitment costs", "To ensure legal compliance with pay laws", "To attract, motivate, and retain employees while aligning with organizational goals", 4)
    ]

    cursor.executemany("""
    INSERT INTO HRQuestions (question_text, option_1, option_2, option_3, option_4, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    """, hr_questions)

    bc_questions = [
        ("What is the primary purpose of business communication?", "To entertain employees", "To build relationships with customers", "To inform, persuade, and influence stakeholders", "To generate profits", 3),
        ("Which of the following is an example of non-verbal communication?", "Sending an email", "Giving a handshake", "Writing a report", "Reading a memo", 2),
        ("Which communication medium is best for conveying a complex, detailed message that requires careful explanation and reference to past documents?", "Email", "Phone call", "Video conference", "Written report", 4),
        ("What is the term for the process of modifying a message to fit the needs and understanding of the target audience?", "Encoding", "Decoding", "Noise", "Adaptation", 4),
        ("In business communication, what is the primary disadvantage of using email as a communication tool?", "It can be too formal", "It lacks immediacy", "It is prone to misunderstandings due to tone and context", "It is only suitable for long messages", 3),
        ("Which of the following is the best way to ensure that a business presentation is effective?", "Use complex technical jargon", "Stick strictly to the text of the slides", "Engage the audience with visuals and interactive elements", "Avoid asking questions to the audience", 3),
        ("What is a key benefit of using active listening in business communication?", "It helps to dominate the conversation", "It allows you to passively hear the speaker’s message", "It helps to foster understanding and build rapport", "It helps in avoiding difficult conversations", 3),
        ("Which of the following is considered a barrier to effective communication?", "Clear message", "Effective feedback", "Physical distractions", "Open body language", 3),
        ("In business writing, what is the main purpose of the executive summary?", "To provide a detailed breakdown of data", "To summarize the main points of a report for quick reading", "To explain the methods used in research", "To list all references used in the report", 2),
        ("Which of the following is an example of 'communication noise'?", "Clear and concise messaging", "Misinterpretation due to cultural differences", "Providing immediate feedback", "Correct spelling and grammar in emails", 2)
    ]

    cursor.executemany("""
    INSERT INTO BusinessCommunicationQuestions (question_text, option_1, option_2, option_3, option_4, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    """, bc_questions)

    scm_questions = [
        ("What is the primary objective of supply chain management?", "To minimize inventory costs", "To maximize customer satisfaction", "To optimize production schedules", "To ensure timely delivery of products", 2),
        ("Which of the following is a key component of supply chain management?", "Marketing strategy", "Financial accounting", "Logistics and transportation", "Human resources management", 3),
        ("What does the 'bullwhip effect' in supply chains refer to?", "Excessive stock at the customer level", "A decrease in demand for products", "Increasing order variances as orders move up the supply chain", "A sudden surge in product innovation", 3),
        ("Which of the following is a common method for managing supply chain risks?", "Supplier diversification", "Shortening lead times", "Limiting product offerings", "Increasing inventory levels", 1),
        ("What is 'just-in-time' inventory management?", "Ordering inventory in large batches", "Storing excess inventory for future demand", "Receiving goods only when they are needed in production", "Shipping inventory in advance to avoid stockouts", 3),
        ("What is the role of a supply chain manager?", "To develop marketing campaigns", "To oversee the entire production process", "To ensure goods are produced and delivered efficiently", "To handle customer complaints", 3),
        ("Which of the following is an example of a 'push' supply chain strategy?", "Ordering products based on customer demand", "Producing products based on forecasted demand", "Distributing products based on real-time sales", "Shipping goods after customer orders are received", 2),
        ("Which technology is often used in supply chain management to track goods in real time?", "Enterprise Resource Planning (ERP)", "Radio Frequency Identification (RFID)", "Customer Relationship Management (CRM)", "Product Lifecycle Management (PLM)", 2),
        ("What is a key benefit of supply chain collaboration?", "Increased competition among suppliers", "Better control over prices", "Improved product quality and faster delivery times", "Decreased dependency on technology", 3),
        ("Which of the following is an example of supply chain integration?", "Outsourcing production to multiple vendors", "Sharing inventory levels across different parts of the supply chain", "Increasing supplier prices", "Increasing transportation lead times", 2)
    ]

    cursor.executemany("""
    INSERT INTO SupplyChainManagementQuestions (question_text, option_1, option_2, option_3, option_4, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    """, scm_questions)

    bad_questions = [
        ("What is the primary purpose of business applications in an organization?", "To automate manual processes", "To collect customer feedback", "To manage company finances", "To track employee performance", 1),
        ("Which of the following is an example of a business application?", "Accounting software", "Web browser", "Social media platform", "Video conferencing app", 1),
        ("What is the main advantage of cloud-based business applications?", "They are cheaper than on-premise applications", "They offer unlimited customization", "They can be accessed from any location", "They don't require internet connectivity", 3),
        ("Which of the following is NOT typically a feature of enterprise resource planning (ERP) systems?", "Supply chain management", "Customer relationship management", "Database management", "Social media management", 4),
        ("Which programming language is commonly used for developing business applications?", "Python", "HTML", "C++", "JavaScript", 1),
        ("Which of the following best describes a database management system (DBMS)?", "A tool for sending emails", "A system for managing data storage and retrieval", "A platform for building websites", "A tool for creating spreadsheets", 2),
        ("In business application development, what is the purpose of a user interface (UI)?", "To manage backend processes", "To facilitate user interaction with the application", "To store data", "To provide security features", 2),
        ("What is an example of a business application that uses data analytics?", "Email client", "Accounting software", "Customer relationship management (CRM)", "Social media platform", 3),
        ("Which of the following is a key consideration when selecting business application software?", "The color scheme of the interface", "The availability of mobile versions", "The security features and data protection", "The number of users it supports", 3),
        ("What is 'agile development' in the context of business application development?", "A method of software development focused on flexibility and iterative progress", "A type of data encryption technique", "A strategy for long-term software maintenance", "A platform for marketing software", 1)
    ]

    cursor.executemany("""
    INSERT INTO BusinessApplicationsDevelopmentQuestions (question_text, option_1, option_2, option_3, option_4, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    """, bad_questions)

    ba_questions = [
        ("What is the main goal of business analytics?", "To analyze customer preferences", "To optimize business performance through data-driven insights", "To reduce operational costs", "To increase brand awareness", 2),
        ("Which of the following is a key component of business analytics?", "Data mining", "Market research", "Product design", "Employee satisfaction", 1),
        ("What is the purpose of predictive analytics?", "To analyze past data for trends", "To predict future outcomes based on historical data", "To collect raw data from the market", "To visualize data trends", 2),
        ("Which of the following is an example of descriptive analytics?", "Predicting future sales based on past data", "Summarizing sales data to show trends over time", "Optimizing business operations for better performance", "Using real-time data to forecast market conditions", 2),
        ("What does 'big data' refer to in business analytics?", "Data that is too large to be processed by traditional methods", "Data that is easy to analyze", "Data from small businesses", "Data collected from social media platforms", 1),
        ("Which tool is commonly used for data visualization in business analytics?", "Excel", "PowerPoint", "Tableau", "Word", 3),
        ("What is a key challenge when implementing business analytics in a company?", "High-quality data collection", "Lack of technical skills in the workforce", "Data privacy concerns", "Integrating analytics with existing business processes", 4),
        ("Which type of data is typically analyzed using business analytics?", "Qualitative data from focus groups", "Historical transactional data", "Customer feedback data", "Employee performance data", 2),
        ("What does 'data cleaning' involve in business analytics?", "Storing large amounts of data", "Ensuring that data is accurate, complete, and consistent", "Visualizing data trends", "Predicting future sales patterns", 2),
        ("Which of the following is a benefit of business analytics?", "Better decision-making based on data insights", "Faster product development", "Increased focus on employee satisfaction", "Higher advertising budgets", 1)
    ]

    cursor.executemany("""
    INSERT INTO BusinessAnalyticsQuestions (question_text, option_1, option_2, option_3, option_4, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    """, ba_questions)

    conn.commit()

    conn.close()

    print("Database created and populated with all quiz questions.")

create_db()