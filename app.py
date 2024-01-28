from flask import Flask, render_template, jsonify
from database import fetch_jobs
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('home.html', jobs = fetch_jobs())

# @app.route('/api/jobs')
# def list_jobs():
#     return jsonify(fetch_jobs())

if __name__ == '__main__':
    Flask.run(self = app,debug = True)