from flask import Flask, render_template, request, redirect, url_for, g
from database import db, Todo
import os
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "todos.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

todo_list = []
# todo_list.append("Buy milk")
# todo_list.append("Learn more about Azure")
# todo_list.append("Complete first Python project")
# todo_list.append("Learn more about Python")
# todo_list.append("Learn more about Flask")
# todo_list.append("Learn more about Django")
# todo_list.append("Learn more about FastAPI")
# todo_list.append("Learn more about Azure Functions")

# for todo in todo_list:
#     print(todo)

db.init_app(app)
with app.app_context():
    db.create_all()

@app.before_request
def load_data_to_g():
    todos = Todo.query.all()
    g.todos = todos
    g.todo = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_todo():
    # get the data from the form
    todo = Todo(
        name=request.form["todo"],
    )

    # add the new ToDo to the list
    db.session.add(todo)
    db.session.commit()
    
    # add the new ToDo to the list
    return redirect(url_for("index"))

@app.route("/remove/<int:id>", methods=["GET", "POST"])
def remove_todo(id):
    db.session.delete(Todo.query.filter_by(id=id).first())
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)