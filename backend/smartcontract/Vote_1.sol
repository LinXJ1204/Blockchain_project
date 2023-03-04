// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract Vote{

    address _constractowner;

    constructor(){
        _constractowner = msg.sender;
    }

    event Voter_set(address voter, uint id);
    event Voting_complete(address voter);
    event Vote_start(uint start_time, uint block_number);
    event Vote_end(uint end_time, uint block_number);

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
        mapping(address=>bytes32) voter_ballot;
        mapping(address => bool) hasVoted;
    }

    mapping(uint => _Proposal) private _proposal;
    mapping(uint => bool) private _proposal_id_used;

    function new_proposal(uint proposal_id) public {
        require(msg.sender==_constractowner, "No Permission");
        require(!_proposal_id_used[proposal_id], "ID been used");
        _proposal[proposal_id]._proposal_id = proposal_id;
        _proposal[proposal_id]._voting_status = 0;
        _proposal_id_used[proposal_id] = true;
    }

    function set_duration(uint duration, uint proposal_id) public {
        require(msg.sender==_constractowner, "No Permission");
        require(_proposal[proposal_id]._voting_status<1);
        _proposal[proposal_id]._duration = duration;
    }

    function set_voter_list(address voter, uint proposal_id) private {
        uint count = _proposal[proposal_id]._count;
        _proposal[proposal_id].voter_list[count] = voter;
        _proposal[proposal_id]._count++;
        emit Voter_set(voter, count);
    }

    function voting(bytes32 ballot, uint proposal_id, uint voter_id) public{
        require(_proposal[proposal_id]._voting_status==1);
        require(msg.sender==_proposal[proposal_id].voter_list[voter_id], "Wrong key");
        _proposal[proposal_id].voter_ballot[msg.sender] = ballot;
        _proposal[proposal_id]._voted++;
        emit Voting_complete(msg.sender);
    }

    function voting_start(uint proposal_id) public {
        require(_proposal[proposal_id]._voting_status<1);
        require(msg.sender==_constractowner, "No Permission");
        _proposal[proposal_id]._voting_status ++;
        _proposal[proposal_id]._timestamp = block.timestamp;
        emit Vote_start(_proposal[proposal_id]._timestamp, block.number);
    }

    function voting_end(uint proposal_id) public {
        require(_proposal[proposal_id]._voting_status==1);
        require(msg.sender==_constractowner, "No Permission");
        require(_proposal[proposal_id]._timestamp-block.timestamp>_proposal[proposal_id]._duration);
        _proposal[proposal_id]._voting_status++;
        emit Vote_end(_proposal[proposal_id]._timestamp, block.number);
    }

    function get_ballot(address voter, uint proposal_id) public view returns(bytes32){
        require(_proposal[proposal_id]._voting_status>1);
        require(msg.sender==_constractowner, "No Permission");
        return _proposal[proposal_id].voter_ballot[voter];
    }

    function set_candidates(address [] memory candidates, uint proposal_id) public {
        require(_proposal[proposal_id]._voting_status<1);
        _proposal[proposal_id]._candidate = candidates;
    }



    function set_voters(address [] memory voters, uint proposal_id) public {
        require(_proposal[proposal_id]._voting_status<1);
        require(msg.sender==_constractowner, "No Permission");
        for(uint i = 0; i < voters.length; i++){
            set_voter_list(voters[i], proposal_id);
        }
    }

}