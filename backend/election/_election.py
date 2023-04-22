from backend.db_operate._db_operate import *
from flask import Flask, request, Blueprint

election_blueprint = Blueprint('election',__name__)

@election_blueprint.route('/myelection', methods=['GET','POST'])
def myelection():
    print(request.json)
    requests = request.json
    electionlist = get_myelection(requests['user_id'])
    return {'electionlist': electionlist}

@election_blueprint.route('/get_election_info', methods=['GET', 'POST'])
def get_election_info():
    print(request.json)
    requests = request.json
    election = get_election_info_db(requests['election_id'])
    print(election)
    return {'title':election.activity_name, 'election_id':requests['election_id'], 'status': election.activity_status}