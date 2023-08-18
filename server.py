from flask import Flask, render_template, request, redirect, url_for, g
from flask_socketio import SocketIO, emit
import psycopg2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['DATABASE'] = {
    'dbname': 'user_info_db',
    'user': 'heinhtet',
    'password': 'root',
    'host': 'localhost'
}
socketio = SocketIO(app, async_mode='eventlet')

active_streams = {}

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(**app.config['DATABASE'])
    return g.db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/broadcast')
def broadcast():
    username = request.args.get('username', 'Anonymous')
    return render_template('broadcast.html', username=username)

@app.route('/viewer')
def viewer():
    username = request.args.get('username', 'Anonymous')
    return render_template('viewer.html', username=username)

@app.route('/show_registration')
def show_registration():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
    except psycopg2.Error as e:
        print("Error registering user:", e)
        conn.rollback()
    finally:
        cur.close()

    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user_type = request.form['user_type']

    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()
        if user:
            # User credentials are valid, redirect to the appropriate page
            if user_type == 'broadcast':
                return redirect(url_for('broadcast', _scheme='http', _external=True, username=username))
            elif user_type == 'viewer':
                return redirect(url_for('viewer', _scheme='http', _external=True, username=username))
        else:
            # Invalid credentials, redirect back to the index page
            return redirect(url_for('index', _scheme='http', _external=True))
    except psycopg2.Error as e:
        print("Error logging in:", e)
    finally:
        cur.close()

    return redirect(url_for('index', _scheme='http', _external=True))

@socketio.on('connect')
def handle_connect():
    username = request.args.get('username', 'Anonymous')
    emit('user_connected', {'user_id': request.sid, 'username': username, 'logged_in': True}, broadcast=True)
    for stream_id in active_streams:
        stream = active_streams[stream_id]
        if stream['broadcaster_id'] == request.sid:
            emit('stream_started', {'user_id': request.sid, 'username': username}, broadcast=True)
        else:
            emit('stream_viewer_connected', {'user_id': request.sid, 'username': username, 'stream_id': stream_id}, broadcast=True)

@socketio.on('message')
def handle_message(data):
    emit('message', {'user_id': request.sid, 'username': data['username'], 'content': data['content']}, broadcast=True)

@socketio.on('start_stream')
def handle_start_stream(data):
    username = data['username']
    active_streams[request.sid] = {'username': username, 'broadcaster_id': request.sid}
    emit('stream_started', {'user_id': request.sid, 'username': username}, broadcast=True)

@socketio.on('stop_stream')
def handle_stop_stream():
    if request.sid in active_streams:
        username = active_streams[request.sid]['username']
        del active_streams[request.sid]
        emit('stream_stopped', {'user_id': request.sid, 'username': username}, broadcast=True)

def create_table():
    conn = psycopg2.connect(**app.config['DATABASE'])
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    create_table()
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
