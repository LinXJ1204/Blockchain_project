// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract Vote{

    address _constractowner;

    constructor(){
        _constractowner = msg.sender;
    }

    event Voter_set(address voter, uint proposal_id);
    event Voting_complete(address voter, string ballot, uint proposal_id);
    event Vote_start(uint start_time, uint block_number, uint proposal_id);
    event Vote_end(uint end_time, uint block_number, uint proposal_id);

    struct _Proposal{
        uint _proposal_id;
        uint _voting_status;
        uint _timestamp;
        uint _duration;
        uint _count;
        uint _voted;
        uint _voter_amount;
        address [] _candidate;
        mapping(uint=>address) voter_list;
        mapping(address=>string) voter_ballot;
        mapping(address=>bool) hasVoted;
    }

    mapping(uint => _Proposal) private _proposal;
    mapping(uint => bool) private _proposal_id_used;

    function new_proposal(uint proposal_id, uint proposal_duration) public returns (bool){
        require(msg.sender==_constractowner, "No Permission");
        require(!_proposal_id_used[proposal_id], "ID been used");
        _proposal[proposal_id]._proposal_id = proposal_id;
        _proposal[proposal_id]._voting_status = 0;
        _proposal[proposal_id]._duration = proposal_duration;
        _proposal_id_used[proposal_id] = true;
        return true;
    }

    function set_duration(uint duration, uint proposal_id) public {
        require(msg.sender==_constractowner, "No Permission");
        require(_proposal[proposal_id]._voting_status<1);
        _proposal[proposal_id]._duration = duration;
    }

    function set_voter_list(address voter, uint user_id, uint proposal_id) private {
        _proposal[proposal_id].voter_list[user_id] = voter;
        _proposal[proposal_id]._count++;
        emit Voter_set(voter, proposal_id);
    }

    function voting(string memory ballot, uint proposal_id, uint voter_id) public{
        require(_proposal[proposal_id]._voting_status==1);
        require(msg.sender==_proposal[proposal_id].voter_list[voter_id], "Wrong key");
        _proposal[proposal_id].voter_ballot[msg.sender] = ballot;
        _proposal[proposal_id]._voted++;
        emit Voting_complete(msg.sender, ballot, proposal_id);
    }

    function voting_start(uint proposal_id) public {
        require(_proposal[proposal_id]._voting_status<1);
        require(msg.sender==_constractowner, "No Permission");
        _proposal[proposal_id]._voting_status ++;
        _proposal[proposal_id]._timestamp = block.timestamp;
        emit Vote_start(_proposal[proposal_id]._timestamp, block.number, proposal_id);
    }

    function voting_end(uint proposal_id) public {
        require(_proposal[proposal_id]._voting_status==1);
        require(msg.sender==_constractowner, "No Permission");
        require(block.timestamp-_proposal[proposal_id]._timestamp>_proposal[proposal_id]._duration);
        _proposal[proposal_id]._voting_status++;
        emit Vote_end(_proposal[proposal_id]._timestamp, block.number, proposal_id);
    }

    function get_ballot(address voter, uint proposal_id) public view returns(string memory){
        require(_proposal[proposal_id]._voting_status>1);
        require(msg.sender==_constractowner, "No Permission");
        return _proposal[proposal_id].voter_ballot[voter];
    }

    function set_candidates(address [] memory candidates, uint proposal_id) public {
        require(_proposal[proposal_id]._voting_status<1);
        _proposal[proposal_id]._candidate = candidates;
    }

    function set_voters(address [] memory voters, uint [] memory user_id, uint proposal_id) public {
        require(_proposal[proposal_id]._voting_status<1);
        require(msg.sender==_constractowner, "No Permission");
        for(uint i = 0; i < voters.length; i++){
            set_voter_list(voters[i], user_id[i], proposal_id);
        }
    }

}