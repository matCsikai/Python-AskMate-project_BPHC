from flask import Flask, render_template, request, redirect, url_for
from common import read_data, write_data, generate_data_id, time_decode
import time
app = Flask(__name__)


@app.route("/")
@app.route("/questions")
def page_home():
    file_name = "question.csv"
    all_data = read_data(file_name)
    decoded_data = time_decode(all_data)
    return render_template("all_question.html", questions=decoded_data)


@app.route("/question/new", methods=['GET', 'POST'])
def page_questions():
    file_name = "question.csv"
    title = "ASK A QUESTION"
    button_name = "Post your question"
    all_data = read_data(file_name)
    timestamp = int(time.time())
    data_list = []
    if request.method == "POST":
        data_list.append(str(generate_data_id(file_name)))
        data_list.append(str(timestamp))
        data_list.append(' ')  # view number
        data_list.append(' ')  # vote number
        data_list.append(request.form['question_title'])
        data_list.append(request.form['message'])
        data_list.append(' ')  # for picture
        all_data.append(data_list)
        new_data_to_write = write_data(file_name, all_data)
        return redirect(url_for('page_home'))
    return render_template("get_data.html",  title=title, button_name=button_name)


@app.route('/question/<question_id>', methods=['GET', 'POST'])
def all_answers(question_id):
    answer_database = read_data('answer.csv')
    question_database = read_data('question.csv')

    decoded_data_answer = time_decode(answer_database)
    decoded_data_question = time_decode(question_database)

    answers = []
    for data_line in decoded_data_answer:
        if str(question_id) in data_line[3]:
            answers.append(data_line)

    for data_line in decoded_data_question:
        if str(question_id) in data_line[0]:
            question_line = data_line
    return render_template('all_answers.html', question_line=question_line, answers=answers)


@app.route('/question/<question_id>/new-answer', methods=['GET', 'POST'])
def new_answer(question_id):
    question_database = read_data('question.csv')
    for line in question_database:
        if str(question_id) in line[0]:
            question_line = line

    file_name = "answer.csv"
    button_name = "Post your answer"
    all_data = read_data(file_name)
    timestamp = int(time.time())
    data_list = []
    if request.method == "POST":
        data_list.append(str(generate_data_id(file_name)))
        data_list.append(str(timestamp))
        data_list.append(' ')  # view number
        data_list.append(question_id)
        data_list.append(request.form['message'])
        data_list.append(' ')  # for picture
        all_data.append(data_list)
        new_data_to_write = write_data(file_name, all_data)
        return redirect(url_for('all_answers', question_id=question_id))
    return render_template("add_answer.html", question_line=question_line)


if __name__ == "__main__":
    app.run()
