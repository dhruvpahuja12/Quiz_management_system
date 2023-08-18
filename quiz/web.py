from flask import Flask, render_template, request
import main

app = Flask(__name__, template_folder="templates")

create_exam = main.MCQExamPlatform()
create_exam.create_exam("maths")
create_exam.add_question_to_exam("maths", "2+2?", "1,4,5,6", "2")
create_exam.add_question_to_exam("maths", "4+9?", "1,4,13,6", "3")
print(create_exam.exams)
# Routes for the frontend
@app.route('/register')
def register():
    # if request.method == 'POST':

    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def home():
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
        return render_template('exam.html', user_name=user_name, exam_name=exam_name, user_score=user_score, total_questions=exam.questions)
    return render_template('conduct_exam.html', exam_names=create_exam.exams.keys())


if __name__ == "__main__":
    app.run(debug=True)