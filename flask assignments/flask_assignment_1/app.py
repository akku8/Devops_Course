from flask import Flask
import json


app = Flask(__name__)

@app.route('/api')
def api():
    f = open('backend_file', 'r+')
    wri = json.load(f)
    print(wri)
    return wri


if __name__ == '__main__' :
    app.run(debug=True)
