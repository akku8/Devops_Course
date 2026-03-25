from flask import Flask, render_template,request
from datetime import datetime
import requests 
BACKEND_URL = 'http://0.0.0.0:9000'

app = Flask(__name__)

@app.route('/')
def home():
    day = datetime.today().strftime('%A')
    return render_template('index.html', day = day)


@app.route('/submit', methods=['POST'])
def submit():
    try:

        form_data = dict(request.form)
        response = requests.post(BACKEND_URL + '/submit', json =form_data)
        if response.status_code == 200:
            return "Data Submitted Successfully"

        else:
            error_msg = response.json().get("error", "Something went wrong")
            return render_template("index.html", error=error_msg)

    except Exception as e:
        return render_template("index.html", error=str(e))
    
if __name__ == '__main__' :
    app.run(debug=True)
