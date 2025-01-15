from flask import Blueprint, request, abort
import logging
from sys import stderr
from app.extensions import mongo
import datetime

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

logging.basicConfig(stream=stderr)

@webhook.route('/receiver', methods=["POST"])
def receiver():
    action = request.headers.get('X-GitHub-Event')  # X-GitHub-Event specifies the type of event that occurred
    try:
        payload = request.json 
    except Exception:
        logging.warning('Request parsing failed')
        abort(400)
    author=""
    from_branch=""
    to_branch=""
    request_id=''
    timestamp=''

    if action == 'push':
        # means that a new branch is created
        if payload['before']=='0000000000000000000000000000000000000000':
            return {'status': 'success'}, 200
            
        head_commit = payload['head_commit']
        author = head_commit['author']['username']
        to_branch = payload['ref'].split('/')[-1]
        request_id = head_commit['id']
        timestamp = datetime.datetime.fromisoformat(head_commit['timestamp'])
        # dt = datetime.datetime.strptime(timestampTZ, '%Y-%m-%dT%H:%M:%SZ')
        # utc_time = dt.astimezone(datetime.timezone.utc)
        # timestamp = utc_time.isoformat()
    
    elif action == "pull_request": 
        pull_request = payload['pull_request']
        from_branch = pull_request['head']['ref']
        to_branch = pull_request['base']['ref']
        request_id = pull_request['id']

        if payload['action']=='opened':
            # opened a new PR (means this will not run when any commit pushed to PR branch)
            author = pull_request['user']['login']
            timestamp = datetime.datetime.strptime(pull_request['created_at'],"%Y-%m-%dT%H:%M:%SZ")
        
        elif payload['action'] == 'closed' and payload['pull_request']['merged']:
            # this is a merge action
            action = 'merge'
            author = pull_request['merged_by']['login']
            timestamp = datetime.datetime.strptime(pull_request['merged_at'],"%Y-%m-%dT%H:%M:%SZ")

        else:
            logging.warning(payload['action']+' pull request action is not supported')
            abort(400)
    
    else:
        logging.warning(f'{action} action is not supported')
        abort(400)

    print(timestamp)

    mongo.db.collection.insert_one({
        'action': action.upper(),
        'request_id':request_id,
        'author': author,
        'from_branch': from_branch,
        'to_branch': to_branch,
        'timestamp': timestamp.replace(microsecond=0).strftime('%d %B %Y - %I:%M %p UTC')
    })

    return {'status': 'success'}, 200
