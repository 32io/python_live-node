All={}

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("live-node-firebase-adminsdk-53jk9-f26391514d.json")
firebase_admin.initialize_app(cred)


def save(m):
    with open("Manager.m","wb") as f:
        pickle.dump(m,f)
def load():
    with open("Manager.m","rb") as f:
        return pickle.load(f)