import numpy as np
import pandas as pd
def start_learning():
    print("Welcome to Python learning!")
    course = input("Which topic would you like to learn? (e.g., Data Analysis, Web Development, Machine Learning): ")
    
    if course.lower() == "data analysis":
            print(f"Great choice! Let's start learning {course} together.")
            Data_Analysis()
    elif course.lower() == "web development":
            print(f"Great choice! Let's start learning {course} together.")
            Web_Development()
    elif course.lower() == "machine learning":
            print(f"Great choice! Let's start learning {course} together.")
            Machine_Learning()
       
    else:
        print("ohhh invalid input! Please first choose a valid topic to start learning.")
    
def Data_Analysis():
        print("Data Analysis is a crucial skill in today's data-driven world.")
        print("We'll cover libraries like Pandas, NumPy, and Matplotlib.")
        print("Let's start with Pandas for data manipulation and analysis.")
def Web_Development():
        print("Web Development is a popular field for creating websites and web applications.")
        print("We'll explore frameworks like Django and Flask.")
def Machine_Learning():
        print("Machine Learning is a subset of artificial intelligence that focuses on building systems that can learn from data.")
        print("We'll dive into libraries like Scikit-learn and TensorFlow.")
        
        
start_learning()

    