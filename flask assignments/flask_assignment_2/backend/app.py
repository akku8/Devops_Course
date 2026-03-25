from flask import Flask, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
import certifi
from dotenv import load_dotenv
import jsonify

load_dotenv()

MONGO_URI =os.getenv('uri')

# Create a new client and connect to the server
client = MongoClient(MONGO_URI, tlsCAFile=certifi.where(),server_api=ServerApi('1'))

# Send a ping to confirm a successful connection

db = client.test
collection = db['flask-tutorial']


app = Flask(__name__)


@app.route('/submit', methods=['POST'])
def submit():
    try:
        form_data = dict(request.json)

        if not form_data:
            return {"error": "No data received"}, 400

        collection.insert_one(form_data)

        return {"message": "Data submitted successfully"}, 200

    except Exception as e:
        return {"error": str(e)}, 500
    



if __name__ == '__main__' :
    app.run(host='0.0.0.0',port=9000,debug=True)
