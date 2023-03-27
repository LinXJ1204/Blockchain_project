from backend.db_operate._db_operate import *
from flask import request, Blueprint


review_blueprint = Blueprint('review',__name__)

@review_blueprint.route('/paper_data', methods=['GET', 'POST'])
def paper_data():
    print(request.json)
    requests = request.json
    paper_apply(requests['user_id'], requests['title'])
    proposal_id = set_proposal(requests['title'], 'review')
    return {'data': proposal_id}

@review_blueprint.route('/reviewer_set', methods=['GET', 'POST'])
def reviewer_set():
    print(request.json)
    requests = request.json
    return True

@review_blueprint.route('/reviewer_comment', methods=['GET', 'POST'])
def reviewer_comment():
    print(request.json)
    requests = request.json
    return True

@review_blueprint.route('/reviewer_pass', methods=['GET', 'POST'])
def review_pass():
    print(request.json)
    requests = request.json
    return True