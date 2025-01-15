from flask import Blueprint
from app.extensions import mongo

api = Blueprint('API', __name__, url_prefix='/api')

@api.route('/events')
def fetch_events():
    # Fetch the latest 10 events from MongoDB
    events = mongo.db.collection.find().sort('timestamp').limit(10)
    # Convert ObjectId to string for each event
    result = []
    for event in events:
        if '_id' in event:
            event['_id'] = str(event['_id'])
        result.append(event)

    return {'events': result}