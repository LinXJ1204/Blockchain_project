from backend.db_operate._db_operate import *
from flask import request, Blueprint


review_blueprint = Blueprint('review',__name__)

@review_blueprint.route('/submit_paper', methods=['GET', 'POST'])
def submit_paper():
    print(request.json)
    requests = request.json
    paper_apply(requests['user_id'], requests['title'])
    proposal_id = set_proposal(requests['title'], 'review', requests['user_address'])
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

@review_blueprint.route('/get_paper_info', methods=['GET', 'POST'])
def get_paper_info():
    print(request.json)
    requests = request.json
    paper = get_paper_info_db(requests['paper_id'])
    print(paper)
    return {'title':paper.paper_title,'status':paper.paper_status, 'paper_id':paper.paper_id}

@review_blueprint.route('/get_paper_review', methods=['GET', 'POST'])
def get_paper_review():
    print(request.json)
    requests = request.json
    field = requests['field']
    paper_review_list = get_paper_review_db(field)
    return paper_review_list



