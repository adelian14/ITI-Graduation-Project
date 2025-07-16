import firebase_admin
from firebase_admin import credentials, firestore, storage
import os

TEMP_DIR = os.path.join(os.path.dirname(__file__), '..', 'temp')
os.makedirs(TEMP_DIR, exist_ok=True)

cred = credentials.Certificate("firebase/teachflow-d25c7-firebase-adminsdk-fbsvc-647469dcf1.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'teachflow-d25c7.firebasestorage.app'
})

db = firestore.client()
bucket = storage.bucket()

