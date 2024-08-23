from flask import Flask, render_template, request, redirect, url_for, Response, flash

SECRET_KEY = "dev"
app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY

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


def get_id_for_adding(db: list[dict]) -> int:
    if len(db) == 0:
        return 1
    return max([task["id"] for task in db]) + 1


def get_task_from_db(pk: int) -> dict:
    for task in fake_db:
        if task["id"] == pk:
            return task


@app.route("/", methods=["GET"])
def index() -> str:
    return render_template("index.html", task_list=fake_db)


@app.route("/task/create", methods=["POST"])
def create_task() -> Response:
    task_name = request.form.get("name", "").strip()
    if task_name:
        fake_db.append({
            "id": get_id_for_adding(fake_db),
            "name": task_name,
            "done": False
        })
        flash(f"Task created", "success")
    else:
        flash("Please enter a correct name", "danger")
    return redirect(url_for("index"))


@app.route("/task/delete", methods=["POST"])
def task_delete() -> Response:
    task_id = int(request.form.get("id"))

    task = get_task_from_db(task_id)
    if task is not None:
        fake_db.remove(task)
        flash(f"Task deleted", "success")

    return redirect(url_for("index"))


@app.route("/task/toggle", methods=["POST"])
def task_toggle() -> Response:
    task_id = int(request.form.get("id"))

    task = get_task_from_db(task_id)

    if task is not None:
        task["done"] = not task["done"]
        flash(f"Task toggled", "success")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
