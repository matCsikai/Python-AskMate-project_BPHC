from flask import Flask, render_template, request
import csv
import common
app = Flask(__name__)


@app.route('/question/<question_id>', methods=['GET', 'POST']) # ???
def all_answers(question_id):
    answer_database = common.read_data('answer.csv')
    question_database = common.read_data('question.csv')
    for data_line in question_database:
        if question_id == data_line[0]:
            question_line = data_line
            print(question_line)
            

    
    return render_template ('all_answers.html', question_line=question_line)





if __name__ == "__main__":
    app.run(debug=True)