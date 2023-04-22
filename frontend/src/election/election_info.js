import { useLoaderData } from "react-router-dom";
import { set_voters, vote_start, vote_end, voting } from "../blockchain";
import { store } from "../store";

const CryptoJS = require("crypto-js");

export async function electioninfo_loader({params}){
    const res = await fetch("http://127.0.0.1:5000/election/get_election_info", {
      method: "post",
      headers: {"Content-Type": "application/json"}, 
      body: JSON.stringify({election_id: params.electionid})
    })
    return res.json()
  }

async function set_voter(proposal_id){
    fetch("http://127.0.0.1:5000/vote/set_participate", {
        method: "post",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({participation:[], id:proposal_id, permission:"voter"})
    }).then((res)=>{
        return res.json();
    }).then((res)=>{
        console.log(res.participation_list, res.participation_id);
        set_voters(proposal_id, res.participation_list, res.participation_id);
    })
}

async function submit_secret(proposal_id, status){
    if(status!="end"){
        return;
    }
    var sballotkey = document.getElementById('sballotkey').value;
    console.log(sballotkey);
    var user_address = store.getState().user_info.address;
    fetch("http://127.0.0.1:5000/vote/submit_secret", {
        method: "post",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({key:sballotkey, vote_id:proposal_id, address:user_address})
    }).then((res)=>{
        window.alert('Submit Success!');
    })
}

function submit_eballot(proposal_id){
    var user_id = store.getState().user_info.userid;
    var eballot = document.getElementById('ballot').value;
    var ballotkey = document.getElementById('ballotkey').value;
    ballotkey = CryptoJS.SHA256(ballotkey);
    const iv = CryptoJS.enc.Utf8.parse("This is an IVVV.");//wait for changing.
    const ciphertext = CryptoJS.AES.encrypt(eballot, ballotkey, { iv: iv }).toString();
    console.log(user_id, ciphertext);
    voting(ciphertext, user_id, proposal_id);
    
}

async function set_candidate(proposal_id){
    var candidate = document.getElementById('candidate').value;
    fetch("http://127.0.0.1:5000/vote/set_candidate", {
        method: "post",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({candidate:[candidate], id:proposal_id, permission:"candidate"})
    }).then((res)=>{
        return res.json();
    }).then((res)=>{
        console.log(res.candidate_list);
        //set_candidate smartcontract
    })
}

function decode(ciphertext, key){
    key = CryptoJS.SHA256(key);
    const iv = CryptoJS.enc.Utf8.parse("This is an IVVV.");
    const plaintext = CryptoJS.AES.decrypt(ciphertext, key, { iv: iv }).toString(CryptoJS.enc.Utf8);
    return plaintext;
}

  

export function Electioninfo(){
    var election_info = useLoaderData();

    return (
        <div className="paperlist default_list">
            <div className="head">
                <h3>{election_info.title}</h3>
                <i className='bx bx-search' ></i>
                <i className='bx bx-filter' ></i>
            </div>
            <table>
                <thead>
                <tr>
                    <th></th>
                    <th></th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td>Title</td>
                    <td>{election_info.title}</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Satus</td>
                    <td>{election_info.status}</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Set voters</td>
                    <td><button onClick={()=>set_voter(election_info.election_id)}>Set</button></td>
                    <td></td>
                </tr>
                <tr>
                    <td>Set candidates</td>
                    <td><input type="text" name="candidate" id="candidate"/></td>
                    <td><button onClick={()=>set_candidate(election_info.election_id)}>Set</button></td>
                </tr>
                <tr>
                    <td>Election Start</td>
                    <td><button onClick={()=>vote_start(election_info.election_id)}>Start</button></td>
                    <td></td>
                </tr>
                <tr>
                    <td>Election End</td>
                    <td><button onClick={()=>vote_end(election_info.election_id)}>End</button></td>
                    <td></td>
                </tr>
                <tr>
                    <td>Submit Ballot</td>
                    <td><input type="text" name="ballot" id="ballot"/></td>
                    <td>Key<input type="text" name="ballotkey" id="ballotkey" /></td>
                    <td style={{textAlign:'left'}} onClick={()=>submit_eballot(election_info.election_id)}><button>Submit</button></td>
                </tr>
                <tr>
                    <td>Submit Ballot Key</td>
                    <td><input type="text" name="sballotkey" id="sballotkey" /></td>
                    <td style={{textAlign:'left'}}><button onClick={()=>{submit_secret(election_info.election_id, election_info.status)}}>Submit</button></td>
                </tr>
                </tbody>
            </table>
        </div>
    )
}