from flask import Flask, render_template, jsonify
app = Flask(__name__)

Jobs =[
    {
       'id' : 1,
       'title': "Data Analyst",
       'location' : "Gurugram, India",
        'salary' : "INR 4,00,000"
    },
    {
       'id' : 2,
       'title': "Data Engineer",
       'location' : "Bengaluru,India",
        'salary' : "INR 7,00,000"
    },
    {
       'id' : 3,
       'title': "DevOps Engineer",
       'location' : "Hybrid",
        'salary' : "INR 10,00,000"
    },
    {
       'id' : 4,
       'title': "Python Developer",
       'location' : "New Delhi, India",
        'salary' : ""
    }

]
@app.route('/')
def hello_world():
    return render_template('home.html', jobs = Jobs)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(Jobs)

if __name__ == '__main__':
    Flask.run(self = app,debug = True)