import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter
from Media import *

# Fetch the service account key JSON file contents
cred = credentials.Certificate('./serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred)
db = firestore.client()

media_ref = db.collection('Media')

def createMedia(media):
    media_ref.add(media.toDict())
    print(f"[DB] Added:\n{media}")

def readAllMedia():
    docs = media_ref.stream()

    media = []
    for doc in docs:
        new_media = Media()
        new_media.fromDict(doc.to_dict())
        media.append(new_media)
        print(f"[DB] {new_media}")

    return list(media)

def readMediaByTitle(title):
    result = media_ref.where(filter=FieldFilter("title", "==", title)).get()
    if(len(result) == 0):
        print(f"[DB] No media matching \"{title}\".")
    else:
        media = Media()
        media.fromDict(result[0].to_dict())
        print(f"[DB] {media}")

        return media

def updateMediaStatus(docId, status):
    valid_statuses = ['not started', 'in progress', 'finished']
    if status not in valid_statuses:
        print(f"[DB] \"{status}\" is an invalid status.")
    else:
        media_ref.document(docId).update({'status': status})
        print(f"[DB] Set status to {status}.")

def deleteMedia(docId):
    doc = media_ref.document(docId).get()

    if doc.exists:
        print(f"[DB] Deleting Media with ID: \"{docId}\".")
        media_ref.document(docId).delete()
    else:
        print(f"[DB] Cannot delete. Media with ID: \"{docId}\" does not exist.")