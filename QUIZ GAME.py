import time

# --------------------------------------------
# Quiz Data: 5 questions for Data Science quiz
# --------------------------------------------
QUESTIONS = [
    {
        "question": "Which language is used for data science?",
        "options": {
            "A": "Python",
            "B": "Java",
            "C": "C++",
            "D": "Ruby"
        },
        "correct": "Python"
    },
    {
        "question": "Which Python library provides the DataFrame structure?",
        "options": {
            "A": "NumPy",
            "B": "Pandas",
            "C": "Matplotlib",
            "D": "SciPy"
        },
        "correct": "Pandas"
    },
    {
        "question": "Which of the following is a supervised machine learning algorithm?",
        "options": {
            "A": "K-Means",
            "B": "Linear Regression",
            "C": "Apriori",
            "D": "PCA"
        },
        "correct": "Linear Regression"
    },
    {
        "question": "What does SQL stand for?",
        "options": {
            "A": "Structured Query Language",
            "B": "Simple Query Logic",
            "C": "Structured Question Language",
            "D": "Sequential Query Language"
        },
        "correct": "Structured Query Language"
    },
    {
        "question": "Which chart type is best for showing trends over time?",
        "options": {
            "A": "Line chart",
            "B": "Bar chart",
            "C": "Pie chart",
            "D": "Scatter plot"
        },
        "correct": "Line chart"
    }
]

# --------------------------------------------
# Helper function to ask a single question
# --------------------------------------------
def ask_question(question_data, q_number, total):
    """Display a question, get user answer, return True if correct."""
    print(f"\n📌 QUESTION {q_number} OF {total}")
    print(f"\n{question_data['question']}\n")
    
    # Display options A, B, C, D
    for key, text in question_data["options"].items():
        print(f"   {key}. {text}")
    
    correct_answer = question_data["correct"]
    options_dict = question_data["options"]
    
    # Loop until a valid answer is given
    while True:
        user_input = input("\nYour answer (letter or full text): ").strip()
        if not user_input:
            print("❌ Please enter an answer.")
            continue
        
        upper_input = user_input.upper()
        
        # Case 1: User entered a letter (A, B, C, D)
        if upper_input in options_dict:
            chosen_text = options_dict[upper_input]
            if chosen_text.lower() == correct_answer.lower():
                print("✅ Correct!\n")
                return True
            else:
                print(f"❌ Wrong! The correct answer is: {correct_answer}\n")
                return False
        
        # Case 2: User entered the full answer text
        elif user_input.lower() == correct_answer.lower():
            print("✅ Correct!\n")
            return True
        
        # Case 3: Invalid input (neither a valid letter nor correct answer)
        else:
            print("❌ Invalid choice. Please enter the letter (A, B, C, D) or the exact answer text.")
            # Show options again to help the user
            print("Options:")
            for key, text in options_dict.items():
                print(f"   {key}. {text}")

# --------------------------------------------
# Main quiz game
# --------------------------------------------
def run_quiz():
    """Runs the full quiz, tracks score, displays final result."""
    print("\n" + "="*50)
    print("        🧠 QUIZ MASTER CHALLENGE 🧠")
    print("="*50)
    print("Answer each question correctly to earn 1 point per question.")
    print("You can answer by typing the letter (A, B, C, D) or the full answer text.")
    print("\nLet's begin! Good luck!")
    time.sleep(1)
    
    score = 0
    total_questions = len(QUESTIONS)
    
    # Loop through each question
    for idx, q_data in enumerate(QUESTIONS, start=1):
        if ask_question(q_data, idx, total_questions):
            score += 1
        
        # Show current score after each question (optional but nice)
        print(f"📊 Current score: {score} / {total_questions}")
        if idx != total_questions:
            time.sleep(0.8)  # small pause before next question
    
    # ---------- FINAL RESULT ----------
    print("\n" + "="*50)
    print("            🏆 QUIZ COMPLETED 🏆")
    print("="*50)
    print(f"\n✨ Your final score: {score} out of {total_questions} ✨")
    
    # Percentage and feedback message
    percentage = (score / total_questions) * 100
    print(f"📈 Percentage: {percentage:.1f}%")
    
    if percentage == 100:
        print("🏅 Perfect! You are a true Quiz Master! 🎉")
    elif percentage >= 80:
        print("🌟 Great job! You really know your stuff!")
    elif percentage >= 60:
        print("👍 Good effort! A little more practice and you'll master it.")
    else:
        print("📚 Keep learning! Try the quiz again to improve your score.")
    
    print("\n" + "="*50)
    print("Thanks for playing! Each correct answer gives you 1 point.")
    print("="*50)

# --------------------------------------------
# Replay option and entry point
# --------------------------------------------
def main():
    """Main entry point with replay functionality."""
    while True:
        run_quiz()
        play_again = input("\n🔁 Play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("\n👋 Thanks for playing! Stay curious and keep learning.\n")
            break
        print("\n🔄 Restarting quiz...\n")
        time.sleep(1)

if __name__ == "__main__":
    main()