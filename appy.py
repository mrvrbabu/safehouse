from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)


@app.route('/')
def home():
    jobs = load_jobs_from_db()
    return render_template('index.html', jobs=jobs, company_name="SafeHouse")


@app.route('/api/jobs')
def jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
