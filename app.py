from flask import Flask, redirect, render_template, request, url_for

from database import db_session, init_db
from forms import TaskForm
from models import ToDo

app = Flask(__name__)
app.config.from_object('settings')

@app.teardown_appcontext
def shutdown_db_session(exception=None):
    db_session.remove()

init_db()

@app.route('/', methods=['GET', ])
def home():
    context = {}
    return render_template('home.html', **context)

@app.route('/list/', methods=['GET', ])
def list_():
    context = {'tasks': ToDo.query.all()}
    return render_template('list.html', **context)

@app.route('/add-task/', methods=['GET', 'POST'])
def add_task():
    form = TaskForm(request.form)
    context = {'form': form}
    if request.method == 'POST' and form.validate():
        task = ToDo(name=form.name.data)
        db_session.add(task)
        try:
            db_session.commit()
        except Exception:
            pass
        return redirect(url_for('home'))
    return render_template('add-task.html', **context)