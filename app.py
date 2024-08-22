from flask import Flask, render_template

app = Flask(__name__)

fake_db = [
    {
        "id": 1,
        "name": "New task",
        "done": False
    },
    {
        "id": 2,
        "name": "New task 2 ",
        "done": False
    },
    {
        "id": 3,
        "name": "New task 3 ",
        "done": False
    },
]


@app.route("/")
def index() -> render_template:
    return render_template("index.html", task_list=fake_db)


if __name__ == "__main__":
    app.run(debug=True)
