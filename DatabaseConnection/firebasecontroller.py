import pyrebase
import logging
from DatabaseConnection import CredentialHelper as credential


class firebase_controller(object):

    def __init__(self, service):
        super().__init__()
        self.service = service

    # this is to make a DatabaseConnection Connection with firebase DatabaseConnection service

    @staticmethod
    def database_connect():
        firebase = pyrebase.initialize_app(credential.firebaseConfig)
        if firebase is None:
            print("error")
            logging.error("problem while connecting to server")
        else:
            logging.debug("database connected")
            return firebase.database()

    # this is to get the database data from the firebase DatabaseConnection

    def get_service_data(self):
        database = self.database_connect().get()
        flag = False
        for i in range(len(database.pyres)):
            if database.pyres[i].key() == self.service:
                logging.debug("data fetched")
                flag = True
                return database.pyres[i]
        if not flag:
            logging.error("service not available")
            print("test")
            return "service currently not available"


# this main class is just for demo purposes
if __name__ == "__main__":
    data = " enter here your database name "
    db = firebase_controller(data)
