import time
import random

class Question:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

class Exam:
    def __init__(self):
        self.questions = []

    def add_question(self, question, options, correct_option):
        new_question = Question(question, options, correct_option)
        self.questions.append(new_question)

class MCQExamPlatform:
    def __init__(self):
        self.exams = {}
        self.users = {}

    def create_exam(self, exam_name):
        if exam_name in self.exams:
            print("Exam with this name already exists.")
        else:
            exam = Exam()
            self.exams[exam_name] = exam
            print(f"Exam '{exam_name}' created successfully.")

    def add_question_to_exam(self, exam_name, question, options, correct_option):
        if exam_name in self.exams:
            exam = self.exams[exam_name]
            exam.add_question(question, options.split(","), correct_option)
            print("Question added successfully.")
        else:
            print("Exam not found.")

    def register_user(self, user_name):
        if user_name in self.users:
            print("User already registered.")
        else:
            self.users[user_name] = 0
            print(f"User '{user_name}' registered successfully.")

    def conduct_exam(self, user_name, exam_name):
        if user_name in self.users and exam_name in self.exams:
            exam = self.exams[exam_name]
            user_score = self.users[user_name]
            random.shuffle(exam.questions)

            print(f"\nWelcome, {user_name}! The {exam_name} is starting...")
            time.sleep(1)

            for idx, question in enumerate(exam.questions, start=1):
                print(f"\nQuestion {idx}: {question.question}")
                for i, option in enumerate(question.options, start=1):
                    print(f"{i}. {option}")

                user_answer = int(input("Your answer (enter the option number): "))

                if user_answer == question.correct_option:
                    print("Correct answer!")
                    user_score += 1
                else:
                    print("Wrong answer!")

                time.sleep(1)

            self.users[user_name] = user_score
            print("\nExam completed!")
            print(f"{user_name}, your score in {exam_name} is: {user_score}/{len(exam.questions)}")
        else:
            print("Invalid user or exam name.")





# class teacher, student
#     1- create exam
#         2- add question
#     2- type name and exam code from list
#     score print

# Taking input from user
# if __name__ == "__main__":
#     game = True
#     create_exam = MCQExamPlatform()
#     while game:
#         user = input("press 1 for Teacher or 2 for Student: \n")
#
#         if user == "1":
#             # teacher_exam = MCQExamPlatform()
#             input_1 = input("press 1 for Creating Exam or 2 for Adding Questions: \n")
#
#             if input_1 == "1":
#                 time.sleep(1)
#                 exam_name = input("enter Exam Name: ")
#                 create_exam.create_exam(exam_name)
#             elif input_1 == "2":
#                 # Adding question by user Teacher
#                 input_2 = input("No. Question you want to add: ")
#
#                 exam_name = input("Enter exam name: ")
#                 for _ in range(int(input_2)):
#
#                     question = input("Enter your question: ")
#                     options = input("Enter options(comma seperated without spaces): ").split(',')
#                     correct_option = input("Enter correct option number: ")
#                     create_exam.add_question_to_exam(exam_name, question, options, correct_option)
#             else:
#                 print("enter right value.")
#
#         elif user == "2":
#             print("Welcome to Quiz:")
#             student_input = input("press 1 for Adding User or 2 for Conducting Exam: \n")
#
#             # New user registration
#             if student_input == "1":
#                 name = input("Enter your Name: \n")
#                 create_exam.register_user(name)
#
#             # User conducting exam
#             elif student_input == "2":
#                 name = input("Enter your Name: \n")
#                 exam_name = input("Enter Exam Name: \n")
#                 create_exam.conduct_exam(name, exam_name)
#
#             else:
#                 print("enter right value.")
#
#         # if user want to restart the game
#         restart = input("Press 1 to continue or 0 to end.")
#         if restart == "0":
#             game = False
















