import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('helloworldfirebase-d2241-firebase-adminsdk-houq9-b99b786071.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
  'databaseURL': 'https://helloworldfirebase-d2241-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('restricted_access/secret_document')
print(ref.get())