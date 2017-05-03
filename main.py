from flask import Flask, render_template, request, redirect, url_for
from common import read_data, write_data, generate_data_id
app = Flask(__name__)


@app.route("/")
@app.route("/questions")
def page_home():
    file_name = "question.csv"
    all_data = read_data(file_name)
    return render_template("all_question.html", questions=all_data)

if __name__ == "__main__":
    app.run()
