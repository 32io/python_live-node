

import firebase_admin
from firebase_admin import credentials

from firebase_admin import db
All={}
cred = credentials.Certificate("live-node-firebase-adminsdk-53jk9-f26391514d.json")
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://databaseName.firebaseio.com'
})
# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('All')
def save(m):
    ref.set(All)
def load():
   All=ref.get()