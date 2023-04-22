// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract Vote{

    address _constractowner;

    constructor(){
        _constractowner = msg.sender;
    }

    event New_vote(string vote_title, uint vote_id);
    event Voter_set(address voter, uint vote_id);
    event Voting_complete(address voter, string ballot, uint vote_id);
    event Vote_start(uint start_time, uint block_number, uint vote_id);
    event Vote_end(uint end_time, uint block_number, uint vote_id);
    event Esecret_submit(address voter, uint vote_id, string esecret);
    event Esecret_submit_end(uint vote_id);

    struct _voting{
        address _invoker;
        string _title;
        uint _vote_id;
        uint _voting_status;
        uint _timestamp;
        uint _duration;
        uint _count;
        uint _voted;
        uint _voter_amount;
        string _pulickey;
        address [] _candidate;
        mapping(uint=>address) voter_list;
        mapping(address=>string) voter_ballot;
        mapping(address=>bool) hasVoted;
        mapping(address=>string) ballot_esecret;
        mapping(address => string[]) result;
    }

    mapping(uint => _voting) private _vote;
    mapping(uint => bool) private _vote_id_used;

    function new_vote(string memory title, uint vote_id, address [] memory candidates, uint vote_duration) public returns (bool){
        require(!_vote_id_used[vote_id], "ID been used");
        _vote[vote_id]._invoker = msg.sender;
        _vote[vote_id]._vote_id = vote_id;
        _vote[vote_id]._title = title;
        _vote[vote_id]._voting_status = 0;
        _vote[vote_id]._duration = vote_duration;
        _vote_id_used[vote_id] = true;
        set_candidates(candidates, vote_id);
        emit New_vote(title, vote_id);
        return true;
    }

    function set_voter(address voter, uint user_id, uint vote_id) private {
        _vote[vote_id].voter_list[user_id] = voter;
        _vote[vote_id]._count++;
        emit Voter_set(voter, vote_id);
    }

    function voting(string memory ballot, uint vote_id, uint voter_id) public{
        require(_vote[vote_id]._voting_status==1);
        require(msg.sender==_vote[vote_id].voter_list[voter_id], "Wrong key");
        _vote[vote_id].voter_ballot[msg.sender] = ballot;
        _vote[vote_id]._voted++;
        emit Voting_complete(msg.sender, ballot, vote_id);
    }

    function voting_start(uint vote_id) public {
        require(_vote[vote_id]._voting_status<1);
        require(msg.sender==_vote[vote_id]._invoker, "No Permission");
        _vote[vote_id]._voting_status ++;
        _vote[vote_id]._timestamp = block.timestamp;
        emit Vote_start(_vote[vote_id]._timestamp, block.number, vote_id);
    }

    function voting_end(uint vote_id) public {
        require(_vote[vote_id]._voting_status==1);
        require(msg.sender==_vote[vote_id]._invoker, "No Permission");
        require(block.timestamp-_vote[vote_id]._timestamp>_vote[vote_id]._duration);
        _vote[vote_id]._voting_status++;
        emit Vote_end(_vote[vote_id]._timestamp, block.number, vote_id);
    }

    function get_ballot(address voter, uint vote_id) public view returns(string memory){
        require(_vote[vote_id]._voting_status>1);
        return _vote[vote_id].voter_ballot[voter];
    }

    function set_candidates(address [] memory candidates, uint vote_id) private {
        require(_vote[vote_id]._voting_status<1);
        _vote[vote_id]._candidate = candidates;
    }

    function set_voters(address [] memory voters, uint [] memory user_id, uint vote_id) public {
        require(_vote[vote_id]._voting_status<1);
        require(msg.sender==_constractowner||msg.sender==_vote[vote_id]._invoker, "No Permission");
        for(uint i = 0; i < voters.length; i++){
            set_voter(voters[i], user_id[i], vote_id);
        }
    }

    function set_publickey(uint vote_id, string memory publickey) public {
        require(msg.sender==_constractowner, "No Permission");
        _vote[vote_id]._pulickey = publickey;
    }

    function get_publickey(uint vote_id) public view returns(string memory){
        return _vote[vote_id]._pulickey;
    }

    function upload_esecret(uint vote_id, string memory esecret) public {
        require(_vote[vote_id]._voting_status==2);
        require(_vote[vote_id].hasVoted[msg.sender]);
        _vote[vote_id].ballot_esecret[msg.sender] = esecret;
        emit Esecret_submit(msg.sender, vote_id, esecret);
    }

    function esecret_submit_end(uint vote_id) public {
        require(_vote[vote_id]._voting_status==2);
        require(msg.sender==_vote[vote_id]._invoker, "No Permission");
        _vote[vote_id]._voting_status++;
        emit Esecret_submit_end(vote_id);
    }

    function set_result(uint vote_id, string [] memory ver_result, address candidate) public {
        require(_vote[vote_id]._voting_status==2);
        require(msg.sender==_constractowner, "No Permission");
        _vote[vote_id].result[candidate] = ver_result;
    }
}