from application import app, db
from application.models import ToDoList
from flask import redirect, url_for

@app.route('/add')
def add():
    new_task = ToDoList(task_name="New Task")
    db.session.add(new_task)
    db.session.commit()
    return "Added new task to database"

@app.route('/read')
def read():
    all_tasks = ToDoList.query.all()
    task_string = ""
    for task in all_tasks:
        task_string += "<br>" + task.task_name + "    Completed: " + str(task.completed)
    return task_string

@app.route('/update/<name>')
def update(name):
    first_task = ToDoList.query.first()
    first_task.task_name = name
    db.session.commit()
    return first_task.task_name + " " + str(first_task.completed)

@app.route('/delete')
def delete():
    delete_task = ToDoList.query.first()
    db.session.delete(delete_task)
    db.session.commit()
    return redirect(url_for('read'))

@app.route('/complete/<int:number>')
def complete(number):
    complete_task = ToDoList.query.first()
    if number == 1:
        complete_task.completed = True
        db.session.commit()
    else:
        complete_task.completed = False
        db.session.commit()
    
    return redirect(url_for('read'))