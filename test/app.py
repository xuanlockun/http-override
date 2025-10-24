from flask import Flask, request, render_template, redirect, url_for, session, flash
import random

app = Flask(__name__)
app.secret_key = "i_love_defcon_haha"

LOGIN_USERNAME = "john3236"
LOGIN_PASSWORD = "johnPassword@!32369"

messages = {
    1: "Hello admin, yes i got your account you sent me username: john3236, password: johnPassword@!32369",
    2: "Middle age orange duck 38 years old live in Da Nang need to be gone ",
    3: "Old green duck 53 years old live in Ha Noi need to be gone",
    4: "Young pink duck 21 years old live in Thanh Hoa need to be gone",
    5: "Default response message."
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    message = request.form.get('message')
    messages[5] = message
    flash("Message saved to /messages/5")
    return redirect(url_for('show_message', message_id=5))

@app.route('/messages/<int:message_id>')
def show_message(message_id):
    content = messages.get(message_id, "No message found.")
    return render_template('message.html', message_id=message_id, content=content)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username', '')
        pwd = request.form.get('password', '')
        if user == LOGIN_USERNAME and pwd == LOGIN_PASSWORD:
            session['logged_in'] = True
            session['user'] = user
            flash("Login successful.")
            return redirect(url_for('dashboard', user=user))
        else:
            flash("Invalid username or password.")
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out.")
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        flash("You must be logged in to view the dashboard.")
        return redirect(url_for('login'))

    viewed_user = request.args.get('user', session.get('user'))
    flag = None

    if viewed_user == "admin":
        flag = "v1t{u_h4v3_c4ught_th3_duck}"

    return render_template('dashboard.html', viewed_user=viewed_user, flag=flag)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=False)

