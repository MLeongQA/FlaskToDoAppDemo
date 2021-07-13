from application import db

class ToDoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(30))
    completed = db.Column(db.Boolean, default=False)