// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract Vote{
    address _constractowner;
    uint _voter_amount;
    uint _voted;
    bool _voting_status;
    uint _timestamp;
    uint _duration;
    uint _count;
    address [] _candidate;

    constructor(uint voter_amount, uint duration){
        _constractowner = msg.sender;
        _voter_amount = voter_amount;
        _voted = 0;
        _voting_status = false;
        _duration = duration;
        _count = 0;
    }
    mapping(uint=>address) voter_list;
    mapping(address=>bytes32) voter_ballot;

    event Voter_set(address voter, uint id);
    event Voting_complete(address voter);
    event Vote_start(uint start_time);
    event Vote_end(uint end_time);

    function set_voter_list(address voter) private {
        voter_list[_count] = voter;
        _count++;
        emit Voter_set(voter, _count-1);
    }

    function voting(bytes32 ballot) public{
        require(msg.sender==voter_list[_count], "Wrong key");
        voter_ballot[msg.sender] = ballot;
        _voted++;
        emit Voting_complete(msg.sender);
    }

    function voting_start() public {
        require(msg.sender==_constractowner, "No Permission");
        _voting_status = true;
        _timestamp = block.timestamp;
        emit Vote_start(_timestamp);
    }

    function voting_end() public {
        require(msg.sender==_constractowner, "No Permission");
        require(_timestamp-block.timestamp>_duration);
        _voting_status = false;
        emit Vote_end(_timestamp);
    }

    function get_ballot(address voter) public view returns(bytes32){
        require(msg.sender==_constractowner, "No Permission");
        return voter_ballot[voter];
    }

    function set_candidates(address [] memory candidates) public {
        _candidate = candidates;
    }

    function set_voters(address [] memory voters) public {
        require(msg.sender==_constractowner, "No Permission");
        for(uint i = 0; i < voters.length; i++){
            set_voter_list(voters[i]);
        }
    }

}