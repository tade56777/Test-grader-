import os
import sys
from datetime import datetime

# Test Grader v10.0.0 - Ultimate Edition
# The most advanced test grading system with comprehensive features

class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Display the application banner"""
    clear_screen()
    print(Colors.BOLD + Colors.OKBLUE + "="*60)
    print("           TEST GRADER v10.0.0 - ULTIMATE EDITION")
    print("           Professional Grade Analysis System")
    print("="*60 + Colors.ENDC)
    print()

def get_valid_grade():
    """Get a valid grade input with enhanced validation"""
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        try:
            grade_input = input(f"\n{Colors.OKBLUE}Enter your grade (0-100):{Colors.ENDC} ")
            grade = float(grade_input)
            
            if 0 <= grade <= 100:
                return grade
            else:
                print(f"{Colors.WARNING}⚠️  Grade must be between 0 and 100. Please try again.{Colors.ENDC}")
                attempts += 1
        except ValueError:
            print(f"{Colors.FAIL}❌ Invalid input! Please enter a numeric value.{Colors.ENDC}")
            attempts += 1
        except KeyboardInterrupt:
            print(f"\n{Colors.WARNING}Operation cancelled by user.{Colors.ENDC}")
            sys.exit(0)
    
    print(f"{Colors.FAIL}Too many invalid attempts. Exiting...{Colors.ENDC}")
    sys.exit(1)

def determine_grade_advanced(score):
    """Advanced grading system with detailed categorization"""
    if score >= 97:
        return "A+", "Outstanding! Exceptional mastery!", "🌟", Colors.OKGREEN
    elif score >= 93:
        return "A", "Excellent work! Superior performance!", "⭐", Colors.OKGREEN
    elif score >= 90:
        return "A-", "Great job! Strong understanding!", "✨", Colors.OKGREEN
    elif score >= 87:
        return "B+", "Very good! Above average work!", "🎯", Colors.OKCYAN
    elif score >= 83:
        return "B", "Good work! Solid performance!", "👍", Colors.OKCYAN
    elif score >= 80:
        return "B-", "Decent job! Room for growth!", "📈", Colors.OKCYAN
    elif score >= 77:
        return "C+", "Fair work! Satisfactory!", "✓", Colors.WARNING
    elif score >= 73:
        return "C", "Average performance!", "📝", Colors.WARNING
    elif score >= 70:
        return "C-", "Passing but needs improvement!", "⚠️", Colors.WARNING
    elif score >= 67:
        return "D+", "Below average. More study needed!", "📚", Colors.WARNING
    elif score >= 63:
        return "D", "Poor performance. Significant improvement needed!", "⚡", Colors.FAIL
    elif score >= 60:
        return "D-", "Barely passing. Critical improvement required!", "🚻", Colors.FAIL
    else:
        return "F", "Failed. Please seek help immediately!", "❌", Colors.FAIL

def calculate_gpa(letter_grade):
    """Calculate GPA equivalent"""
    gpa_map = {
        "A+": 4.0, "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D+": 1.3, "D": 1.0, "D-": 0.7,
        "F": 0.0
    }
    return gpa_map.get(letter_grade, 0.0)

def display_advanced_visualization(score, letter_grade):
    """Display enhanced visual representation with multiple bars"""
    max_bars = 50
    filled_bars = int((score / 100) * max_bars)
    empty_bars = max_bars - filled_bars
    
    print("\n" + Colors.BOLD + "📊 SCORE VISUALIZATION" + Colors.ENDC)
    print("─" * 60)
    
    # Main progress bar
    print(f"Score: {score:.1f}%")
    print(f"0{'─' * (max_bars-2)}100")
    
    # Color-coded bar
    if score >= 90:
        bar_color = Colors.OKGREEN
    elif score >= 80:
        bar_color = Colors.OKCYAN
    elif score >= 70:
        bar_color = Colors.WARNING
    else:
        bar_color = Colors.FAIL
    
    print(f"[{bar_color}{'█' * filled_bars}{Colors.ENDC}{' ' * empty_bars}]")
    
    # Percentage markers
    markers = "0%       25%      50%      75%      100%"
    print(markers)
    print()

def generate_detailed_feedback(score, letter_grade):
    """Generate comprehensive feedback with actionable advice"""
    feedback = []
    
    if letter_grade in ["A+", "A", "A-"]:
        feedback.append("🎓 Outstanding Achievement!")
        feedback.append("   • You've demonstrated exceptional understanding")
        feedback.append("   • Continue to challenge yourself with advanced material")
        feedback.append("   • Consider helping peers who may be struggling")
    elif letter_grade in ["B+", "B", "B-"]:
        feedback.append("✨ Good Performance!")
        feedback.append(f"   • You're {90-score:.1f} points from an A")
        feedback.append("   • Review the concepts you found challenging")
        feedback.append("   • Focus on mastering the fundamentals")
    elif letter_grade in ["C+", "C", "C-"]:
        feedback.append("📚 Room for Improvement")
        feedback.append(f"   • You need {80-score:.1f} more points for a B")
        feedback.append("   • Schedule study sessions to review material")
        feedback.append("   • Consider forming a study group")
        feedback.append("   • Seek help during office hours")
    elif letter_grade in ["D+", "D", "D-"]:
        feedback.append("⚠️ Critical Improvement Needed")
        feedback.append(f"   • You need {70-score:.1f} more points to pass with a C")
        feedback.append("   • Immediate action required!")
        feedback.append("   • Meet with your instructor this week")
        feedback.append("   • Consider tutoring services")
        feedback.append("   • Review all course materials thoroughly")
    else:
        feedback.append("❌ Failed - Immediate Action Required")
        feedback.append(f"   • You need {60-score:.1f} more points to pass")
        feedback.append("   • Schedule an urgent meeting with your instructor")
        feedback.append("   • Explore academic support resources")
        feedback.append("   • Develop a comprehensive study plan")
        feedback.append("   • Consider if course withdrawal is an option")
    
    return "\n".join(feedback)

def display_grade_statistics(score, letter_grade, gpa):
    """Display statistical information"""
    print(Colors.BOLD + "\n📈 GRADE STATISTICS" + Colors.ENDC)
    print("─" * 60)
    print(f"Numerical Score:    {score:.2f}/100")
    print(f"Letter Grade:       {letter_grade}")
    print(f"GPA Equivalent:     {gpa:.2f}/4.00")
    print(f"Percentage:         {score:.1f}%")
    
    # Calculate percentile (simplified)
    if score >= 90:
        percentile = "Top 10%"
    elif score >= 80:
        percentile = "Top 25%"
    elif score >= 70:
        percentile = "Top 50%"
    elif score >= 60:
        percentile = "Bottom 40%"
    else:
        percentile = "Bottom 25%"
    
    print(f"Estimated Rank:     {percentile}")
    print()

def display_comprehensive_boundaries():
    """Display complete grade boundaries table"""
    print(Colors.BOLD + "\n📋 COMPLETE GRADING SCALE" + Colors.ENDC)
    print("─" * 60)
    
    boundaries = [
        ("A+", "97-100", "4.0", "Outstanding"),
        ("A ", "93-96",  "4.0", "Excellent"),
        ("A-", "90-92",  "3.7", "Great"),
        ("B+", "87-89",  "3.3", "Very Good"),
        ("B ", "83-86",  "3.0", "Good"),
        ("B-", "80-82",  "2.7", "Decent"),
        ("C+", "77-79",  "2.3", "Fair"),
        ("C ", "73-76",  "2.0", "Average"),
        ("C-", "70-72",  "1.7", "Passing"),
        ("D+", "67-69",  "1.3", "Below Average"),
        ("D ", "63-66",  "1.0", "Poor"),
        ("D-", "60-62",  "0.7", "Barely Passing"),
        ("F ", "0-59",   "0.0", "Failing")
    ]
    
    print(f"{'Grade':<6} {'Range':<10} {'GPA':<6} {'Description'}")
    print("─" * 60)
    for grade, range_val, gpa, desc in boundaries:
        print(f"{grade:<6} {range_val:<10} {gpa:<6} {desc}")
    print()

def save_grade_report(score, letter_grade, gpa, timestamp):
    """Save grade report to file"""
    try:
        filename = "grade_history.txt"
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"\n{'='*60}\n")
            f.write(f"Test Grader v10.0.0 - Grade Report\n")
            f.write(f"Timestamp: {timestamp}\n")
            f.write(f"{'='*60}\n")
            f.write(f"Score: {score:.2f}/100\n")
            f.write(f"Letter Grade: {letter_grade}\n")
            f.write(f"GPA: {gpa:.2f}/4.00\n")
            f.write(f"{'='*60}\n\n")
        return True
    except Exception as e:
        print(f"{Colors.WARNING}Note: Could not save report to file: {e}{Colors.ENDC}")
        return False

def display_menu():
    """Display main menu options"""
    print(Colors.BOLD + "\n🎯 OPTIONS" + Colors.ENDC)
    print("─" * 60)
    print("1. Grade another test")
    print("2. View grading scale")
    print("3. View grade history")
    print("4. Exit")
    print()

def main():
    """Main application loop"""
    print_banner()
    
    grade_count = 0
    total_score = 0
    
    while True:
        try:
            # Get grade input
            grade = get_valid_grade()
            grade_count += 1
            total_score += grade
            
            # Determine grade information
            letter_grade, message, emoji, color = determine_grade_advanced(grade)
            gpa = calculate_gpa(letter_grade)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Display results
            print("\n" + "="*60)
            print(color + Colors.BOLD + f"   {emoji} RESULT: {letter_grade} - {message}" + Colors.ENDC)
            print("="*60)
            
            # Display visualization
            display_advanced_visualization(grade, letter_grade)
            
            # Display statistics
            display_grade_statistics(grade, letter_grade, gpa)
            
            # Display feedback
            print(Colors.BOLD + "\n💬 PERSONALIZED FEEDBACK" + Colors.ENDC)
            print("─" * 60)
            print(generate_detailed_feedback(grade, letter_grade))
            print()
            
            # Save report
            if save_grade_report(grade, letter_grade, gpa, timestamp):
                print(f"{Colors.OKGREEN}✓ Report saved to grade_history.txt{Colors.ENDC}")
            
            # Display statistics for session
            if grade_count > 1:
                avg_score = total_score / grade_count
                print(f"\n{Colors.OKCYAN}📊 Session Stats: {grade_count} tests graded | Average: {avg_score:.1f}%{Colors.ENDC}")
            
            # Ask for next action
            display_menu()
            choice = input(f"{Colors.OKBLUE}Enter your choice (1-4):{Colors.ENDC} ").strip()
            
            if choice == "1":
                print_banner()
                continue
            elif choice == "2":
                display_comprehensive_boundaries()
                input(f"\n{Colors.OKBLUE}Press Enter to continue...{Colors.ENDC}")
                print_banner()
            elif choice == "3":
                try:
                    with open("grade_history.txt", "r", encoding="utf-8") as f:
                        print("\n" + Colors.BOLD + "📚 GRADE HISTORY" + Colors.ENDC)
                        print("─" * 60)
                        print(f.read())
                        input(f"\n{Colors.OKBLUE}Press Enter to continue...{Colors.ENDC}")
                        print_banner()
                except FileNotFoundError:
                    print(f"{Colors.WARNING}No grade history found.{Colors.ENDC}")
                    input(f"\n{Colors.OKBLUE}Press Enter to continue...{Colors.ENDC}")
                    print_banner()
            elif choice == "4":
                print(f"\n{Colors.OKGREEN}Thank you for using Test Grader v10.0.0!{Colors.ENDC}")
                print(f"{Colors.OKCYAN}Graded {grade_count} test(s) this session.{Colors.ENDC}")
                print(f"{Colors.BOLD}Goodbye! 👋{Colors.ENDC}\n")
                break
            else:
                print(f"{Colors.WARNING}Invalid choice. Continuing...{Colors.ENDC}")
                print_banner()
                
        except KeyboardInterrupt:
            print(f"\n\n{Colors.WARNING}Program interrupted by user.{Colors.ENDC}")
            print(f"{Colors.OKGREEN}Thank you for using Test Grader v10.0.0! Goodbye! 👋{Colors.ENDC}\n")
            break
        except Exception as e:
            print(f"\n{Colors.FAIL}An unexpected error occurred: {e}{Colors.ENDC}")
            print(f"{Colors.WARNING}Please try again or contact support.{Colors.ENDC}\n")
            continue

if __name__ == "__main__":
    main()