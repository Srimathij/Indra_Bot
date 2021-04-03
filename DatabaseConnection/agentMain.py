from flask import Flask
from DatabaseConnection import firebasecontroller as firebase_controller
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)


# this is to create a webHook for the DialogueFlow

@app.route("/", methods=['POST', 'GET'])
def data():
    Database = firebase_controller.firebase_controller("Your DatabaseConnection name here ")
    data_from_database = Database.get_service_data()
    return data_from_database


# as the DialogueFlow requires a Https WebHook Url we use Flask Nagrok to make a temporary WebLink for
# testing purpose but later on we can also use the a paid service like Heroku or AWS


# run the app
if __name__ == '__main__':
    app.run()
