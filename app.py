from flask import Flask, render_template, request
from data import questions, responses

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():  # put application's code here
    if request.method == "POST":

        data = request.form.to_dict()
        score = 0
        for question, number in data.items():
            score += int(number)

        print(score)
        if score >= 90:
            return render_template("results.html", response=responses[0], score=score)
        elif score >= 75:
            return render_template("results.html", response=responses[1], score=score)
        elif score >= 50:
            return render_template("results.html", response=responses[2], score=score)
        elif score >= 25:
            return render_template("results.html", response=responses[3], score=score)
        elif score >= 0:
            return render_template("results.html", response=responses[4], score=score)
    else:
        return render_template("index.html", questions=questions)


if __name__ == '__main__':
    app.run()

