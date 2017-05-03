from flask import Flask, render_template, request, redirect, url_for
from common import read_data, write_data, generate_data_id
app = Flask(__name__)


@app.route("/")
@app.route("/questions")
def page_home():
    file_name = "question.csv"
    all_data = read_data(file_name)
    return render_template("all_question.html", questions=all_data)


@app.route("/question/new", methods=['GET', 'POST'])
def page_questions():
    file_name = "question.csv"
    title = "ASK A QUESTION"
    button_name = "Post your question"
    all_data = read_data(file_name)
    data_list = []
    if request.method == "POST":
        data_list.append(str(generate_data_id(file_name)))
        data_list.append("2017-05-08")  # here will the UNIX timestamp added to the list
        data_list.append('')  # view number
        data_list.append('')  # vote number
        data_list.append(request.form['question_title'])
        data_list.append(request.form['message'])
        data_list.append('')  # for picture
        all_data.append(data_list)
        new_data_to_write = write_data(file_name, all_data)
        return redirect(url_for('page_home'))
    return render_template("get_data.html",  title=title, button_name=button_name)


if __name__ == "__main__":
    app.run()
