import { store } from "../store";
import axios from 'axios';
import sc_initial from '../blockchain';
import { ethers } from "https://cdnjs.cloudflare.com/ajax/libs/ethers/6.1.0/ethers.min.js";




function set_proposal(proposal_id, title, useraddress){
    return  sc_initial().then((signer)=>{
                let smartcontract_address = '0x4545cc438b5122f8CB249FBCf58486D7defE3715';
                let abi = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"voter","type":"address"},{"indexed":false,"internalType":"uint256","name":"vote_id","type":"uint256"},{"indexed":false,"internalType":"string","name":"esecret","type":"string"}],"name":"Esecret_submit","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"Esecret_submit_end","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"vote_title","type":"string"},{"indexed":false,"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"New_vote","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"end_time","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"block_number","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"Vote_end","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"start_time","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"block_number","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"Vote_start","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"voter","type":"address"},{"indexed":false,"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"Voter_set","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"voter","type":"address"},{"indexed":false,"internalType":"string","name":"ballot","type":"string"},{"indexed":false,"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"Voting_complete","type":"event"},{"inputs":[{"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"esecret_submit_end","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"voter","type":"address"},{"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"get_ballot","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"get_publickey","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"title","type":"string"},{"internalType":"uint256","name":"vote_id","type":"uint256"},{"internalType":"address[]","name":"candidates","type":"address[]"},{"internalType":"uint256","name":"vote_duration","type":"uint256"}],"name":"new_vote","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"vote_id","type":"uint256"},{"internalType":"string","name":"publickey","type":"string"}],"name":"set_publickey","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"vote_id","type":"uint256"},{"internalType":"string[]","name":"ver_result","type":"string[]"},{"internalType":"address","name":"candidate","type":"address"}],"name":"set_result","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"voters","type":"address[]"},{"internalType":"uint256[]","name":"user_id","type":"uint256[]"},{"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"set_voters","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"vote_id","type":"uint256"},{"internalType":"string","name":"esecret","type":"string"}],"name":"upload_esecret","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"ballot","type":"string"},{"internalType":"uint256","name":"vote_id","type":"uint256"},{"internalType":"uint256","name":"voter_id","type":"uint256"}],"name":"voting","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"voting_end","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"voting_start","outputs":[],"stateMutability":"nonpayable","type":"function"}];
                const contract = new ethers.Contract(smartcontract_address, abi, signer);
                //duration has not been set!!
                contract.new_vote(title, proposal_id, [useraddress] ,150).then(()=>{window.alert('Apply ok')})
            })
}

function applydb(title){
    var user_id = store.getState().user_info.userid;
    var useraddress = store.getState().user_info.address;
    console.log(useraddress);
   axios({
    method: 'post',
    url: "http://127.0.0.1:5000/review/submit_paper",
    data: ({user_id: user_id, title:title, user_address:useraddress})
  }).then(response => {
    set_proposal(response.data.data, title, useraddress)
})
}

export function Apply(){

    return(
        <div className="apply ">
            <div>
                    <table>
                        <thead>
                        <tr>
                            <th></th>
                            <th></th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>
                            <p>Paper Title</p>
                            </td>
                            <td><input type="text" name="papertitle" id="papertitle" /></td>
                        </tr>
                        <tr>
                            <td>
                            <p>paper_field</p>
                            </td>
                            <td>
                                <select>
                                    <option>Distributed System</option>
                                    <option>Network</option>
                                    <option>Crypto</option>
                                </select>
                            </td>
                        </tr>
                        <tr>
                            <td>Abstract</td>
                            <td>
                                <textarea id="paper_abstract" rows={15} cols={65}></textarea>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                    <input className= 'applypaperbuttom' type="submit" value="Apply" onClick={()=>{
                        var paper_title = document.getElementById('papertitle').value;
                        applydb(paper_title)}}/>
                        
            </div>
        </div>
    )
}


export default Apply;