import bcrypt
import pymongo
from flask import Flask, render_template, request, url_for, redirect, session
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

# set app as a Flask instance
app = Flask(__name__)
# encryption relies on secret keys so they could be run
app.secret_key = os.environ.get('SECRET_KEY')

# connect to your Mongo DB database
client = pymongo.MongoClient(os.environ.get('MONGO_URI'))

# get the database name
db = client.get_database('DB_NAME')
users = db[os.environ.get('USERS_COLLECTION')]


@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


if __name__ == "__main__":
    app.secret_key = os.environ.get('SECERT_KEY')
    app.run('127.0.0.1', 5000, debug=True)