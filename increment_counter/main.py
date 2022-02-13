import functions_framework
import json
from google.cloud import firestore

client = firestore.Client()


@functions_framework.http
def increment_counter(request):
    # Load the doc from the firestore
    doc = client.collection(u'visits').document(u'iAz4JOHFJPPHBBtWdojK')
    # pull the current value. I'm supposed to be able to use .get('count')
    # But even if I do... I still have to convert to dict and then pull the count out anyways.
    cur_val = doc.get().to_dict()['count']
    # set up a new object with the count updated
    new_data = {'count': cur_val + 1}
    # use it to set the new count
    doc.set(new_data)
    # and return it as a json object with the new count
    return json.dumps(new_data)
