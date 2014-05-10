from flask import render_template, redirect, url_for
from zapas import app, db

@app.route('/')
def index():
    valves = db.valves.find({})
    print valves
    return render_template('index.html', valves=valves)

@app.route('/edit')
def edit():
    pass

if __name__ == '__main__':
# Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)