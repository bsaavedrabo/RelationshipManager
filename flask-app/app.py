from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session handling

# Step 1: Display the form to collect names and age
@app.route('/')
def step1():
    return render_template('step1.html')

# Step 2: Save names and age to session and redirect to step 2
@app.route('/save-names', methods=['POST'])
def save_names():
    # Store age and names in session
    session['age'] = request.form['age']
    session['names'] = request.form['fnames'].split(',')  # Convert the comma-separated names into a list
    # Redirect to the next page (Step 2)
    return redirect(url_for('step2'))

# Step 3: Display the second page where the canvas is shown
@app.route('/step2')
def step2():
    # Retrieve names from session
    names = session.get('names', [])
    return render_template('step2.html', names=names)

# Step 4: Fetch the names from the session and send them as JSON
@app.route('/get-names', methods=['GET'])
def get_names():
    names = session.get('names', [])  # Retrieve names from the session
    return jsonify(names)

# Optional: Clear session (for testing or debugging)
@app.route('/clear-session')
def clear_session():
    session.clear()  # Clear all session data
    return redirect(url_for('step1'))  # Redirect back to step 1

if __name__ == '__main__':
    app.run(debug=True)
