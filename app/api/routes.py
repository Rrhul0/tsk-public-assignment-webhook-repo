from flask import Blueprint
from app.extensions import mongo

api = Blueprint('API', __name__, url_prefix='/api')

@api.route('/events')
def fetch_events():
    events = mongo.db.collection.find().sort('timestamp')
    # Convert ObjectId to string for each event to make json serializable
    result = []
    for event in events:
        if '_id' in event:
            event['_id'] = str(event['_id'])
        result.append(event)

    return {'events': result}