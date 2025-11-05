print("Welcome to the Test Grader version 2.4.12!")

grade = int(input("Enter your grade: "))

# Determine letter grade and message
if grade >= 90:
    letter_grade = "A"
    message = "Excellent work!"
elif grade >= 80:
    letter_grade = "B"
    message = "Good job!"
elif grade >= 70:
    letter_grade = "C"
    message = "Satisfactory."
elif grade >= 60:
    letter_grade = "D"
    message = "Need improvement."
else:
    letter_grade = "F"
    message = "Failed the test."

# Display the results
print(f"You have an {letter_grade}. {message}")

# Visual representation of the score
max_bars = 20
filled_bars = int((grade / 100) * max_bars)
empty_bars = max_bars - filled_bars

# Draw the score bar
print("\nYour Score Visualization:")
print(f"0{'-' * (max_bars-2)}100")
print(f"[{'#' * filled_bars}{' ' * empty_bars}]")
print(f" {grade}/100")

# This is version 2.4.0 of the test grader script.
# Added visual representation of score and fixed welcome message formatting.