import sqlite3
# Other imports...
from bottle import Bottle, run, template, request, redirect, static_file

# Rest of the code...



# Initialize the Bottle app
app = Bottle()

# SQLite3 database setup
db_path = "gym.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS trainers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS trainees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        trainer_id INTEGER,
        FOREIGN KEY (trainer_id) REFERENCES trainers(id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS workouts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        trainee_id INTEGER,
        hours INTEGER,
        FOREIGN KEY (trainee_id) REFERENCES trainees(id)
    )
""")

conn.commit()

# CRUD operations for trainers
@app.route('/trainers')
def trainers_list():
    cursor.execute("SELECT * FROM trainers")
    trainers = cursor.fetchall()
    return template('trainers', trainers=trainers)

@app.route('/trainer/new', method='GET')
def new_trainer():
    return template('new_trainer')

@app.route('/trainer/new', method='POST')
def add_trainer():
    name = request.forms.get('name')
    cursor.execute("INSERT INTO trainers (name) VALUES (?)", (name,))
    conn.commit()
    redirect('/trainers')

@app.route('/trainer/edit/<id>', method='GET')
def edit_trainer(id):
    cursor.execute("SELECT * FROM trainers WHERE id=?", (id,))
    trainer = cursor.fetchone()
    return template('edit_trainer', trainer=trainer)

@app.route('/trainer/edit/<id>', method='POST')
def update_trainer(id):
    name = request.forms.get('name')
    cursor.execute("UPDATE trainers SET name=? WHERE id=?", (name, id))
    conn.commit()
    redirect('/trainers')

@app.route('/trainer/delete/<id>')
def delete_trainer(id):
    cursor.execute("DELETE FROM trainers WHERE id=?", (id,))
    conn.commit()
    redirect('/trainers')

# CRUD operations for trainees
@app.route('/trainees')
def trainees_list():
    cursor.execute("SELECT * FROM trainees")
    trainees = cursor.fetchall()
    return template('trainees', trainees=trainees)

@app.route('/trainee/new', method='GET')
def new_trainee():
    cursor.execute("SELECT * FROM trainers")
    trainers = cursor.fetchall()
    return template('new_trainee', trainers=trainers)

@app.route('/trainee/new', method='POST')
def add_trainee():
    name = request.forms.get('name')
    trainer_id = request.forms.get('trainer_id')
    cursor.execute("INSERT INTO trainees (name, trainer_id) VALUES (?, ?)", (name, trainer_id))
    conn.commit()
    redirect('/trainees')

@app.route('/trainee/edit/<id>', method='GET')
def edit_trainee(id):
    cursor.execute("SELECT * FROM trainees WHERE id=?", (id,))
    trainee = cursor.fetchone()
    cursor.execute("SELECT * FROM trainers")
    trainers = cursor.fetchall()
    return template('edit_trainee', trainee=trainee, trainers=trainers)

@app.route('/trainee/edit/<id>', method='POST')
def update_trainee(id):
    name = request.forms.get('name')
    trainer_id = request.forms.get('trainer_id')
    cursor.execute("UPDATE trainees SET name=?, trainer_id=? WHERE id=?", (name, trainer_id, id))
    conn.commit()
    redirect('/trainees')

@app.route('/trainee/delete/<id>')
def delete_trainee(id):
    cursor.execute("DELETE FROM trainees WHERE id=?", (id,))
    conn.commit()
    redirect('/trainees')

# CRUD operations for workouts
@app.route('/workouts')
def workouts_list():
    cursor.execute("SELECT * FROM workouts")
    workouts = cursor.fetchall()
    return template('workouts', workouts=workouts)

@app.route('/workout/new', method='GET')
def new_workout():
    cursor.execute("SELECT * FROM trainees")
    trainees = cursor.fetchall()
    return template('new_workout', trainees=trainees)

@app.route('/workout/new', method='POST')
def add_workout():
    trainee_id = request.forms.get('trainee_id')
    hours = request.forms.get('hours')
    cursor.execute("INSERT INTO workouts (trainee_id, hours) VALUES (?, ?)", (trainee_id, hours))
    conn.commit()
    redirect('/workouts')

@app.route('/workout/edit/<id>', method='GET')
def edit_workout(id):
    cursor.execute("SELECT * FROM workouts WHERE id=?", (id,))
    workout = cursor.fetchone()
    cursor.execute("SELECT * FROM trainees")
    trainees = cursor.fetchall()
    return template('edit_workout', workout=workout, trainees=trainees)

@app.route('/workout/edit/<id>', method='POST')
def update_workout(id):
    trainee_id = request.forms.get('trainee_id')
    hours = request.forms.get('hours')
    cursor.execute("UPDATE workouts SET trainee_id=?, hours=? WHERE id=?", (trainee_id, hours, id))
    conn.commit()
    redirect('/workouts')

@app.route('/workout/delete/<id>')
def delete_workout(id):
    cursor.execute("DELETE FROM workouts WHERE id=?", (id,))
    conn.commit()
    redirect('/workouts')

# Define templates for rendering HTML
@app.route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static')

@app.route('/')
def index():
    return template('index')

# Run the application
if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
