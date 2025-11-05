print("="*50)
print("Welcome to the Test Grader version 6.0.0!")
print("A professional grade calculation tool")
print("="*50)

def get_valid_grade():
    """Get a valid grade input from the user."""
    while True:
        try:
            grade = int(input("\nEnter your grade (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("⚠️ Please enter a valid grade between 0 and 100.")
        except ValueError:
            print("⚠️ Please enter a numeric value ,take you.")

def determine_grade(score):
    """Determine letter grade, message, and color code based on score."""
    if score >= 90:
        return "A", "Excellent work! Outstanding performance!", "A+"
    elif score >= 85:
        return "B+", "Very good job! Above average performance.", "B+"
    elif score >= 80:
        return "B", "Good job! Strong performance.", "B" 
    elif score >= 75:
        return "C+", "Fair work. Above average performance.", "C+"
    elif score >= 70:
        return "C", "Satisfactory. Average performance.", "C"
    elif score >= 65:
        return "D+", "Needs some improvement. Below average.", "D+"
    elif score >= 60:
        return "D", "Needs significant improvement.", "D"
    else:
        return "F", "Failed the test. Please see the instructor.", "F"

def display_score_bar(score):
    """Display a visual representation of the score."""
    max_bars = 40
    filled_bars = int((score / 100) * max_bars)
    empty_bars = max_bars - filled_bars
    
    print("\n📊 Your Score Visualization:")
    print(f"0{'-' * (max_bars-2)}100")
    print(f"[{'#' * filled_bars}{' ' * empty_bars}]")
    print(f" {score}/100")
    
    # Add a performance indicator
    if score >= 90:
        indicator = "🌟 Outstanding"
    elif score >= 80:
        indicator = "✨ Excellent"
    elif score >= 70:
        indicator = "👍 Good"
    elif score >= 60:
        indicator = "🔍 Passing"
    else:
        indicator = "⚠️ Needs Improvement"
        
    print(f"Performance: {indicator}")

def display_grade_boundaries():
    """Display the grade boundaries."""
    print("\n📋 Grade Boundaries:")
    boundaries = [
        ("A", "90-100", "Outstanding"),
        ("B+", "85-89", "Very Good"),
        ("B", "80-84", "Good"),
        ("C+", "75-79", "Above Average"),
        ("C", "70-74", "Average"),
        ("D+", "65-69", "Below Average"),
        ("D", "60-64", "Poor"),
        ("F", "0-59", "Failing")
    ]
    
    for grade, range_val, descriptor in boundaries:
        print(f"{grade}: {range_val} - {descriptor}")

def generate_feedback(score, letter_grade):
    """Generate detailed feedback based on the score."""
    if letter_grade == "A":
        if score == 100:
            return "Perfect score! Outstanding achievement!"
        else:
            return f"Your performance is excellent! Keep up the great work. Only {100-score} points away from a perfect score!"
    elif letter_grade in ["B+", "B"]:
        return f"Good work! You're {90-score} points away from an A. Focus on improving key areas."
    elif letter_grade in ["C+", "C"]:
        return f"You're doing okay, but have room to improve. You need {80-score} more points for a B."
    elif letter_grade in ["D+", "D"]:
        return f"You're struggling in this subject. Consider seeking additional help. You need {70-score} more points for a C."
    else:
        points_needed = 60 - score
        return f"You need to significantly improve your understanding of the material. You need {points_needed} more points to pass. Please see your instructor for help."

def main():
    try:
        # Get grade input
        grade = get_valid_grade()
        
        # Determine grade information
        letter_grade, message, grade_category = determine_grade(grade)
        
        # Display results
        print("\n"+"="*50)
        print(f"📝 RESULT: You have a{'n' if letter_grade[0] in ['A', 'F'] else ''} {letter_grade}. {message}")
        
        # Display score visualization
        display_score_bar(grade)
        
        # Display grade boundaries
        display_grade_boundaries()
        
        # Display personalized feedback
        print("\n💬 Personalized Feedback:")
        print(generate_feedback(grade, letter_grade))
        print("="*50)
        
        # Ask if the user wants to grade another test
        retry = input("\nWould you like to grade another test? (yes/no): ").lower()
        if retry in ["yes", "y"]:
            # Use a loop instead of recursion to prevent stack overflow
            return True
        else:
            print("\nThank you for using Test Grader v6.0.0! Goodbye.")
            return False
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please try again.")
        return True

# Run the program
if __name__ == "__main__":
    # Use a loop instead of recursion for multiple test grading
    continue_grading = True
    while continue_grading:
        continue_grading = main()
