import tkinter as tk
from tkinter import messagebox
import random
from questions import questions

# Extract unique topics from the questions list
AVAILABLE_TOPICS = sorted(set(q["topic"] for q in questions))

# Color Palette
COLORS = {
    "dark_blue": "#03045E",
    "medium_blue": "#023E8A",
    "light_blue": "#48CAE4",
    "very_light_blue": "#CAF0F8",
    "bright_blue": "#0096C7",
    "correct": "green",
    "incorrect": "red"
}

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Code Quiz Generator")
        self.root.geometry("650x500")
        self.root.configure(bg=COLORS["very_light_blue"])

        self.selected_topic = tk.StringVar()
        self.selected_answer = tk.IntVar()
        self.current_question = None

        self.create_widgets()

    def create_widgets(self):
        """Create GUI components."""
        tk.Label(self.root, text="Available Topics:", bg=COLORS["very_light_blue"], font=("Arial", 12, "bold")).pack(pady=5)
        self.topics_label = tk.Label(self.root, text=", ".join(AVAILABLE_TOPICS), bg=COLORS["very_light_blue"], font=("Arial", 10), fg=COLORS["dark_blue"])
        self.topics_label.pack(pady=5)

        tk.Label(self.root, text="Enter a Topic:", bg=COLORS["very_light_blue"], font=("Arial", 12)).pack(pady=5)
        self.topic_entry = tk.Entry(self.root, font=("Arial", 12))
        self.topic_entry.pack(pady=5)

        tk.Button(self.root, text="Generate Python Question", bg=COLORS["bright_blue"], fg="white", 
                  font=("Arial", 12), command=self.generate_question).pack(pady=5)

        self.question_frame = tk.Frame(self.root, bg=COLORS["very_light_blue"])
        self.question_frame.pack(pady=10)

        self.topic_label = tk.Label(self.question_frame, text="", font=("Arial", 14, "bold"), bg=COLORS["very_light_blue"], fg=COLORS["dark_blue"])
        self.topic_label.pack()

        self.question_label = tk.Label(self.question_frame, text="", font=("Arial", 12), bg=COLORS["very_light_blue"])
        self.question_label.pack()

        self.code_label = tk.Label(self.question_frame, text="", font=("Courier", 12), bg=COLORS["very_light_blue"], fg=COLORS["medium_blue"])
        self.code_label.pack()

        self.options_frame = tk.Frame(self.root, bg=COLORS["very_light_blue"])
        self.options_frame.pack()

        self.submit_btn = tk.Button(self.root, text="Submit", bg=COLORS["bright_blue"], fg="white", 
                                    font=("Arial", 12), command=self.check_answer)
        self.submit_btn.pack(pady=10)

        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 12, "bold"), bg=COLORS["very_light_blue"])
        self.feedback_label.pack()

    def generate_question(self):
        """Generate a question based on the entered topic."""
        topic = self.topic_entry.get().strip().lower()
        filtered_questions = [q for q in questions if q["topic"].lower() == topic]

        if not filtered_questions:
            messagebox.showerror("Error", f"No questions found for '{topic}'.\nAvailable topics: {', '.join(AVAILABLE_TOPICS)}")
            return

        self.current_question = random.choice(filtered_questions)
        self.display_question()

    def display_question(self):
        """Display the selected question and options."""
        if not self.current_question:
            return

        self.topic_label.config(text=f"Topic: {self.current_question['topic']}")
        self.question_label.config(text=self.current_question["question"])
        self.code_label.config(text=self.current_question["code"])

        for widget in self.options_frame.winfo_children():
            widget.destroy()

        self.option_buttons = []
        self.selected_answer.set(-1)

        for idx, option in enumerate(self.current_question["options"]):
            btn = tk.Radiobutton(self.options_frame, text=option, variable=self.selected_answer, value=idx, bg=COLORS["very_light_blue"])
            btn.pack(anchor="w")
            self.option_buttons.append(btn)

    def check_answer(self):
        """Check if the selected answer is correct."""
        if self.current_question is None:
            return

        selected = self.selected_answer.get()
        correct = self.current_question["answer"]

        if selected == -1:
            messagebox.showwarning("Warning", "Please select an answer!")
            return

        if selected == correct:
            self.feedback_label.config(text="Correct! 🎉", fg=COLORS["correct"])
        else:
            self.feedback_label.config(text=f"Incorrect. Try again! (Correct: {self.current_question['options'][correct]})", fg=COLORS["incorrect"])

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
