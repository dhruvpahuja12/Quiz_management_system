from flask import Flask, render_template, request
import main

app = Flask(__name__)

# Your MCQExamPlatform class and other code here...

# Your MCQExamPlatform instance (create_exam) should be created outside the route functions.

create_exam = main.MCQExamPlatform()

# Routes for the frontend
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_name = request.form['user_name']
        create_exam.register_user(user_name)
        return render_template('register.html', user_name=user_name)
    return render_template('register.html')

@app.route('/conduct_exam', methods=['GET', 'POST'])
def conduct_exam():
    if request.method == 'POST':
        user_name = request.form['user_name']
        exam_name = request.form['exam_name']
        create_exam.conduct_exam(user_name, exam_name)
        user_score = create_exam.users[user_name]
        exam = create_exam.exams[exam_name]
        return render_template('exam_result.html', user_name=user_name, exam_name=exam_name, user_score=user_score, total_questions=len(exam.questions))
    return render_template('conduct_exam.html', exam_names=create_exam.exams.keys())

if __name__ == "__main__":
    app.run(debug=True)