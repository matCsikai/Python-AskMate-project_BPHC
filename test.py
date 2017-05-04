from flask import Flask, render_template, request
import csv
import common
app = Flask(__name__)


@app.route('/question/<question_id>', methods=['GET', 'POST']) # ???
def all_answers(question_id):
    answer_database = common.read_data('answer.csv')
    question_database = common.read_data('question.csv')
    answers = []
    for data_line in answer_database:
        if str(question_id) in data_line[3]:
            answers.append(data_line)
    print(answers)

    for data_line in question_database:
        if str(question_id) in data_line[0]:
            question_line = data_line
            print(question_line)
    return render_template('all_answers.html', question_line=question_line)

    






if __name__ == "__main__":
    app.run(debug=True)